# 🧠 VJSS: Universal AI Agent Super-Skills Ecosystem

[![Creator: Mr. Vishalkumar Joshi](https://img.shields.io/badge/Creator-Mr.%20Vishalkumar%20Joshi-blue.svg)](https://github.com/mrvishaljjoshi-cmyk)
[![Website: vjprojects.co.in](https://img.shields.io/badge/Website-vjprojects.co.in-purple.svg)](https://vjprojects.co.in)
[![Email: mrvishaljjoshi@gmail.com](https://img.shields.io/badge/Email-mrvishaljjoshi%40gmail.com-orange.svg)](mailto:mrvishaljjoshi@gmail.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills: 130 Total](https://img.shields.io/badge/Skills-130%20Total-brightgreen.svg)](INDEX.md)
[![Format: Pure Plain--Text](https://img.shields.io/badge/Format-Pure%20Plain--Text%20(.txt)-blueviolet.svg)](txt_skills/)
[![Gateway: UniversalCopilot](https://img.shields.io/badge/Gateway-VJSS__UniversalCopilot-red.svg)](txt_skills/VJSS_UniversalCopilot.txt)
[![Quality Benchmark](https://img.shields.io/badge/Quality%20Benchmark-100%2F100%20A%2B-brightgreen.svg)](tests/benchmark_suite.py)
[![Web Catalog](https://img.shields.io/badge/Web%20Catalog-Interactive%20Explorer-purple.svg)](web/index.html)
[![CI Quality Gate](https://github.com/mrvishaljjoshi-cmyk/VJSS/actions/workflows/benchmark.yml/badge.svg)](https://github.com/mrvishaljjoshi-cmyk/VJSS/actions)
[![GitHub Stars](https://img.shields.io/github/stars/mrvishaljjoshi-cmyk/VJSS?style=social)](https://github.com/mrvishaljjoshi-cmyk/VJSS)

**VJSS (Vishal Joshi Super-Skills)** is the ultimate production-grade collection of **130 specialized AI engineering protocols and prompt skills**, created and architected by **Mr. Vishalkumar Joshi**. Built in **pure plain-text (`.txt`)**, it gives autonomous AI agents and pair-programming assistants superhuman capabilities across architecture, backend, frontend, cloud, security, and algorithmic fintech.

> ⭐ **If you find VJSS useful, please give it a star on GitHub — it helps the project grow and empowers developers worldwide!**

---

## ⚡ THE CORE PHILOSOPHY: "INSTALL 1st → AUTO-CALL REST"

> [!IMPORTANT]
> **MANDATORY STARTUP, PRIVACY & TOKEN EFFICIENCY PROTOCOL:**
> 1. **100% Local-First Data Sovereignty (Zero Data Egress):** VJSS is completely private and on-device. All project context, conversation memory, and code analysis stay strictly on `127.0.0.1` or your local filesystem. **Zero telemetry, zero tracking, zero third-party analytics.**
> 2. **Always Load On Session Start:** Every AI agent must initialize [`VJSS_UniversalCopilot`](txt_skills/VJSS_UniversalCopilot.txt) on turn 1 of every conversation.
> 3. **Absolute Priority = Save Tokens (80/20 Rule):** Keep context fast and cheap via targeted line reads, compact runbooks, and Redis SmartContext.
> 4. **Auto-Call Specialized Skills & JIT Fetch:** When a domain task is encountered (FastAPI, Docker, React, K8s, OWASP, ATR Backtesting), the AI agent **autonomously loads or JIT-fetches that matching skill in the background**. Zero manual file hunting!

```
                     USER PROMPT (Natural language, brief, or typos)
                                           │
                                           ▼
          ╔═══════════════════════════════════════════════════════════════╗
          ║                  STEP 1: INSTALL THIS 1 SKILL                 ║
          ║                    `VJSS_UniversalCopilot`                    ║
          ║      (Installed in Claude Code / Cursor / Windsurf / etc.)    ║
          ╚═══════════════════════════════════════════════════════════════╝
                                           │
                ┌──────────────────────────┴──────────────────────────┐
                ▼                                                     ▼
     [1. Intent Optimizer]                                 [2. Token Shield Guard]
      • Decodes user objective                              • Strict 80/20 brevity
      • Auto-corrects typos                                 • Targeted line reads
                │                                                     │
                └──────────────────────────┬──────────────────────────┘
                                           │
                                           ▼
                    [3. Autonomous Dynamic Skill Fetcher]
                     • Detects exact domain requirement
                     • AUTONOMOUSLY loads `txt_skills/VJSS_<SkillName>.txt`
                                           │
                                           ▼
          ╔═══════════════════════════════════════════════════════════════╗
          ║              STEP 2: AGENT AUTO-LOADS & EXECUTES              ║
          ║  • Adopts strict engineering SOPs & security checks           ║
          ║  • Delivers working code + Proactive Recommendations          ║
          ║  • ZERO manual skill hunting needed by the user!              ║
          ╚═══════════════════════════════════════════════════════════════╝
```

<p align="center">
  <img src="assets/terminal_demo.svg" alt="VJSS 1-Line Quick Installation Demo" width="100%">
</p>

---

## 🚀 1-Command Universal Installation (All Tools)

### Option A: Remote 1-Liner (Zero Clone Needed)
```bash
# Linux / macOS (All 6 AI Tools):
curl -fsSL https://raw.githubusercontent.com/mrvishaljjoshi-cmyk/VJSS/main/install.sh | bash -s -- --all

# Windows PowerShell:
irm https://raw.githubusercontent.com/mrvishaljjoshi-cmyk/VJSS/main/install.ps1 | iex
```

### Option B: Local Clone & Target Tool Installer
```bash
git clone https://github.com/mrvishaljjoshi-cmyk/VJSS.git
cd VJSS
./install.sh
```

| Tool | 1-Line Command | What It Does |
| :--- | :--- | :--- |
| **🔵 Google Antigravity & Gemini CLI** | `./install.sh --agy` | Syncs 130 native progressive disclosure skills to `~/.gemini/config/skills/` |
| **🟣 Claude Code CLI** | `./install.sh --claude` | Injects VJSS Bootloader into `./CLAUDE.md` with JIT skill fetcher |
| **🟡 Cursor IDE** | `./install.sh --cursor` | Configures `./.cursorrules` and `./.cursor/rules/vjss_universal_copilot.mdc` |
| **🌊 Windsurf IDE (Cascade)** | `./install.sh --windsurf` | Configures `./.windsurfrules` with 80/20 token shield |
| **🟢 VS Code & GitHub Copilot** | `./install.sh --vscode` | Generates `./.github/copilot-instructions.md` |
| **🤖 Roo Code & Cline** | `./install.sh --cline` | Generates `./.clinerules` and `./.roomodes` |
| **⭐ ALL TOOLS** | `./install.sh --all` | Configures all 6 coding tools in one click |

*(Windows users: run `install.bat` or `install.ps1`)*

---

## 🛠️ Manual 1-Click Setup (Top 5 AI Coding Tools)

### 1. 🟣 Claude Code CLI (`claude` / `claude-code`)
```bash
cat txt_skills/VJSS_UniversalCopilot.txt >> CLAUDE.md
```

### 2. 🔵 Google Antigravity CLI (`agy` / Gemini CLI)
```bash
mkdir -p ~/.gemini/config/skills && cp -r categories/*/* ~/.gemini/config/skills/
```

### 3. 🟡 Cursor IDE (`.cursorrules`)
```bash
cat txt_skills/VJSS_UniversalCopilot.txt > .cursorrules
```

### 4. 🌊 Windsurf IDE (Codeium Cascade)
```bash
cat txt_skills/VJSS_UniversalCopilot.txt > .windsurfrules
```

### 5. 🟢 VS Code (GitHub Copilot, Roo-Code, Cline)
* **Roo-Code / Cline:** Open Settings → **Custom Instructions** → Paste the contents of [`txt_skills/VJSS_UniversalCopilot.txt`](txt_skills/VJSS_UniversalCopilot.txt).
* **GitHub Copilot:** `mkdir -p .github && cat txt_skills/VJSS_UniversalCopilot.txt > .github/copilot-instructions.md`

---

## 📁 Repository Directory Structure

```
VJSS/
├── install.sh                       # 1-Click interactive & CLI installer for Linux/macOS
├── install.bat                      # 1-Click installer for Windows
├── txt_skills/                      # Flat library of all 130 .txt files for instant attachment
│   ├── VJSS_UniversalCopilot.txt    # 🌟 THE 1 MASTER GATEWAY SKILL (Install this first)
│   ├── VJSS_PythonFastapi.txt       # High-performance async FastAPI architecture
│   ├── VJSS_DockerMaster.txt        # Production multi-stage containerization
│   └── ... (130 plain-text skills)
├── categories/                      # Organized by 6 Technical Domains (contains pure SKILL.txt)
│   ├── 01_AI_ML_DataScience/        # 14 Skills: Scikit-Learn, PyTorch, TensorFlow, NLP, RAG, Vector DB
│   ├── 02_Backend_Cloud_DevOps/     # 23 Skills: Python, Node, Rust, AWS, GCP, Azure, Docker, K8s
│   ├── 03_Frontend_Mobile_UI/       # 22 Skills: React, Next.js, Vue, Flutter, SwiftUI, Tailwind, UI/UX
│   ├── 04_Security_Quality_Testing/ # 22 Skills: OWASP, Pentesting, Encryption, E2E Cypress, Jest, K6
│   ├── 05_Trading_Fintech_Strategy/ # 12 Skills: Backtesting, Options Chain, Quant Logic, Risk Control
│   └── 06_Universal_Orchestration_Operations/ # 37 Skills: UniversalCopilot, SuperAdmin, Architect, Debugger
├── INDEX.md & INDEX.txt             # Complete alphabetized catalog
├── README.txt                       # Pure plain-text guide
└── README.md                        # Master GitHub documentation
```

---

## 📊 Complete Categorized Skills Inventory (130 Total Skills)

### 1. AI ML DataScience (14 Skills)
| Skill Name | Description | Plain-Text File |
| :--- | :--- | :--- |
| **`VJSS_AiIntegrator`** | Head of AI & LLM Engineering. Use for RAG (Retrieval-Augmented Generation) loops, vector database management, Ollama/Qwen2.5 integration, and AI signal validation logic. | [`txt_skills/VJSS_AiIntegrator.txt`](txt_skills/VJSS_AiIntegrator.txt) |
| **`VJSS_Datacleaner`** | Universal high-performance Datacleaner skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Datacleaner.txt`](txt_skills/VJSS_Datacleaner.txt) |
| **`VJSS_Geminiapidev`** | Use this skill when building applications with Gemini models, Gemini API, working with multimodal content (text, images, audio, video), implementing function calling, using structured outputs, or needing current model specifications. | [`txt_skills/VJSS_Geminiapidev.txt`](txt_skills/VJSS_Geminiapidev.txt) |
| **`VJSS_NlpSpecialist`** | Universal high-performance NlpSpecialist skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_NlpSpecialist.txt`](txt_skills/VJSS_NlpSpecialist.txt) |
| **`VJSS_Ollamalocalexpert`** | Universal high-performance Ollamalocalexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Ollamalocalexpert.txt`](txt_skills/VJSS_Ollamalocalexpert.txt) |
| **`VJSS_Pandasdatawizard`** | Universal high-performance Pandasdatawizard skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Pandasdatawizard.txt`](txt_skills/VJSS_Pandasdatawizard.txt) |
| **`VJSS_Promptengineer`** | Universal high-performance Promptengineer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Promptengineer.txt`](txt_skills/VJSS_Promptengineer.txt) |
| **`VJSS_Pytorchdev`** | Universal high-performance Pytorchdev skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Pytorchdev.txt`](txt_skills/VJSS_Pytorchdev.txt) |
| **`VJSS_Ragarchitect`** | Universal high-performance Ragarchitect skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Ragarchitect.txt`](txt_skills/VJSS_Ragarchitect.txt) |
| **`VJSS_Scikitlearnexpert`** | Expert AI data science and machine learning engineer using scikit-learn. Token-optimized logic. | [`txt_skills/VJSS_Scikitlearnexpert.txt`](txt_skills/VJSS_Scikitlearnexpert.txt) |
| **`VJSS_Superdata`** | Universal data analysis, transformation, and insight generation. Use when working with CSV, JSON, SQL, or large datasets to normalize schemas or extract business intelligence. | [`txt_skills/VJSS_Superdata.txt`](txt_skills/VJSS_Superdata.txt) |
| **`VJSS_Superintelligent`** | The ultimate auto-fixing, self-improving universal agent skill. Ensures all skills load perfectly into Gemini CLI and Claude Code. Never compromises existing features, always adds new ones, and guarantees 1000-line compliance. | [`txt_skills/VJSS_Superintelligent.txt`](txt_skills/VJSS_Superintelligent.txt) |
| **`VJSS_Tensorflowpro`** | Universal high-performance Tensorflowpro skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Tensorflowpro.txt`](txt_skills/VJSS_Tensorflowpro.txt) |
| **`VJSS_VectorDbAdmin`** | Universal high-performance VectorDbAdmin skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_VectorDbAdmin.txt`](txt_skills/VJSS_VectorDbAdmin.txt) |

### 2. Backend Cloud DevOps (23 Skills)
| Skill Name | Description | Plain-Text File |
| :--- | :--- | :--- |
| **`VJSS_Ansibleexpert`** | Universal high-performance Ansibleexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Ansibleexpert.txt`](txt_skills/VJSS_Ansibleexpert.txt) |
| **`VJSS_Awsarchitect`** | Universal high-performance Awsarchitect skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Awsarchitect.txt`](txt_skills/VJSS_Awsarchitect.txt) |
| **`VJSS_Azurearchitect`** | Universal high-performance Azurearchitect skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Azurearchitect.txt`](txt_skills/VJSS_Azurearchitect.txt) |
| **`VJSS_CiCdPipelineBuilder`** | Universal high-performance CiCdPipelineBuilder skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_CiCdPipelineBuilder.txt`](txt_skills/VJSS_CiCdPipelineBuilder.txt) |
| **`VJSS_CompressionWiz`** | Universal high-performance CompressionWiz skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_CompressionWiz.txt`](txt_skills/VJSS_CompressionWiz.txt) |
| **`VJSS_Djangoexpert`** | Universal high-performance Djangoexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Djangoexpert.txt`](txt_skills/VJSS_Djangoexpert.txt) |
| **`VJSS_Dockermaster`** | Universal high-performance Dockermaster skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Dockermaster.txt`](txt_skills/VJSS_Dockermaster.txt) |
| **`VJSS_FintechDevops`** | Head of Core Infrastructure & DBRE. Use for MariaDB/Redis management, Linux server optimization and performance tuning, background service (PM2/Systemd) configuration, and network security. | [`txt_skills/VJSS_FintechDevops.txt`](txt_skills/VJSS_FintechDevops.txt) |
| **`VJSS_GcpPro`** | Universal high-performance GcpPro skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_GcpPro.txt`](txt_skills/VJSS_GcpPro.txt) |
| **`VJSS_Graphqlmaster`** | Universal high-performance Graphqlmaster skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Graphqlmaster.txt`](txt_skills/VJSS_Graphqlmaster.txt) |
| **`VJSS_Grpcexpert`** | Universal high-performance Grpcexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Grpcexpert.txt`](txt_skills/VJSS_Grpcexpert.txt) |
| **`VJSS_IamPolicyExpert`** | Universal high-performance IamPolicyExpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_IamPolicyExpert.txt`](txt_skills/VJSS_IamPolicyExpert.txt) |
| **`VJSS_K8SAdmin`** | Universal high-performance K8SAdmin skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_K8SAdmin.txt`](txt_skills/VJSS_K8SAdmin.txt) |
| **`VJSS_Microserviceswiz`** | Universal high-performance Microserviceswiz skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Microserviceswiz.txt`](txt_skills/VJSS_Microserviceswiz.txt) |
| **`VJSS_Nginxmaster`** | Universal high-performance Nginxmaster skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Nginxmaster.txt`](txt_skills/VJSS_Nginxmaster.txt) |
| **`VJSS_Nodearchitect`** | Universal high-performance Nodearchitect skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Nodearchitect.txt`](txt_skills/VJSS_Nodearchitect.txt) |
| **`VJSS_Postgrespro`** | Universal high-performance Postgrespro skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Postgrespro.txt`](txt_skills/VJSS_Postgrespro.txt) |
| **`VJSS_Pythonfastapi`** | Universal high-performance Pythonfastapi skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Pythonfastapi.txt`](txt_skills/VJSS_Pythonfastapi.txt) |
| **`VJSS_Redisspecialist`** | Universal high-performance Redisspecialist skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Redisspecialist.txt`](txt_skills/VJSS_Redisspecialist.txt) |
| **`VJSS_Rustbackend`** | Universal high-performance Rustbackend skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Rustbackend.txt`](txt_skills/VJSS_Rustbackend.txt) |
| **`VJSS_Serverlesswiz`** | Universal high-performance Serverlesswiz skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Serverlesswiz.txt`](txt_skills/VJSS_Serverlesswiz.txt) |
| **`VJSS_Superdevops`** | Universal Git, CI/CD, and deployment automation. Use for branch management, conventional commits, and automated infrastructure workflows. | [`txt_skills/VJSS_Superdevops.txt`](txt_skills/VJSS_Superdevops.txt) |
| **`VJSS_Terraformexpert`** | Universal high-performance Terraformexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Terraformexpert.txt`](txt_skills/VJSS_Terraformexpert.txt) |

### 3. Frontend Mobile UI (22 Skills)
| Skill Name | Description | Plain-Text File |
| :--- | :--- | :--- |
| **`VJSS_A11yAuditor`** | Universal high-performance A11yAuditor skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_A11yAuditor.txt`](txt_skills/VJSS_A11yAuditor.txt) |
| **`VJSS_Androidkotlin`** | Universal high-performance Androidkotlin skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Androidkotlin.txt`](txt_skills/VJSS_Androidkotlin.txt) |
| **`VJSS_Angulararchitect`** | Universal high-performance Angulararchitect skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Angulararchitect.txt`](txt_skills/VJSS_Angulararchitect.txt) |
| **`VJSS_Animationspecialist`** | Universal high-performance Animationspecialist skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Animationspecialist.txt`](txt_skills/VJSS_Animationspecialist.txt) |
| **`VJSS_Cssgridpro`** | Universal high-performance Cssgridpro skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Cssgridpro.txt`](txt_skills/VJSS_Cssgridpro.txt) |
| **`VJSS_D3visualizer`** | Universal high-performance D3visualizer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_D3visualizer.txt`](txt_skills/VJSS_D3visualizer.txt) |
| **`VJSS_Expoexpert`** | Universal high-performance Expoexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Expoexpert.txt`](txt_skills/VJSS_Expoexpert.txt) |
| **`VJSS_Flutterdev`** | Universal high-performance Flutterdev skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Flutterdev.txt`](txt_skills/VJSS_Flutterdev.txt) |
| **`VJSS_Frontenddesign`** | Create distinctive, production-grade frontend interfaces for the Enterprise Engineering Applications. Use when building web components, pages, or trading dashboards. Generates creative, polished code that avoids generic AI aesthetics while adhering to Enterprise Engineering Applications's native HTML/JS architecture. | [`txt_skills/VJSS_Frontenddesign.txt`](txt_skills/VJSS_Frontenddesign.txt) |
| **`VJSS_Ionicpro`** | Universal high-performance Ionicpro skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Ionicpro.txt`](txt_skills/VJSS_Ionicpro.txt) |
| **`VJSS_IosSwiftUi`** | Universal high-performance IosSwiftUi skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_IosSwiftUi.txt`](txt_skills/VJSS_IosSwiftUi.txt) |
| **`VJSS_Nextjspro`** | Universal high-performance Nextjspro skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Nextjspro.txt`](txt_skills/VJSS_Nextjspro.txt) |
| **`VJSS_PwaBuilder`** | Universal high-performance PwaBuilder skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_PwaBuilder.txt`](txt_skills/VJSS_PwaBuilder.txt) |
| **`VJSS_Reactexpert`** | Universal high-performance Reactexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Reactexpert.txt`](txt_skills/VJSS_Reactexpert.txt) |
| **`VJSS_Reactnativeexpert`** | Universal high-performance Reactnativeexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Reactnativeexpert.txt`](txt_skills/VJSS_Reactnativeexpert.txt) |
| **`VJSS_Superfrontend`** | Create distinctive, production-grade frontend interfaces. Use when building UI components, dashboards, or web applications with a focus on bold aesthetics and creative design. | [`txt_skills/VJSS_Superfrontend.txt`](txt_skills/VJSS_Superfrontend.txt) |
| **`VJSS_Tailwindmaster`** | Universal high-performance Tailwindmaster skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Tailwindmaster.txt`](txt_skills/VJSS_Tailwindmaster.txt) |
| **`VJSS_Uiperfectionist`** | Expert UI/UX auditing and cross-device testing. Use this skill to identify visual inconsistencies, broken layouts, accessibility issues, and interaction bugs in web applications. | [`txt_skills/VJSS_Uiperfectionist.txt`](txt_skills/VJSS_Uiperfectionist.txt) |
| **`VJSS_Unitymobile`** | Universal high-performance Unitymobile skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Unitymobile.txt`](txt_skills/VJSS_Unitymobile.txt) |
| **`VJSS_Vuespecialist`** | Universal high-performance Vuespecialist skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Vuespecialist.txt`](txt_skills/VJSS_Vuespecialist.txt) |
| **`VJSS_WealthUiEngineer`** | Head of Wealth Executive UI & Client Portals. Use for Telegram bot message formatting, Enterprise Engineering Applications frontend (HTML/CSS/JS) development, and responsive UI/UX perfection. | [`txt_skills/VJSS_WealthUiEngineer.txt`](txt_skills/VJSS_WealthUiEngineer.txt) |
| **`VJSS_WebglWizard`** | Universal high-performance WebglWizard skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_WebglWizard.txt`](txt_skills/VJSS_WebglWizard.txt) |

