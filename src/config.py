import os
from dotenv import load_dotenv

load_dotenv()

# Project Identity (update in CONTEXT.md and here after 9:30 AM)
PROJECT_NAME = os.getenv("PROJECT_NAME", "DataQuest Project")
TAGLINE = os.getenv("TAGLINE", "AI-Powered Data Analytics Dashboard")
TEAM_NAME = os.getenv("TEAM_NAME", "Team Alpha")

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Data paths
RAW_DATA_DIR = "data/raw"
CLEAN_DATA_DIR = "data/clean"

# Feature Flags (set to False if a feature isn't working, it removes it from UI cleanly)
ENABLE_AI_INSIGHTS = bool(GEMINI_API_KEY)
ENABLE_PREDICTIONS = True
ENABLE_MAP_VIEW = False   # Set True only if you have lat/lon data
