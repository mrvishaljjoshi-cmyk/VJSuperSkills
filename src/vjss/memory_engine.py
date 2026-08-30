#!/usr/bin/env python3
import os, sys, json, re, glob, datetime

HOME_DIR = os.path.expanduser("~")
CONVERSATION_DIR = os.environ.get("VJSS_CONVERSATION_DIR", os.path.join(HOME_DIR, "Docs", "conversation"))
CLOSED_POA_DIR = os.environ.get("VJSS_POA_DIR", os.path.join(HOME_DIR, "Docs", "poa", "closed"))
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 0
MEMORY_TTL = 86400 * 7  # 7 Days TTL

def get_redis_client():
    try:
        import redis
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, socket_timeout=1)
        r.ping()
        return r
    except Exception:
        return None

def parse_daily_session_file(file_path, max_entries=5):
    entries = []
    if not file_path or not os.path.exists(file_path):
        return entries
        
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        blocks = re.split(r'🕒\s*\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\s+[A-Z]+)\]\s*CONVERSATION UPDATE', content)
        if len(blocks) > 1:
            for i in range(1, len(blocks), 2):
                timestamp = blocks[i].strip()
                body = blocks[i+1].strip() if (i+1) < len(blocks) else ""
                
                user_input = ""
                agent_understanding = ""
                resolution = ""
                
                u_match = re.search(r'User Input:\s*(.*?)(?=\nAgent Understanding:|\nFinal Resolution:|\Z)', body, re.DOTALL)
                if u_match:
                    user_input = u_match.group(1).strip()
                    
                a_match = re.search(r'Agent Understanding:\s*(.*?)(?=\nFinal Resolution:|\Z)', body, re.DOTALL)
                if a_match:
                    agent_understanding = a_match.group(1).strip()
                    
                r_match = re.search(r'Final Resolution:\s*(.*?)(?=\n\n|\Z)', body, re.DOTALL)
                if r_match:
                    resolution = r_match.group(1).strip()
                    
                entries.append({
                    "timestamp": timestamp,
                    "user_input": user_input[:200],
                    "agent_understanding": agent_understanding[:250],
                    "resolution": resolution[:300],
                    "source_file": file_path
                })
    except Exception as e:
        pass
        
    return entries[-max_entries:]

def parse_recent_closed_poas(max_poas=5):
    poas = []
    if not os.path.exists(CLOSED_POA_DIR):
        return poas
        
    files = sorted(glob.glob(os.path.join(CLOSED_POA_DIR, "*.md")), key=os.path.getmtime, reverse=True)
    for p in files[:max_poas]:
        try:
            name = os.path.basename(p)
            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                
            title_match = re.search(r'#\s*📋\s*Plan of Action.*?:\s*(.*)', content)
            title = title_match.group(1).strip() if title_match else name.replace('.md', '').replace('_', ' ')
            
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(p), tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            
            poas.append({
                "poa_file": name,
                "title": title,
                "completed_at": mtime,
                "path": p
            })
        except Exception:
            pass
            
    return poas