### 4. Security Quality Testing (22 Skills)
| Skill Name | Description | Plain-Text File |
| :--- | :--- | :--- |
| **`VJSS_Apitester`** | Universal high-performance Apitester skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Apitester.txt`](txt_skills/VJSS_Apitester.txt) |
| **`VJSS_BrowserstackPro`** | Universal high-performance BrowserstackPro skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_BrowserstackPro.txt`](txt_skills/VJSS_BrowserstackPro.txt) |
| **`VJSS_Browsertester`** | Advanced headless browser testing and UI/UX validation engine. Capable of simulating user behavior, checking for visual regressions, and auditing DOM integrity. | [`txt_skills/VJSS_Browsertester.txt`](txt_skills/VJSS_Browsertester.txt) |
| **`VJSS_Chaosmonkey`** | Universal high-performance Chaosmonkey skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Chaosmonkey.txt`](txt_skills/VJSS_Chaosmonkey.txt) |
| **`VJSS_Compliancechecker`** | Universal high-performance Compliancechecker skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Compliancechecker.txt`](txt_skills/VJSS_Compliancechecker.txt) |
| **`VJSS_Coverageoptimizer`** | Universal high-performance Coverageoptimizer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Coverageoptimizer.txt`](txt_skills/VJSS_Coverageoptimizer.txt) |
| **`VJSS_E2ECypress`** | Universal high-performance E2ECypress skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_E2ECypress.txt`](txt_skills/VJSS_E2ECypress.txt) |
| **`VJSS_Encryptionexpert`** | Universal high-performance Encryptionexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Encryptionexpert.txt`](txt_skills/VJSS_Encryptionexpert.txt) |
| **`VJSS_Firewallwiz`** | Universal high-performance Firewallwiz skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Firewallwiz.txt`](txt_skills/VJSS_Firewallwiz.txt) |
| **`VJSS_LoadTesterK6`** | Universal high-performance LoadTesterK6 skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_LoadTesterK6.txt`](txt_skills/VJSS_LoadTesterK6.txt) |
| **`VJSS_Mobilesecurity`** | Universal high-performance Mobilesecurity skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Mobilesecurity.txt`](txt_skills/VJSS_Mobilesecurity.txt) |
| **`VJSS_Mutationtesting`** | Universal high-performance Mutationtesting skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Mutationtesting.txt`](txt_skills/VJSS_Mutationtesting.txt) |
| **`VJSS_OwaspValidator`** | Universal high-performance OwaspValidator skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_OwaspValidator.txt`](txt_skills/VJSS_OwaspValidator.txt) |
| **`VJSS_Pentestbot`** | Universal high-performance Pentestbot skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Pentestbot.txt`](txt_skills/VJSS_Pentestbot.txt) |
| **`VJSS_Perfanalyzer`** | Universal high-performance Perfanalyzer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Perfanalyzer.txt`](txt_skills/VJSS_Perfanalyzer.txt) |
| **`VJSS_Piiscanner`** | Universal high-performance Piiscanner skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Piiscanner.txt`](txt_skills/VJSS_Piiscanner.txt) |
| **`VJSS_RiskAuditor`** | Head of Quality Assurance & Risk Management. Use for capital protection auditing, code reviews, signal veto verification, and enforcing portfolio drawdown limits and risk management guardrails. | [`txt_skills/VJSS_RiskAuditor.txt`](txt_skills/VJSS_RiskAuditor.txt) |
| **`VJSS_Securityguidance`** | Proactive security guidance for Enterprise Engineering Applications. Use whenever editing or writing code to identify common security pitfalls like command injection, XSS, insecure deserialization, and credential leaks. | [`txt_skills/VJSS_Securityguidance.txt`](txt_skills/VJSS_Securityguidance.txt) |
| **`VJSS_Supersecurity`** | Global security auditing and threat modeling. Use to identify vulnerabilities, harden systems, and ensure PII/SPI protection across any project. | [`txt_skills/VJSS_Supersecurity.txt`](txt_skills/VJSS_Supersecurity.txt) |
| **`VJSS_Threatmodeler`** | Universal high-performance Threatmodeler skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Threatmodeler.txt`](txt_skills/VJSS_Threatmodeler.txt) |
| **`VJSS_Unittestjest`** | Universal high-performance Unittestjest skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Unittestjest.txt`](txt_skills/VJSS_Unittestjest.txt) |
| **`VJSS_Visualregression`** | Universal high-performance Visualregression skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Visualregression.txt`](txt_skills/VJSS_Visualregression.txt) |

