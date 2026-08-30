#!/usr/bin/env python3
import os, sys, json, time, subprocess, datetime

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 0
DEFAULT_TTL = 86400  # 24 Hours

def get_redis_client():
    try:
        import redis
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, socket_timeout=1)
        r.ping()
        return r
    except Exception:
        # Self-healing attempt: Try starting silent userspace Redis daemon (zero sudo/polkit prompt)
        try:
            subprocess.run(
                ["redis-server", "--daemonize", "yes"],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=1
            )
            time.sleep(0.3)
            import redis
            r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, socket_timeout=1)
            r.ping()
            return r
        except Exception:
            return None

def detect_project_root(start_dir=None):
    current = os.path.abspath(start_dir or os.getcwd())
    while current != os.path.dirname(current):
        if os.path.exists(os.path.join(current, ".git")) or os.path.exists(os.path.join(current, ".agents")) or os.path.exists(os.path.join(current, "GUIDE.md")):
            return current
        current = os.path.dirname(current)
    return os.path.abspath(start_dir or os.getcwd())

def build_project_context(project_root=None):
    root = detect_project_root(project_root)
    project_name = os.path.basename(root).lower().replace(' ', '_').replace('-', '_')
    
    context = {
        "project_name": project_name,
        "project_root": root,
        "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "creator": "Mr. Vishalkumar Joshi",
        "git": {},
        "structure": {},
        "guide_summary": "",
        "pm2_processes": [],
        "skills_status": {}
    }
    
    # 1. Git Information
    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=root, stderr=subprocess.DEVNULL).decode('utf-8').strip()
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=root, stderr=subprocess.DEVNULL).decode('utf-8').strip()
        status_raw = subprocess.check_output(["git", "status", "--short"], cwd=root, stderr=subprocess.DEVNULL).decode('utf-8').strip()
        context["git"] = {
            "branch": branch,
            "commit": commit,
            "modified_files_count": len(status_raw.splitlines()) if status_raw else 0
        }
    except Exception:
        context["git"] = {"branch": "unknown", "commit": "unknown", "modified_files_count": 0}
        
    # 2. Structure & Key Directories
    try:
        top_items = os.listdir(root)
        dirs = [d for d in top_items if os.path.isdir(os.path.join(root, d)) and not d.startswith('.')]
        files = [f for f in top_items if os.path.isfile(os.path.join(root, f)) and not f.startswith('.')]
        context["structure"] = {
            "key_directories": sorted(dirs)[:12],
            "key_files": sorted(files)[:12]
        }
    except Exception:
        pass
        
    # 3. GUIDE.md Summary
    guide_path = os.path.join(root, "GUIDE.md")
    if os.path.exists(guide_path):
        try:
            with open(guide_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]
                context["guide_summary"] = " | ".join(lines[:5])
        except Exception:
            pass

    # 4. PM2 Status
    try:
        pm2_out = subprocess.check_output(["pm2", "jlist"], stderr=subprocess.DEVNULL, timeout=2).decode('utf-8')
        pm2_data = json.loads(pm2_out)
        context["pm2_processes"] = [{"name": p.get("name"), "status": p.get("pm2_env", {}).get("status"), "restarts": p.get("pm2_env", {}).get("restart_time", 0)} for p in pm2_data]
    except Exception:
        context["pm2_processes"] = []

    # 5. Skills status
    ws_skills_dir = os.path.join(root, ".agents", "skills")
    if os.path.exists(ws_skills_dir):
        context["skills_status"]["workspace_skills_count"] = len(os.listdir(ws_skills_dir))
    else:
        context["skills_status"]["workspace_skills_count"] = 0

    return context

def get_project_context(project_root=None, max_age_seconds=DEFAULT_TTL):
    root = detect_project_root(project_root)
    project_name = os.path.basename(root).lower().replace(' ', '_').replace('-', '_')
    redis_key = f"vjp:agent:context:{project_name}"
    local_fallback_path = os.path.join(root, ".agents", "context.json")
    
    r = get_redis_client()
    
    # 1. Try Redis
    if r is not None:
        try:
            cached = r.get(redis_key)
            if cached:
                data = json.loads(cached.decode('utf-8'))
                updated_at_str = data.get("updated_at")
                if updated_at_str:
                    updated_at = datetime.datetime.fromisoformat(updated_at_str)
                    age = (datetime.datetime.now(datetime.timezone.utc) - updated_at).total_seconds()
                    if age < max_age_seconds:
                        data["_source"] = "redis_cache"
                        data["_age_seconds"] = int(age)
                        return data
        except Exception:
            pass
            
    # 2. Try Local Fallback File if Redis missed/offline
    if os.path.exists(local_fallback_path):
        try:
            with open(local_fallback_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                updated_at_str = data.get("updated_at")
                if updated_at_str:
                    updated_at = datetime.datetime.fromisoformat(updated_at_str)
                    age = (datetime.datetime.now(datetime.timezone.utc) - updated_at).total_seconds()
                    if age < max_age_seconds:
                        data["_source"] = "local_json_fallback"
                        data["_age_seconds"] = int(age)
                        return data
        except Exception:
            pass
            
    # 3. Build Fresh Context
    fresh_context = build_project_context(root)
    
    # Save to Redis
    if r is not None:
        try:
            r.set(redis_key, json.dumps(fresh_context), ex=DEFAULT_TTL)
            fresh_context["_source"] = "fresh_build_saved_to_redis"
        except Exception:
            fresh_context["_source"] = "fresh_build_redis_write_failed"
    else:
        fresh_context["_source"] = "fresh_build_redis_offline"
        
    # Save Local Fallback File
    try:
        os.makedirs(os.path.join(root, ".agents"), exist_ok=True)
        with open(local_fallback_path, "w", encoding="utf-8") as f:
            json.dump(fresh_context, f, indent=2)
    except Exception:
        pass
        
    return fresh_context

def update_project_context(project_root=None, extra_data=None):
    root = detect_project_root(project_root)
    context = build_project_context(root)
    if extra_data and isinstance(extra_data, dict):
        context.update(extra_data)
        
    project_name = context["project_name"]
    redis_key = f"vjp:agent:context:{project_name}"
    local_fallback_path = os.path.join(root, ".agents", "context.json")
    
    r = get_redis_client()
    if r is not None:
        try:
            r.set(redis_key, json.dumps(context), ex=DEFAULT_TTL)
        except Exception:
            pass
            
    try:
        os.makedirs(os.path.join(root, ".agents"), exist_ok=True)
        with open(local_fallback_path, "w", encoding="utf-8") as f:
            json.dump(context, f, indent=2)
    except Exception:
        pass
        
    return context

if __name__ == "__main__":
    ctx = get_project_context()
    print(json.dumps(ctx, indent=2))
