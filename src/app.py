import streamlit as st
from src.config import PROJECT_NAME, TAGLINE

st.set_page_config(
    page_title=PROJECT_NAME,
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Global CSS
with open("src/components/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar Navigation is handled by Streamlit's pages/ folder automatically
st.title(f"🚀 {PROJECT_NAME}")
st.markdown(f"> {TAGLINE}")