### 5. Trading Fintech Strategy (12 Skills)
| Skill Name | Description | Plain-Text File |
| :--- | :--- | :--- |
| **`VJSS_Algobacktester`** | Universal high-performance Algobacktester skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Algobacktester.txt`](txt_skills/VJSS_Algobacktester.txt) |
| **`VJSS_Cryptoauditor`** | Universal high-performance Cryptoauditor skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Cryptoauditor.txt`](txt_skills/VJSS_Cryptoauditor.txt) |
| **`VJSS_Cryptotracker`** | Universal high-performance Cryptotracker skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Cryptotracker.txt`](txt_skills/VJSS_Cryptotracker.txt) |
| **`VJSS_Demathistorian`** | Universal high-performance Demathistorian skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Demathistorian.txt`](txt_skills/VJSS_Demathistorian.txt) |
| **`VJSS_Dividendtracker`** | Universal high-performance Dividendtracker skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Dividendtracker.txt`](txt_skills/VJSS_Dividendtracker.txt) |
| **`VJSS_Forexexpert`** | Universal high-performance Forexexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Forexexpert.txt`](txt_skills/VJSS_Forexexpert.txt) |
| **`VJSS_Insidertradingmonitor`** | Universal high-performance Insidertradingmonitor skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Insidertradingmonitor.txt`](txt_skills/VJSS_Insidertradingmonitor.txt) |
| **`VJSS_Optionschainanalyzer`** | Advanced options chain intelligence for NIFTY, BANKNIFTY, and FINNIFTY. Provides real-time strike suggestion, Greek analysis, and automated execution logic. | [`txt_skills/VJSS_Optionschainanalyzer.txt`](txt_skills/VJSS_Optionschainanalyzer.txt) |
| **`VJSS_Portfoliooptimizer`** | Universal high-performance Portfoliooptimizer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Portfoliooptimizer.txt`](txt_skills/VJSS_Portfoliooptimizer.txt) |
| **`VJSS_QuantArchitect`** | Head of Quantitative Strategy & Alpha Labs. Use for algorithmic trading logic, strategy refactoring, backtesting analysis, and mathematical modeling for quantitative finance models and automated execution engines. | [`txt_skills/VJSS_QuantArchitect.txt`](txt_skills/VJSS_QuantArchitect.txt) |
| **`VJSS_Riskmanagementbot`** | Universal high-performance Riskmanagementbot skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Riskmanagementbot.txt`](txt_skills/VJSS_Riskmanagementbot.txt) |
| **`VJSS_Taxoptimizer`** | Universal high-performance Taxoptimizer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Taxoptimizer.txt`](txt_skills/VJSS_Taxoptimizer.txt) |

