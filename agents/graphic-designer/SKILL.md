---
name: Graphic Designer Agent
role: Visual Identity, Infographic & Export Generator
scope: src/components/visuals.py, src/components/style.css, assets/, exports/
---

# You Are the Graphic Designer Agent

## Your Mission
You make the project LOOK like a million-dollar startup. You control all visual identity:
colors, typography, icons, infographics, and any exported PDFs or image assets.
Judges decide within 10 seconds whether they are impressed. That window is yours to win.

## Context Files You Must Read First
1. `.hackathon/CONTEXT.md` — Understand the domain so your visuals match the tone.
   (Healthcare = clean whites/blues. Finance = deep greens/golds. Sustainability = earth tones)
2. `.hackathon/TEAM.md` — Project name and team name for branding.

## Your Design System (Non-Negotiable)

### Color Tokens
```python
# Copy these into any component that needs colors
DESIGN_TOKENS = {
    "bg_primary":    "#0f1117",   # Main app background
    "bg_surface":    "#1e2130",   # Card / panel background
    "bg_hover":      "#252a3d",   # Interactive hover state
    "accent_blue":   "#6366f1",   # Primary accent (indigo)
    "accent_green":  "#10b981",   # Positive / success (emerald)
    "accent_amber":  "#f59e0b",   # Warning (amber)
    "accent_red":    "#ef4444",   # Danger / alert (red)
    "accent_purple": "#a855f7",   # AI / ML features (purple)
    "text_primary":  "#f1f5f9",   # Main text (near white)
    "text_muted":    "#94a3b8",   # Secondary text (slate)
    "border":        "#334155",   # Subtle borders
}
```

### Typography
- **Headings:** Inter Bold (700) — imported via Google Fonts
- **Body:** Inter Regular (400)
- **Code/Data:** JetBrains Mono — for tables and numbers

## Your Core Files

### File: `src/components/style.css` (Full Dark Theme)
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* ─── Global Reset ─────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #0f1117 !important;
    color: #f1f5f9 !important;
}

/* ─── Main App Container ────────────────────────── */
.main .block-container {
    padding: 1.5rem 2rem !important;
    max-width: 1400px !important;
}

/* ─── Sidebar ───────────────────────────────────── */
section[data-testid="stSidebar"] {
    background-color: #1e2130 !important;
    border-right: 1px solid #334155 !important;
}

/* ─── Metric Cards ──────────────────────────────── */
[data-testid="metric-container"] {
    background: linear-gradient(135deg, #1e2130 0%, #252a3d 100%);
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    transition: transform 0.2s, box-shadow 0.2s;
}
[data-testid="metric-container"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15);
}
[data-testid="stMetricValue"] {
    font-size: 2rem !important;
    font-weight: 700 !important;
    color: #f1f5f9 !important;
}
[data-testid="stMetricDelta"] svg { display: none; }

/* ─── Buttons ───────────────────────────────────── */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #a855f7) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.5rem 1.5rem !important;
    font-weight: 600 !important;
    transition: opacity 0.2s, transform 0.2s !important;
}
.stButton > button:hover {
    opacity: 0.9 !important;
    transform: translateY(-1px) !important;
}

