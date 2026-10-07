# 🔌 MCP Server Setup Guide

## What Are MCP Servers?
Model Context Protocol (MCP) servers give your AI agent real-world "senses":
- 🌐 **Search the web** for live statistics and datasets
- 📂 **Read and write files** in your workspace automatically
- 🗄️ **Run SQL queries** on your database
- 🐙 **Browse GitHub** for example code
- 🧠 **Persist memory** across sessions

Without MCP, the AI only knows what you type into the chat box.
With MCP, the AI can autonomously browse, query, and write code.

---

## Configured Servers (all in `mcp_config.json`)

| Server | Purpose | Required Key |
|--------|---------|-------------|
| `brave-search` | Live web search for stats & datasets | `BRAVE_API_KEY` |
| `fetch` | Read any webpage as markdown | None |
| `sqlite` | SQL queries on local database | None |
| `github` | Search repos & read code | `GITHUB_TOKEN` |
| `filesystem` | Read/write workspace files | None |
| `memory` | Persistent key-value storage | None |
| `sequential-thinking` | Step-by-step reasoning mode | None |
| `kaggle` | Search & download datasets | `KAGGLE_USERNAME` + `KAGGLE_KEY` |

---

## Installation

### Step 1: Install uvx (one-time)
```powershell
# Windows PowerShell (run as normal user):
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
powershell -ExecutionPolicy RemoteSigned -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 2: Activate MCP in Claude Desktop
1. Open **Claude Desktop** → Settings → Developer → Edit Config
2. Copy the full contents of `mcp/mcp_config.json`
3. Paste it into the config file. Save. Restart Claude Desktop.
4. You should see 🔌 icons in the chat bar for each server.

### Step 3: Activate MCP in Cursor
1. Open Cursor → Settings → MCP Servers
2. Click "Add Server" for each entry in `mcp_config.json`

---

## Get API Keys (Free Tiers)
| Service | Link | Free Tier |
|---------|------|-----------|
| Brave Search | https://brave.com/search/api/ | 2,000 queries/month |
| Google Gemini | https://aistudio.google.com/ | Very generous |
| GitHub Token | https://github.com/settings/tokens | Free |
| Kaggle API | https://www.kaggle.com/settings → API | Free |
| OpenAI | https://platform.openai.com/ | Needs ₹400 credit |

---

## Example Usage in Claude Chat (with MCP active)
```
"Use brave-search to find a CSV dataset about hospital admissions in India.
Then use the fetch server to read the download page.
Then write a Python script using the filesystem server to load and clean it."
```

The AI will do all three steps autonomously.