### 6. Universal Orchestration Operations (37 Skills)
| Skill Name | Description | Plain-Text File |
| :--- | :--- | :--- |
| **`VJSS_Asttransformer`** | Universal high-performance Asttransformer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Asttransformer.txt`](txt_skills/VJSS_Asttransformer.txt) |
| **`VJSS_Authsystembuilder`** | Universal high-performance Authsystembuilder skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Authsystembuilder.txt`](txt_skills/VJSS_Authsystembuilder.txt) |
| **`VJSS_Calendaroptimizer`** | Universal high-performance Calendaroptimizer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Calendaroptimizer.txt`](txt_skills/VJSS_Calendaroptimizer.txt) |
| **`VJSS_Codereview`** | High-signal code review for Enterprise Engineering Applications. Use to audit pull requests or file changes for bugs, logic errors, and adherence to project conventions (project conventions and architecture guidelines). Focuses on correctness, security, and architectural integrity. | [`txt_skills/VJSS_Codereview.txt`](txt_skills/VJSS_Codereview.txt) |
| **`VJSS_Deeplinkingwiz`** | Universal high-performance Deeplinkingwiz skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Deeplinkingwiz.txt`](txt_skills/VJSS_Deeplinkingwiz.txt) |
| **`VJSS_Dependencymanager`** | Universal high-performance Dependencymanager skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Dependencymanager.txt`](txt_skills/VJSS_Dependencymanager.txt) |
| **`VJSS_DocsGenerator`** | Universal high-performance DocsGenerator skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_DocsGenerator.txt`](txt_skills/VJSS_DocsGenerator.txt) |
| **`VJSS_Emailtriage`** | Universal high-performance Emailtriage skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Emailtriage.txt`](txt_skills/VJSS_Emailtriage.txt) |
| **`VJSS_Featuredev`** | Guided feature development workflow for Enterprise Engineering Applications. Use when adding new components, broker integrations, or backend services. Follows a systematic 7-phase approach: Discovery, Exploration, Questions, Architecture, Implementation, Quality Review, and Summary. | [`txt_skills/VJSS_Featuredev.txt`](txt_skills/VJSS_Featuredev.txt) |
| **`VJSS_Gitmaster`** | Universal high-performance Gitmaster skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Gitmaster.txt`](txt_skills/VJSS_Gitmaster.txt) |
| **`VJSS_Gitworkflow`** | Automated and structured Git workflow for Enterprise Engineering Applications. Use to generate conventional commit messages, push changes, and create pull requests using the GitHub CLI (gh). | [`txt_skills/VJSS_Gitworkflow.txt`](txt_skills/VJSS_Gitworkflow.txt) |
| **`VJSS_GoogleWorkspacePro`** | Universal high-performance GoogleWorkspacePro skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_GoogleWorkspacePro.txt`](txt_skills/VJSS_GoogleWorkspacePro.txt) |
| **`VJSS_DistributedPlatformCommander`** | Autonomous orchestrator for the DistributedEnterprisePlatform DistributedPlatformCluster. Manages Postgres/Redis synchronization, Gemini-First AI failover, and hardware-pinned task execution (Super-Threading). Use when migrating projects, deploying new features across core groups, or validating the 100% Stability Protocol. | [`txt_skills/VJSS_DistributedPlatformCommander.txt`](txt_skills/VJSS_DistributedPlatformCommander.txt) |
| **`VJSS_Jiramanager`** | Universal high-performance Jiramanager skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Jiramanager.txt`](txt_skills/VJSS_Jiramanager.txt) |
| **`VJSS_Jsontransformer`** | Universal high-performance Jsontransformer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Jsontransformer.txt`](txt_skills/VJSS_Jsontransformer.txt) |
| **`VJSS_Knowledgebasewiz`** | Universal high-performance Knowledgebasewiz skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Knowledgebasewiz.txt`](txt_skills/VJSS_Knowledgebasewiz.txt) |
| **`VJSS_Loganalyzer`** | Universal high-performance Loganalyzer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Loganalyzer.txt`](txt_skills/VJSS_Loganalyzer.txt) |
| **`VJSS_Meetingsummarizer`** | Universal high-performance Meetingsummarizer skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Meetingsummarizer.txt`](txt_skills/VJSS_Meetingsummarizer.txt) |
| **`VJSS_Notionarchitect`** | Universal high-performance Notionarchitect skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Notionarchitect.txt`](txt_skills/VJSS_Notionarchitect.txt) |
| **`VJSS_Regexmaster`** | Universal high-performance Regexmaster skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Regexmaster.txt`](txt_skills/VJSS_Regexmaster.txt) |
| **`VJSS_Shellexpert`** | Universal high-performance Shellexpert skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Shellexpert.txt`](txt_skills/VJSS_Shellexpert.txt) |
| **`VJSS_Slackbotbuilder`** | Universal high-performance Slackbotbuilder skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Slackbotbuilder.txt`](txt_skills/VJSS_Slackbotbuilder.txt) |
| **`VJSS_Smartcontext`** | Universal high-performance Smartcontext skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Smartcontext.txt`](txt_skills/VJSS_Smartcontext.txt) |
| **`VJSS_StrategicOverseer`** | Head of Strategic Operations. Use for global mandate enforcement, ecosystem-wide architectural changes, and managing the standard Git commit and release lifecycle GitHub lifecycle. | [`txt_skills/VJSS_StrategicOverseer.txt`](txt_skills/VJSS_StrategicOverseer.txt) |
| **`VJSS_SuperVJBrain`** | The ultimate Master Orchestrator for the VJSuperSkills ecosystem. Features autonomous skill discovery, token-optimized planning, and a 30-second delayed startup heartbeat. | [`txt_skills/VJSS_SuperVJBrain.txt`](txt_skills/VJSS_SuperVJBrain.txt) |
| **`VJSS_Superadmin`** | Universal SysAdmin, automation, and project management. Use for task orchestration, health monitoring, environment setup, and general project administration. | [`txt_skills/VJSS_Superadmin.txt`](txt_skills/VJSS_Superadmin.txt) |
| **`VJSS_Superarchitect`** | Global system design and codebase mapping. Use when starting new projects, refactoring legacy systems, or understanding complex cross-component dependencies in any AI agent environment. | [`txt_skills/VJSS_Superarchitect.txt`](txt_skills/VJSS_Superarchitect.txt) |
| **`VJSS_Superbuilder`** | Universal 7-phase feature development workflow. Ensures thorough discovery, architecture design, and quality-controlled implementation for any software feature. | [`txt_skills/VJSS_Superbuilder.txt`](txt_skills/VJSS_Superbuilder.txt) |
| **`VJSS_Superdebugger`** | Deep root cause analysis and issue resolution. Use when investigating bugs, crashes, or unintended behavior in any software system. | [`txt_skills/VJSS_Superdebugger.txt`](txt_skills/VJSS_Superdebugger.txt) |
| **`VJSS_Superdocs`** | Universal technical writing and documentation. Use when creating API references, READMEs, architectural overviews, or project-specific SOPs. | [`txt_skills/VJSS_Superdocs.txt`](txt_skills/VJSS_Superdocs.txt) |
| **`VJSS_Superhealing`** | Autonomous error resolution engine. Automatically diagnoses failures, fetches documentation, and chains other skills to apply fixes without user intervention. | [`txt_skills/VJSS_Superhealing.txt`](txt_skills/VJSS_Superhealing.txt) |
| **`VJSS_Superparallel`** | Multi-threaded execution engine for batch processing. Use this to run multiple shell commands or file analyses simultaneously across available CPU cores. | [`txt_skills/VJSS_Superparallel.txt`](txt_skills/VJSS_Superparallel.txt) |
| **`VJSS_Superpower`** | Universal high-performance Superpower skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Superpower.txt`](txt_skills/VJSS_Superpower.txt) |
| **`VJSS_Superpowersplugin`** | A structured workflow plugin that enforces explore -> plan -> code. Matches Anthropic's best-practice advice but automated. Contains 14 workflow and orchestration skills. | [`txt_skills/VJSS_Superpowersplugin.txt`](txt_skills/VJSS_Superpowersplugin.txt) |
| **`VJSS_Superreviewer`** | Professional-grade automated code review. Use to audit changes for bugs, security leaks, and architectural integrity. Focuses on high-signal feedback and automated validation. | [`txt_skills/VJSS_Superreviewer.txt`](txt_skills/VJSS_Superreviewer.txt) |
| **`VJSS_Taskautomator`** | Universal high-performance Taskautomator skill for autonomous AI agents and pair-programming assistants. | [`txt_skills/VJSS_Taskautomator.txt`](txt_skills/VJSS_Taskautomator.txt) |
| **`VJSS_UniversalCopilot`** ⭐ **[MASTER GATEWAY]** | Master Personal AI Assistant & Skill Orchestrator. Analyzes & refines user intent, dynamically routes 130+ VJSS skills, minimizes token consumption, remembers conversational history, provides proactive recommendations, and guides setup across all AI tools. | [`txt_skills/VJSS_UniversalCopilot.txt`](txt_skills/VJSS_UniversalCopilot.txt) |

