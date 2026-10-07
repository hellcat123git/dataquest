"""
Deep Analysis Page — 02_analysis.py
Correlation heatmaps, scatter plots, distributions, and statistical breakdowns.
"""
import streamlit as st
import pandas as pd
from src.components.visuals import (
    branded_scatter, branded_heatmap, branded_histogram, branded_box,
    download_chart_button, load_css
)

st.set_page_config(page_title="Deep Analysis", layout="wide")
load_css("src/components/style.css")

st.title("🔬 Deep Analysis")
st.caption("Explore correlations, distributions, and statistical relationships.")
st.divider()

if "df" not in st.session_state:
    st.warning("⚠️ No dataset loaded.")
    st.stop()

df: pd.DataFrame = st.session_state["df"]
num_cols = df.select_dtypes(include="number").columns.tolist()
cat_cols  = df.select_dtypes(include="object").columns.tolist()

# ─── Correlation Heatmap ──────────────────────────────────────────
st.subheader("🌡️ Correlation Matrix")
if len(num_cols) >= 2:
    fig_heat = branded_heatmap(df, title="Numeric Feature Correlations")
    st.plotly_chart(fig_heat, use_container_width=True)
    download_chart_button(fig_heat, "Correlation Heatmap")
else:
    st.info("At least 2 numeric columns required.")

st.divider()

# ─── Scatter & Distribution in 2 columns ─────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("⚡ Scatter Plot")
    if len(num_cols) >= 2:
        x_axis = st.selectbox("X Axis", num_cols, key="sc_x")
        y_axis = st.selectbox("Y Axis", num_cols, index=min(1, len(num_cols)-1), key="sc_y")
        color_by = st.selectbox("Color by", ["None"] + cat_cols, key="sc_c")
        color_col = None if color_by == "None" else color_by
        fig_sc = branded_scatter(df, x=x_axis, y=y_axis, color=color_col,
                                 title=f"{x_axis} vs {y_axis}")
        st.plotly_chart(fig_sc, use_container_width=True)
        download_chart_button(fig_sc, "Scatter Plot")

with col2:
    st.subheader("📊 Distribution")
    if num_cols:
        dist_col = st.selectbox("Column", num_cols, key="dist_col")
        fig_dist = branded_histogram(df, x=dist_col, title=f"Distribution of {dist_col}")
        st.plotly_chart(fig_dist, use_container_width=True)
        download_chart_button(fig_dist, "Distribution Chart")

st.divider()

# ─── Box Plot ─────────────────────────────────────────────────────
st.subheader("📦 Box Plot — Outlier Detection")
if num_cols and cat_cols:
    box_x = st.selectbox("Category", cat_cols, key="box_x")
    box_y = st.selectbox("Metric", num_cols, key="box_y")
    fig_box = branded_box(df, x=box_x, y=box_y, title=f"{box_y} by {box_x}")
    st.plotly_chart(fig_box, use_container_width=True)

st.divider()

# ─── Statistical Summary ──────────────────────────────────────────
st.subheader("📐 Statistical Summary")
stats = df[num_cols].describe().T.round(2) if num_cols else pd.DataFrame()
st.dataframe(stats, use_container_width=True)
