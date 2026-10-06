#!/usr/bin/env python3
"""
HackathonOS Bootstrap Script
Run: python setup.py
This will:
1. Check Python version
2. Create a virtual environment
3. Install all dependencies
4. Create .env from .env.example
5. Create data directories
6. Run a health check
"""

import sys
import subprocess
import os
import shutil

def check_python():
    if sys.version_info < (3, 10):
        print("❌ Python 3.10+ required. Please upgrade.")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected.")

def create_venv():
    if not os.path.exists("venv"):
        print("📦 Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    print("✅ Virtual environment ready.")

def install_deps():
    print("📥 Installing dependencies (this takes ~2 minutes)...")
    pip_path = "venv/Scripts/pip" if os.name == "nt" else "venv/bin/pip"
    subprocess.run([pip_path, "install", "-r", "requirements.txt", "-q"], check=True)
    print("✅ Dependencies installed.")

def setup_env():
    if not os.path.exists(".env"):
        shutil.copy(".env.example", ".env")
        print("📝 Created .env from template. PLEASE ADD YOUR API KEYS TO .env NOW.")
    else:
        print("✅ .env already exists.")

def create_dirs():
    dirs = ["data/raw", "data/clean", "docs/screenshots"]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print("✅ Data directories created.")

def health_check():
    python_path = "venv/Scripts/python" if os.name == "nt" else "venv/bin/python"
    result = subprocess.run(
        [python_path, "-c", "import streamlit, pandas, plotly; print('All OK')"],
        capture_output=True, text=True
    )
    if "All OK" in result.stdout:
        print("✅ Health check passed. Ready to hack!")
    else:
        print(f"❌ Health check failed: {result.stderr}")

if __name__ == "__main__":
    print("\n🚀 HackathonOS — Environment Bootstrap\n" + "="*40)
    check_python()
    create_venv()
    install_deps()
    setup_env()
    create_dirs()
    health_check()
    
    activate = "venv\\Scripts\\activate" if os.name == "nt" else "source venv/bin/activate"
    print(f"\n{'='*40}")
    print(f"✨ Setup complete! Next steps:")
    print(f"   1. Run: {activate}")
    print(f"   2. Edit .env with your API keys")
    print(f"   3. Fill in .hackathon/CONTEXT.md with the problem statement")
    print(f"   4. Run: streamlit run src/app.py")
    print(f"{'='*40}\n")