---


## 🤝 Community Contributions & Creator Protection

We welcome community contributions! Please read our [**CONTRIBUTING.md**](CONTRIBUTING.md) to understand our **7-Pillar Fool-Proof Quality Standard** and **Creator & Contributor Attribution Guidelines**.

All Pull Requests are automatically validated by our [**GitHub Actions CI Benchmark Suite**](.github/workflows/benchmark.yml).

## 👤 Creator & Lead Architect

| Field | Information |
| :--- | :--- |
| **Creator & Author** | **Mr. Vishalkumar Joshi** |
| **Official Website** | [https://vjprojects.co.in](https://vjprojects.co.in) |
| **GitHub Profile** | [@mrvishaljjoshi-cmyk](https://github.com/mrvishaljjoshi-cmyk) |
| **Official Email** | [mrvishaljjoshi@gmail.com](mailto:mrvishaljjoshi@gmail.com) |
| **Project Repository** | [https://github.com/mrvishaljjoshi-cmyk/VJSS](https://github.com/mrvishaljjoshi-cmyk/VJSS) |

---

## 🏷️ Viral AI Topics & Search Keywords

`#AIAgents` `#ClaudeCode` `#CursorRules` `#WindsurfRules` `#PromptEngineering` `#AICoding` `#AutonomousAgents` `#LLM` `#CursorAI` `#DevTools` `#AwesomePrompts` `#Antigravity` `#VJSS` `#PairProgramming` `#AgenticWorkflow` `#GitHubCopilot` `#RooCode` `#Cline` `#FastAPI` `#Docker` `#Kubernetes` `#React` `#NextJS` `#Fintech` `#AlgoTrading` `#CyberSecurity` `#OWASP` `#VishalkumarJoshi` `#VJProjects`

**Search Index:** AI Agent Skills, Claude Code Prompts, Cursor IDE System Rules, Windsurf Cascade Rules, Roo Code Custom Instructions, Cline Agent Protocols, Antigravity CLI Skills, Gemini CLI Prompts, Enterprise Python FastAPI Architecture, Zero-Bill Cloud Architecture, Dynamic ATR Rally-Riding Strategy, Full-Stack AI Developer Skills, Best AI Prompt Library 2026.

---

### 🌟 Enjoying VJSS? Support the Project!
If this ecosystem helped you build faster with zero errors, please support the creator **Mr. Vishalkumar Joshi**:
👉 **[⭐ Star VJSS on GitHub](https://github.com/mrvishaljjoshi-cmyk/VJSS)** — *Help more developers discover universal agent skills!*  
🌐 **[Visit Official Website (vjprojects.co.in)](https://vjprojects.co.in)** | 💬 **[Leave a Review or Suggest a Skill](https://github.com/mrvishaljjoshi-cmyk/VJSS/discussions)**

---
*Created with ❤️ by **Mr. Vishalkumar Joshi** for autonomous AI agents and modern software developers worldwide.*
