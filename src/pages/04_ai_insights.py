"""
AI Insights Page — 04_ai_insights.py
Connects to Gemini API and displays natural language insights.
"""
import streamlit as st
import pandas as pd
import os, time
from src.components.visuals import load_css
from src.config import ENABLE_AI_INSIGHTS

st.set_page_config(page_title="AI Insights", layout="wide")
load_css("src/components/style.css")

st.title("🤖 AI Insights")
st.caption("Powered by Google Gemini — Natural language analysis of your data.")
st.divider()

if "df" not in st.session_state:
    st.warning("⚠️ No dataset loaded. Go back to the home page and upload a CSV.")
    st.stop()

df: pd.DataFrame = st.session_state["df"]

# ─── AI Panel ────────────────────────────────────────────────────
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Executive Summary")
    
    domain = st.text_input("What domain is this data about?",
                           placeholder="e.g., Healthcare, Finance, Agriculture...")
    problem = st.text_area("What problem are you solving?",
                           placeholder="e.g., Predicting supply shortages in rural clinics...",
                           height=100)
    
    gen_btn = st.button("✨ Generate AI Summary", type="primary", use_container_width=True)
    
    if gen_btn:
        if not ENABLE_AI_INSIGHTS:
            st.error("⚠️ GEMINI_API_KEY not found in .env file. Using demo mode.")
            with st.spinner("Generating insights..."):
                time.sleep(2)
            st.markdown("""
            **AI Executive Summary (Demo Mode)**
            
            • **Trend Alert:** The dataset reveals a 23.7% upward trend in the primary metric over the observed period, concentrated in Q3.
            • **Anomaly Detected:** Approximately 8.2% of records fall more than 2 standard deviations from the mean — warranting further investigation.
            • **Recommendation:** Reallocating 15% of resources from the top-performing category to the bottom three would improve overall distribution efficiency by an estimated 31%.
            """)
        else:
            try:
                from src.integrations.gemini_client import generate_data_summary
                with st.spinner("🧠 Gemini is analyzing your data..."):
                    summary = generate_data_summary(df, domain, problem)
                st.success("✅ Analysis complete!")
                st.markdown(summary)
                if "ai_summaries" not in st.session_state:
                    st.session_state["ai_summaries"] = []
                st.session_state["ai_summaries"].append(summary)
            except Exception as e:
                st.error(f"API Error: {e}")

with col2:
    st.subheader("💬 Ask a Question")
    st.caption("Ask anything about your data in plain English.")
    
    question = st.text_area("Your question", placeholder="e.g., Which district has the highest average cost?", height=80)
    ask_btn = st.button("🔍 Ask AI", use_container_width=True)
    
    if ask_btn and question:
        if not ENABLE_AI_INSIGHTS:
            with st.spinner("Thinking..."):
                time.sleep(1.5)
            st.info("**Demo Answer:** Based on the data, the answer appears to be related to the top-performing category. Enable Gemini API for accurate responses.")
        else:
            try:
                from src.integrations.gemini_client import answer_question
                with st.spinner("🧠 Thinking..."):
                    answer = answer_question(df, question)
                st.success(answer)
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()

# ─── Trend Prediction ────────────────────────────────────────────
st.subheader("🔮 Trend Prediction")
num_cols = df.select_dtypes(include="number").columns.tolist()
date_cols = [c for c in df.columns if "date" in c or "year" in c]

if num_cols and date_cols:
    pred_col = st.selectbox("Select metric to predict trend for:", num_cols)
    predict_btn = st.button("📈 Predict Trend", use_container_width=False)
    
    if predict_btn:
        if not ENABLE_AI_INSIGHTS:
            with st.spinner("Running model..."):
                time.sleep(2)
            st.markdown("""
            **Trend Analysis (Demo Mode)**
            
            The selected metric shows a **moderately increasing** trend (R² = 0.78).
            Projected value for the next period: **+12.4% above current baseline**.
            Confidence interval: ±3.2%
            """)
        else:
            try:
                from src.integrations.gemini_client import predict_trend
                with st.spinner("Analyzing trend..."):
                    result = predict_trend(df, pred_col)
                st.success(result)
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("A dataset with both numeric columns and a date column is required for trend prediction.")

# ─── History ─────────────────────────────────────────────────────
if st.session_state.get("ai_summaries"):
    st.divider()
    with st.expander("📚 Summary History", expanded=False):
        for i, s in enumerate(reversed(st.session_state["ai_summaries"])):
            st.markdown(f"**Summary {len(st.session_state['ai_summaries']) - i}:**")
            st.markdown(s)
            st.divider()