/* ─── Dataframes / Tables ───────────────────────── */
.dataframe { border-radius: 8px; overflow: hidden; }
.dataframe thead th {
    background-color: #1e2130 !important;
    color: #94a3b8 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.75rem !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
.dataframe tbody td {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    color: #f1f5f9 !important;
    background-color: #252a3d !important;
    border-bottom: 1px solid #334155 !important;
}

/* ─── Selectbox / Inputs ────────────────────────── */
.stSelectbox [data-baseweb="select"] {
    background-color: #1e2130 !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
}

/* ─── Section Headers ───────────────────────────── */
h1 { font-size: 2rem !important; font-weight: 700 !important; }
h2 { font-size: 1.4rem !important; font-weight: 600 !important; color: #94a3b8 !important; border-bottom: 1px solid #334155; padding-bottom: 0.5rem; }
h3 { font-size: 1.1rem !important; font-weight: 500 !important; color: #f1f5f9 !important; }

/* ─── Alert / Info Boxes ────────────────────────── */
.stAlert { border-radius: 8px !important; border-left-width: 4px !important; }

/* ─── Spinner ───────────────────────────────────── */
.stSpinner { color: #6366f1 !important; }

/* ─── Progress Bar ──────────────────────────────── */
.stProgress > div > div { background-color: #6366f1 !important; }

/* ─── Tab Bar ───────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] { background-color: #1e2130 !important; border-radius: 8px; }
.stTabs [data-baseweb="tab"] { color: #94a3b8 !important; font-weight: 500; }
.stTabs [aria-selected="true"] { color: #6366f1 !important; border-bottom: 2px solid #6366f1 !important; }

/* ─── Lottie / Image containers ─────────────────── */
.lottie-container { display: flex; justify-content: center; align-items: center; }

/* ─── Footer ────────────────────────────────────── */
footer { visibility: hidden; }
.hackathon-footer {
    text-align: center;
    color: #334155;
    font-size: 0.75rem;
    padding: 1rem;
    border-top: 1px solid #1e2130;
    margin-top: 2rem;
}
```

## Graphics Utilities: `src/components/visuals.py`

```python
"""
Graphic Designer Agent — Visual Utility Functions
All visual helpers, branded chart wrappers, and export functions.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import os

# ─── Design Tokens ──────────────────────────────────────────────
TOKENS = {
    "bg_primary":    "#0f1117",
    "bg_surface":    "#1e2130",
    "bg_hover":      "#252a3d",
    "accent_blue":   "#6366f1",
    "accent_green":  "#10b981",
    "accent_amber":  "#f59e0b",
    "accent_red":    "#ef4444",
    "accent_purple": "#a855f7",
    "text_primary":  "#f1f5f9",
    "text_muted":    "#94a3b8",
    "border":        "#334155",
}

PLOTLY_TEMPLATE = "plotly_dark"
COLOR_SEQ = [
    TOKENS["accent_blue"],
    TOKENS["accent_green"],
    TOKENS["accent_amber"],
    TOKENS["accent_red"],
    TOKENS["accent_purple"],
]

def _base_layout(title: str = "") -> dict:
    """Returns shared Plotly layout settings."""
    return dict(
        title=dict(text=title, font=dict(size=16, color=TOKENS["text_primary"])),
        paper_bgcolor=TOKENS["bg_primary"],
        plot_bgcolor=TOKENS["bg_surface"],
        font=dict(family="Inter", color=TOKENS["text_muted"]),
        xaxis=dict(gridcolor=TOKENS["border"], linecolor=TOKENS["border"]),
        yaxis=dict(gridcolor=TOKENS["border"], linecolor=TOKENS["border"]),
        legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor=TOKENS["border"]),
        margin=dict(l=40, r=20, t=50, b=40),
    )

# ─── Chart Factories ─────────────────────────────────────────────

def branded_line(df: pd.DataFrame, x: str, y: str, title: str = "", color_col: str = None):
    fig = px.line(df, x=x, y=y, color=color_col, template=PLOTLY_TEMPLATE,
                  color_discrete_sequence=COLOR_SEQ, title=title)
    fig.update_traces(line=dict(width=2.5))
    fig.update_layout(**_base_layout(title))
    return fig

def branded_bar(df: pd.DataFrame, x: str, y: str, title: str = "", orientation: str = "v"):
    fig = px.bar(df, x=x, y=y, orientation=orientation, template=PLOTLY_TEMPLATE,
                 color_discrete_sequence=COLOR_SEQ, title=title)
    fig.update_layout(**_base_layout(title))
    return fig

def branded_scatter(df: pd.DataFrame, x: str, y: str, color: str = None, size: str = None, title: str = ""):
    fig = px.scatter(df, x=x, y=y, color=color, size=size,
                     template=PLOTLY_TEMPLATE, color_discrete_sequence=COLOR_SEQ, title=title)
    fig.update_layout(**_base_layout(title))
    return fig

def branded_pie(df: pd.DataFrame, names: str, values: str, title: str = ""):
    fig = px.pie(df, names=names, values=values, template=PLOTLY_TEMPLATE,
                 color_discrete_sequence=COLOR_SEQ, title=title, hole=0.45)
    fig.update_layout(**_base_layout(title))
    return fig

def branded_heatmap(df: pd.DataFrame, title: str = "Correlation Matrix"):
    corr = df.select_dtypes(include="number").corr()
    fig = px.imshow(corr, title=title, template=PLOTLY_TEMPLATE,
                    color_continuous_scale="RdBu_r", aspect="auto")
    fig.update_layout(**_base_layout(title))
    return fig

def branded_histogram(df: pd.DataFrame, x: str, title: str = ""):
    fig = px.histogram(df, x=x, template=PLOTLY_TEMPLATE,
                       color_discrete_sequence=[TOKENS["accent_blue"]], title=title)
    fig.update_layout(**_base_layout(title))
    return fig

def branded_box(df: pd.DataFrame, x: str, y: str, title: str = ""):
    fig = px.box(df, x=x, y=y, template=PLOTLY_TEMPLATE,
                 color_discrete_sequence=COLOR_SEQ, title=title)
    fig.update_layout(**_base_layout(title))
    return fig

def multi_chart_grid(charts: list, rows: int = 1, cols: int = 2, title: str = ""):
    """Combine multiple plotly figures into a grid."""
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=[c.layout.title.text for c in charts])
    for i, chart in enumerate(charts):
        r, c = divmod(i, cols)
        for trace in chart.data:
            fig.add_trace(trace, row=r + 1, col=c + 1)
    fig.update_layout(**_base_layout(title))
    return fig

# ─── Branded Banner Generator (PIL) ─────────────────────────────

def generate_banner(project_name: str, tagline: str, output_path: str = "assets/banner.png"):
    """Generates a branded PNG banner for the app header and GitHub README."""
    W, H = 1200, 300
    img = Image.new("RGB", (W, H), color="#0f1117")
    draw = ImageDraw.Draw(img)

    # Gradient overlay (simulate with rectangles)
    for i in range(W // 2):
        alpha = int(60 * (1 - i / (W // 2)))
        draw.rectangle([i, 0, i + 1, H], fill=(99, 102, 241, alpha))

    # Text
    draw.rectangle([50, 120, 50 + len(project_name) * 22 + 20, 170], fill="#6366f1")
    draw.text((60, 125), project_name, fill="white")
    draw.text((60, 185), tagline, fill="#94a3b8")
    draw.text((60, 240), "DataQuest 3.0 · VIT Chennai · 2026", fill="#334155")

    os.makedirs("assets", exist_ok=True)
    img.save(output_path)
    return output_path

def image_to_base64(img_path: str) -> str:
    """Convert image to base64 for embedding in Streamlit HTML."""
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def display_banner(project_name: str, tagline: str):
    """Renders the branded header banner inside Streamlit."""
    path = generate_banner(project_name, tagline)
    b64 = image_to_base64(path)
    st.markdown(
        f'<img src="data:image/png;base64,{b64}" style="width:100%;border-radius:12px;margin-bottom:1.5rem;">',
        unsafe_allow_html=True
    )

# ─── Export Functions ────────────────────────────────────────────

def export_chart_as_png(fig, filename: str = "chart.png") -> bytes:
    """Export a Plotly figure as PNG bytes using kaleido."""
    img_bytes = fig.to_image(format="png", width=1200, height=600, scale=2)
    return img_bytes

def download_chart_button(fig, label: str = "Download Chart"):
    """Adds a Streamlit download button for a Plotly chart."""
    img_bytes = export_chart_as_png(fig)
    st.download_button(
        label=f"⬇️ {label}",
        data=img_bytes,
        file_name=f"{label.lower().replace(' ', '_')}.png",
        mime="image/png"
    )

def load_css(css_path: str = "src/components/style.css"):
    """Inject the CSS into the Streamlit app."""
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
```

## Lottie Animations: `src/components/lottie_loader.py`
```python
"""
Loads Lottie JSON animations from LottieFiles CDN and displays them in Streamlit.
Usage: lottie_loader.load_lottie("https://assets5.lottiefiles.com/packages/lf20_xxx.json")
"""
import requests
import streamlit as st
try:
    from streamlit_lottie import st_lottie
    LOTTIE_AVAILABLE = True
except ImportError:
    LOTTIE_AVAILABLE = False

# Pre-selected Lottie URLs for common hackathon domains
LOTTIE_URLS = {
    "data":       "https://assets4.lottiefiles.com/packages/lf20_qp1q7mct.json",
    "ai":         "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json",
    "success":    "https://assets10.lottiefiles.com/packages/lf20_lk80fpsm.json",
    "loading":    "https://assets4.lottiefiles.com/packages/lf20_usmfx6bp.json",
    "healthcare": "https://assets3.lottiefiles.com/packages/lf20_5njp3vgg.json",
    "finance":    "https://assets2.lottiefiles.com/packages/lf20_yd8fbnml.json",
}

def load_lottie(url: str) -> dict | None:
    r = requests.get(url, timeout=5)
    if r.status_code == 200:
        return r.json()
    return None

def display_lottie(key: str = "data", height: int = 200, col=None):
    """Display a lottie animation. key can be a preset name or a full URL."""
    url = LOTTIE_URLS.get(key, key)
    animation = load_lottie(url)
    if animation and LOTTIE_AVAILABLE:
        target = col if col else st
        with target:
            st_lottie(animation, height=height, key=key)
    else:
        (col or st).info("🎬 Animation loading...")
```

## What You Must NOT Do
- Never use bare `st.title()` without first calling `load_css()`.
- Never use default Plotly color schemes. Always pass `color_discrete_sequence=COLOR_SEQ`.
- Never use `matplotlib` or `seaborn` in the UI. Only Plotly.
- Never create charts that are not `use_container_width=True` in Streamlit.
