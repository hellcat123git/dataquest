import streamlit as st
import pandas as pd
import os
from src.config import PROJECT_NAME, TAGLINE, TEAM_NAME
from src.components.visuals import load_css, display_banner, TOKENS

# ─── Page Config ─────────────────────────────────────────────────
st.set_page_config(
    page_title=PROJECT_NAME,
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": f"**{PROJECT_NAME}** — Built at DataQuest 3.0, VIT Chennai."
    }
)

# ─── Inject CSS ──────────────────────────────────────────────────
css_path = "src/components/style.css"
if os.path.exists(css_path):
    load_css(css_path)

# ─── Sidebar ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"### 🚀 {PROJECT_NAME}")
    st.caption(TAGLINE)
    st.divider()

    # Dataset uploader
    uploaded = st.file_uploader("📁 Upload Dataset (CSV)", type=["csv", "xlsx"])
    if uploaded:
        if uploaded.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded)
        else:
            df = pd.read_csv(uploaded)
        st.session_state["df"] = df
        st.success(f"✅ Loaded {len(df):,} rows")

    # OR load from data/clean/
    clean_files = []
    if os.path.isdir("data/clean"):
        clean_files = [f for f in os.listdir("data/clean") if f.endswith(".csv")]
    if clean_files:
        st.divider()
        chosen = st.selectbox("📂 Or select pre-loaded dataset", ["— Select —"] + clean_files)
        if chosen != "— Select —":
            st.session_state["df"] = pd.read_csv(f"data/clean/{chosen}")
            st.success(f"✅ Loaded: {chosen}")

    st.divider()
    st.caption(f"Built by **{TEAM_NAME}**")
    st.caption("DataQuest 3.0 · VIT Chennai · 2026")

# ─── Main Content ─────────────────────────────────────────────────
display_banner(PROJECT_NAME, TAGLINE)

if "df" not in st.session_state:
    st.info("👈 Upload a dataset or select one from the sidebar to get started.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="background:#1e2130;border-radius:12px;padding:1.5rem;border:1px solid #334155;">
        <h3 style="color:#6366f1;">📊 Dashboard</h3>
        <p style="color:#94a3b8;">Interactive data visualizations with filters and drill-down capabilities.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="background:#1e2130;border-radius:12px;padding:1.5rem;border:1px solid #334155;">
        <h3 style="color:#10b981;">🤖 AI Insights</h3>
        <p style="color:#94a3b8;">Natural language summaries powered by Google Gemini API.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="background:#1e2130;border-radius:12px;padding:1.5rem;border:1px solid #334155;">
        <h3 style="color:#f59e0b;">🔮 Predictions</h3>
        <p style="color:#94a3b8;">ML-powered trend forecasting and pattern detection.</p>
        </div>
        """, unsafe_allow_html=True)
else:
    df = st.session_state["df"]
    st.success(f"Dataset loaded: **{len(df):,} rows × {len(df.columns)} columns**")
    
    # Quick preview
    with st.expander("📋 Data Preview", expanded=False):
        st.dataframe(df.head(10), use_container_width=True)

# ─── Footer ──────────────────────────────────────────────────────
st.markdown(
    f'<div class="hackathon-footer">🚀 {PROJECT_NAME} · {TEAM_NAME} · DataQuest 3.0 · VIT Chennai</div>',
    unsafe_allow_html=True
)