def build_memory_digest():
    session_files = sorted(glob.glob(os.path.join(CONVERSATION_DIR, "*_session.txt")), reverse=True)
    recent_sessions = []
    for sf in session_files[:3]:
        parsed = parse_daily_session_file(sf, max_entries=4)
        recent_sessions.extend(parsed)
        
    recent_poas = parse_recent_closed_poas(max_poas=6)
    
    # Core Architectural Invariants
    core_decisions = [
        "Dynamic ATR Rally Riding (Rules A, B, C, D) for Indian equities, MIS, and options",
        "Centralized AI Master Gateway proxying via http://127.0.0.1:9090",
        "Multi-Cloud Zero-Bill Permanent Always-Free Tier guardrails (OCI, AWS, Azure, GCP)",
        "80/20 Token Shield Guard with targeted line-reads and native progressive disclosure",
        "Self-healing Redis Project Context Cache (vjp:agent:context:<project>)",
        "Universal 1-Click Multi-Tool Bootloader & JIT on-demand skill resolver"
    ]
    
    # Format compact text digest
    digest_lines = [
        f"🧠 VJSS Long-Term Memory & Historical Context (Updated: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}):",
        "• Core Mandates: " + " | ".join(core_decisions[:3]),
        "• Recent Completed POAs:"
    ]
    for poa in recent_poas[:4]:
        digest_lines.append(f"  - [{poa['title']}](file://{poa['path']}) ({poa['completed_at'][:10]})")
        
    if recent_sessions:
        digest_lines.append("• Latest Conversation Highlights:")
        for s in recent_sessions[-3:]:
            digest_lines.append(f"  - [{s['timestamp'][:16]}]: {s['agent_understanding'][:120]}...")
            
    compact_digest_text = "\n".join(digest_lines)
    
    memory_payload = {
        "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "recent_sessions": recent_sessions[-10:],
        "recent_poas": recent_poas,
        "core_decisions": core_decisions,
        "compact_digest": compact_digest_text
    }
    
    return memory_payload

def sync_memory():
    payload = build_memory_digest()
    
    # 1. Save to Redis
    r = get_redis_client()
    if r is not None:
        try:
            r.set("vjp:agent:memory:recent_sessions", json.dumps(payload["recent_sessions"]), ex=MEMORY_TTL)
            r.set("vjp:agent:memory:decisions", json.dumps(payload["core_decisions"]), ex=MEMORY_TTL)
            r.set("vjp:agent:memory:digest", payload["compact_digest"], ex=MEMORY_TTL)
            r.set("vjp:agent:memory:full", json.dumps(payload), ex=MEMORY_TTL)
            payload["_redis_synced"] = True
        except Exception as e:
            payload["_redis_synced"] = False
    else:
        payload["_redis_synced"] = False
        
    # 2. Save Local Fallback File
    ws_fallback = os.path.join(os.getcwd(), ".agents", "memory.json")
    global_fallback = os.path.expanduser("~/.gemini/config/memory.json")
    
    try:
        os.makedirs(os.path.dirname(ws_fallback), exist_ok=True)
        with open(ws_fallback, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
    except Exception:
        pass
        
    try:
        os.makedirs(os.path.dirname(global_fallback), exist_ok=True)
        with open(global_fallback, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
    except Exception:
        pass
        
    return payload

def get_memory():
    r = get_redis_client()
    if r is not None:
        try:
            cached = r.get("vjp:agent:memory:full")
            if cached:
                return json.loads(cached.decode('utf-8'))
        except Exception:
            pass
            
    ws_fallback = os.path.join(os.getcwd(), ".agents", "memory.json")
    if os.path.exists(ws_fallback):
        try:
            with open(ws_fallback, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
            
    return sync_memory()

def search_memory(query):
    query = query.lower()
    results = []
    
    # 1. Search closed POAs
    poa_files = glob.glob(os.path.join(CLOSED_POA_DIR, "*.md"))
    for pf in poa_files:
        try:
            with open(pf, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            if query in text.lower() or query in os.path.basename(pf).lower():
                results.append({
                    "type": "Closed POA",
                    "title": os.path.basename(pf),
                    "file": pf,
                    "snippet": text[:300].replace('\n', ' ')
                })
        except Exception:
            pass
            
    # 2. Search daily conversation sessions
    session_files = glob.glob(os.path.join(CONVERSATION_DIR, "*_session.txt"))
    for sf in session_files[:10]:
        try:
            with open(sf, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            if query in text.lower():
                results.append({
                    "type": "Conversation Session",
                    "title": os.path.basename(sf),
                    "file": sf,
                    "snippet": text[:300].replace('\n', ' ')
                })
        except Exception:
            pass
            
    return results

if __name__ == "__main__":
    mem = sync_memory()
    print("=== Memory Digest ===")
    print(mem["compact_digest"])
