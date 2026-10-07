"""
Overview Page — 01_overview.py
Shows KPI metric cards, primary chart, and quick data summary.
Agent: Dashboard Engineer reads agents/dashboard-engineer/SKILL.md
"""
import streamlit as st
import pandas as pd
from src.components.visuals import (
    branded_line, branded_bar, branded_pie, load_css, TOKENS
)
from src.components.metric_cards import render_metric_row

st.set_page_config(page_title="Overview", layout="wide")
load_css("src/components/style.css")

st.title("📊 Overview")
st.caption("Key metrics and primary trends at a glance.")
st.divider()

if "df" not in st.session_state:
    st.warning("⚠️ No dataset loaded. Go back to the home page and upload a CSV.")
    st.stop()

df: pd.DataFrame = st.session_state["df"]

# ─── Sidebar Filters ──────────────────────────────────────────────
with st.sidebar:
    st.header("🎛️ Filters")
    cat_cols = df.select_dtypes(include="object").columns.tolist()
    num_cols = df.select_dtypes(include="number").columns.tolist()

    selected_cat = None
    if cat_cols:
        selected_cat = st.selectbox("Filter by category", ["All"] + cat_cols)
        if selected_cat and selected_cat != "All":
            cat_vals = df[selected_cat].unique().tolist()
            chosen_val = st.multiselect("Select values", cat_vals, default=cat_vals[:3])
            if chosen_val:
                df = df[df[selected_cat].isin(chosen_val)]

    if num_cols:
        selected_num = st.selectbox("Primary metric", num_cols)
    else:
        selected_num = None

# ─── KPI Metrics ─────────────────────────────────────────────────
st.subheader("📌 Key Metrics")
if num_cols:
    metrics = []
    for col in num_cols[:4]:
        total = df[col].sum()
        avg   = df[col].mean()
        metrics.append({
            "label": col.replace("_", " ").title(),
            "value": f"{total:,.0f}" if total > 1000 else f"{total:.2f}",
            "delta": f"avg {avg:.2f}"
        })
    render_metric_row(metrics)
else:
    st.info("No numeric columns detected for metrics.")

st.divider()

# ─── Primary Chart ────────────────────────────────────────────────
col1, col2 = st.columns([2, 1])

date_cols = [c for c in df.columns if "date" in c or "year" in c or "time" in c]

with col1:
    if date_cols and selected_num:
        st.subheader(f"📈 {selected_num.replace('_',' ').title()} Over Time")
        time_df = df[[date_cols[0], selected_num]].dropna().sort_values(date_cols[0])
        fig = branded_line(time_df, x=date_cols[0], y=selected_num,
                           title=f"{selected_num.replace('_',' ').title()} Trend")
        st.plotly_chart(fig, use_container_width=True)
    elif selected_num and cat_cols:
        st.subheader(f"📊 {selected_num.replace('_',' ').title()} by Category")
        agg = df.groupby(cat_cols[0])[selected_num].sum().reset_index().sort_values(selected_num, ascending=False).head(10)
        fig = branded_bar(agg, x=cat_cols[0], y=selected_num,
                          title=f"Top 10 by {selected_num.replace('_',' ').title()}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Add a date or category column to enable chart rendering.")

with col2:
    if cat_cols and selected_num:
        st.subheader(f"🥧 Distribution")
        pie_df = df.groupby(cat_cols[0])[selected_num].sum().reset_index().head(8)
        fig = branded_pie(pie_df, names=cat_cols[0], values=selected_num,
                          title="Category Breakdown")
        st.plotly_chart(fig, use_container_width=True)

# ─── Data Table ───────────────────────────────────────────────────
st.divider()
st.subheader("🗂️ Data Sample")
st.dataframe(
    df.head(20).style.format({col: "{:,.2f}" for col in num_cols if col in df.columns}),
    use_container_width=True,
    height=300
)
st.caption(f"Showing 20 of {len(df):,} rows")
