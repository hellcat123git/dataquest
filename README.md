# 🧠 HackathonOS

> **The AI-Powered Workspace Operating System for DataQuest 3.0**
> Clone once. Fill in the context. Let the agents do the rest.

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?logo=streamlit)](https://streamlit.io)
[![Gemini](https://img.shields.io/badge/Gemini_API-ready-green?logo=google)](https://aistudio.google.com)
[![MCP](https://img.shields.io/badge/MCP_Servers-8_configured-purple)](./mcp/)
[![Agents](https://img.shields.io/badge/AI_Agents-8_roles-orange)](./agents/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 🚀 What Is HackathonOS?

HackathonOS is not just a project template. It is a **multi-agent AI workspace** that lets your team of 6 operate like a 60-person company — each person paired with a specialized AI agent that knows exactly what to do.

Instead of everyone writing random code, you have:
- **8 specialized AI agents** with role-specific instructions
- **8 MCP servers** that give AI tools real-world senses (web search, file access, SQL, GitHub)
- **A complete Streamlit data dashboard** ready to accept any CSV
- **Design system** with dark theme, color tokens, chart factories, and branded exports
- **One-command setup** via `python setup.py`

---

## 🗂️ Repository Structure

```
hackathon-os/
│
├── 📂 .hackathon/           ← TEAM FILLS THIS AT 9 AM (shared brain)
│   ├── CONTEXT.md           ← Problem statement, solution, dataset info
│   ├── TEAM.md              ← Member names & roles
│   └── DECISIONS.md         ← Architecture decision log
│
├── 📂 agents/               ← AI Agent instruction files (SKILL.md)
│   ├── orchestrator/        ← Product direction, scope, PPT generation
│   ├── data-analyst/        ← CSV cleaning and data pipeline
│   ├── dataset-hunter/      ← Kaggle/data discovery (NEW)
│   ├── dashboard-engineer/  ← Streamlit UI and charts
│   ├── graphic-designer/    ← CSS, design tokens, visual exports (NEW)
│   ├── ai-integrator/       ← Gemini API and ML models
│   ├── devops/              ← Git, README, submission
│   └── pitch-lead/          ← PPT, pitch script, business model
│
├── 📂 mcp/                  ← 8 MCP server configurations
│   ├── mcp_config.json      ← Master config (load into Claude/Cursor)
│   └── README.md            ← Setup instructions + API key sources
│
├── 📂 src/                  ← Streamlit application source code
│   ├── app.py               ← Main entry point
│   ├── config.py            ← Environment variables
│   ├── pages/               ← 4 dashboard pages
│   │   ├── 01_overview.py   ← KPIs, primary chart, data table
│   │   ├── 02_analysis.py   ← Correlation, scatter, distributions
│   │   ├── 03_predictions.py← ML linear regression forecasting
│   │   └── 04_ai_insights.py← Gemini API Q&A and summaries
│   ├── components/          ← Reusable UI components
│   │   ├── visuals.py       ← Chart factories, design tokens, PIL banner
│   │   ├── metric_cards.py  ← KPI metric card component
│   │   ├── lottie_loader.py ← Animated Lottie graphics
│   │   └── style.css        ← Full dark theme CSS
│   ├── integrations/        ← External API connectors
│   │   ├── gemini_client.py ← Google Gemini API integration
│   │   ├── openai_client.py ← OpenAI API integration
│   │   ├── simple_ml.py     ← Scikit-learn linear regression
│   │   └── huggingface_client.py
│   └── data_pipeline/       ← Data loading and cleaning
│
├── 📂 data/
│   ├── raw/                 ← Drop Kaggle CSVs here
│   └── clean/               ← Cleaned outputs land here
│
├── 📂 docs/                 ← Documentation and screenshots
├── 📂 assets/               ← Generated banners and images
│
├── setup.py                 ← ONE-COMMAND SETUP
├── requirements.txt         ← All Python dependencies
└── .env.example             ← API key template
```

---

## ⚡ Quickstart (5 Minutes)

### 1. Clone
```bash
git clone https://github.com/hellcat123git/dataquest.git
cd dataquest
```

### 2. Bootstrap Everything
```bash
python setup.py
```
This creates a virtual environment, installs all dependencies, and copies `.env.example` → `.env`.

### 3. Add API Keys
Open `.env` and fill in at minimum:
```env
GEMINI_API_KEY=your_key_here   # Get free at aistudio.google.com
PROJECT_NAME=Your Project Name
TEAM_NAME=Your Team Name
```

### 4. Launch the App
```bash
# Activate venv first:
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

streamlit run src/app.py
```

### 5. Upload Any CSV and Start Exploring!

---

## 🤖 The 8 AI Agents

Each agent has a `SKILL.md` file that tells your AI tool (Claude, Cursor, ChatGPT) exactly who it is, what to do, and what constraints to follow.

**How to use an agent:** Open the `SKILL.md` file in your AI tool and say *"Read and follow the instructions in this file."*

| Agent | SKILL.md Location | Responsibility |
|-------|-------------------|----------------|
| 🎯 Orchestrator | `agents/orchestrator/SKILL.md` | Project direction, scope control, PPT |
| 🔍 Dataset Hunter | `agents/dataset-hunter/SKILL.md` | Kaggle search, data discovery |
| 🧹 Data Analyst | `agents/data-analyst/SKILL.md` | CSV cleaning, profiling, pipeline |
| 🎨 Graphic Designer | `agents/graphic-designer/SKILL.md` | CSS, charts, visual identity |
| 📊 Dashboard Engineer | `agents/dashboard-engineer/SKILL.md` | Streamlit UI, Plotly charts |
| 🤖 AI Integrator | `agents/ai-integrator/SKILL.md` | Gemini API, ML models |
| 🛠️ DevOps | `agents/devops/SKILL.md` | Git, README, submission |
| 🎤 Pitch Lead | `agents/pitch-lead/SKILL.md` | PPT, pitch script, business model |

---

## 🔌 MCP Servers

Load `mcp/mcp_config.json` into **Claude Desktop** or **Cursor** to activate 8 servers:

| Server | What It Enables |
|--------|----------------|
| 🌐 Brave Search | AI can search the live web for datasets and stats |
| 📄 Fetch | AI can read any webpage as clean text |
| 🗄️ SQLite | AI can run SQL on your local database |
| 🐙 GitHub | AI can find existing solutions on GitHub |
| 📂 Filesystem | AI can read and write your project files |
| 🧠 Memory | AI remembers decisions across sessions |
| 🤔 Sequential Thinking | Forces AI to reason step-by-step |
| 📊 Kaggle | AI can search and download datasets directly |

See [`mcp/README.md`](./mcp/README.md) for installation instructions.

---

## 🎨 Design System

The **Graphic Designer Agent** (`agents/graphic-designer/SKILL.md`) manages the full visual identity:
- **Dark theme** with custom CSS injected via `src/components/style.css`
- **Design tokens** — consistent color palette across all charts
- **Branded chart factories** — `branded_line()`, `branded_bar()`, `branded_pie()`, etc.
- **PIL banner generator** — creates a header image for the app and GitHub README
- **Lottie animations** — pre-selected for Healthcare, Finance, and AI domains
- **Export functions** — download any chart as a high-resolution PNG

---

## 📊 Dashboard Pages

| Page | What It Shows |
|------|--------------|
| 🏠 Home (`app.py`) | Upload dataset, quick intro cards |
| 📊 Overview | KPI metrics, trend chart, category breakdown |
| 🔬 Analysis | Correlation heatmap, scatter, distributions, box plots |
| 🔮 Predictions | ML linear regression forecasting with confidence |
| 🤖 AI Insights | Gemini-powered Q&A, executive summaries, trend analysis |

---

## 🔑 API Keys Required

| Key | Where to Get | Cost |
|-----|-------------|------|
| `GEMINI_API_KEY` | [aistudio.google.com](https://aistudio.google.com) | Free |
| `KAGGLE_USERNAME` + `KAGGLE_KEY` | [kaggle.com/settings](https://www.kaggle.com/settings) | Free |
| `BRAVE_API_KEY` | [brave.com/search/api](https://brave.com/search/api/) | Free (2k/mo) |
| `GITHUB_TOKEN` | [github.com/settings/tokens](https://github.com/settings/tokens) | Free |
| `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com) | ~₹400 credit |

---

## 🏆 Built For

**DataQuest 3.0** — 24-Hour Data-Driven Hackathon
Organized by ECDS (Engagement & Collaboration Committee of Data Science)
**VIT Chennai** · Oct 7–8, 2026 · MG Auditorium

---

*HackathonOS — Trust the system. Fill the context. Let the agents build.*
