# 🧠 HackathonOS: Team Operating Guide

Welcome to HackathonOS! This repository is your 6-person team's secret weapon for DataQuest 3.0. 
It is a pre-configured, multi-agent AI workspace.

## 🚀 How This System Works

Instead of everyone coding randomly, this repo forces a highly coordinated workflow where **AI does the coding and humans do the architecture**.

### 1. The Core Setup (9:00 AM)
When the hackathon starts, open a terminal in this folder and run:
``bash
python setup.py
``
This single command will install all dependencies, create your virtual environment, and set up your .env file.

### 2. The "Brain" (Your Shared Context)
The most important folder in this repo is **.hackathon/**. 
* Open .hackathon/CONTEXT.md and fill in the secret problem statement at 9:00 AM.
* **Why?** Every AI agent you use (Cursor, Claude, etc.) will read this file. If you update the context here, all your AI tools instantly know what you are building.

### 3. The AI Agents (gents/)
We have pre-defined 6 specific AI personas. When you want an AI to write code for a specific part of the app, tell it to read its specific SKILL.md file first!
* **@Orchestrator:** Reads gents/orchestrator/SKILL.md. Keeps the team on track and prevents scope creep.
* **@Data-Analyst:** Reads gents/data-analyst/SKILL.md. Cleans CSVs and outputs them to data/clean/.
* **@Dashboard-Engineer:** Reads gents/dashboard-engineer/SKILL.md. Writes the Streamlit frontend UI in src/.
* **@AI-Integrator:** Reads gents/ai-integrator/SKILL.md. Hooks up the Google Gemini API to generate insights.
* **@DevOps:** Reads gents/devops/SKILL.md. Handles Git merges and the final 2:00 AM submission.
* **@Pitch-Lead:** Reads gents/pitch-lead/SKILL.md. Helps you write the perfect PPT and script.

### 4. The MCP Servers (Supercharging the AI)
Look in the **mcp/** folder. We have configured Model Context Protocol servers.
If you load mcp_config.json into Cursor or Claude Desktop, your AI will suddenly have the ability to:
- Browse the live internet for datasets (Brave Search)
- Run SQL queries (SQLite)
- Read other GitHub repos (GitHub)

### 5. The Application Architecture (src/)
Your actual hackathon project lives in src/.
* src/app.py is the main entry point for the Streamlit dashboard.
* Run it locally using: streamlit run src/app.py
* UI components (charts, metric cards) are separated into src/components/.
* Data analysis scripts go in src/data_pipeline/.

## 📌 Your First Action Item
1. Ask the team DevOps manager to push this repo to a private GitHub repository.
2. Have all 6 members clone the repository to their laptops.
3. Everyone must run python setup.py.
4. Everyone must paste their Gemini API key into the .env file.

Good luck. Trust the system, don't write code from scratch, and win the hackathon.
