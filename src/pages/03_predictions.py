"""
Predictions Page — 03_predictions.py
Simple ML forecasting using scikit-learn Linear Regression.
"""
import streamlit as st
import pandas as pd
import numpy as np
from src.components.visuals import branded_line, load_css
from src.integrations.simple_ml import simple_linear_forecast

st.set_page_config(page_title="Predictions", layout="wide")
load_css("src/components/style.css")

st.title("🔮 Predictions")
st.caption("Trend forecasting powered by Linear Regression.")
st.divider()

if "df" not in st.session_state:
    st.warning("⚠️ No dataset loaded.")
    st.stop()

df: pd.DataFrame = st.session_state["df"]
num_cols  = df.select_dtypes(include="number").columns.tolist()
date_cols = [c for c in df.columns if "date" in c or "year" in c]

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ Model Config")
    if not num_cols:
        st.error("No numeric columns in dataset.")
        st.stop()

    target = st.selectbox("Target metric to predict", num_cols)
    steps  = st.slider("Forecast steps ahead", 1, 30, 7)
    run_btn = st.button("🚀 Run Forecast", type="primary", use_container_width=True)

with col2:
    if run_btn:
        if date_cols:
            x_col = date_cols[0]
            df_model = df[[x_col, target]].dropna().copy()
            df_model[x_col] = pd.to_datetime(df_model[x_col], errors='coerce')
            df_model.dropna(inplace=True)
            df_model = df_model.sort_values(x_col)
            df_model["x_ord"] = df_model[x_col].map(pd.Timestamp.toordinal)

            result = simple_linear_forecast(df_model, "x_ord", target, steps)

            st.metric("Model R² Score", f"{result['r_squared']:.3f}",
                      delta="Good fit" if result['r_squared'] > 0.6 else "Weak fit")
            st.metric("Trend Direction", result["trend"].title())

            # Build forecast dates
            last_date = df_model[x_col].max()
            freq = pd.infer_freq(df_model[x_col].dropna()) or "ME"
            future_dates = pd.date_range(last_date, periods=steps + 1, freq=freq)[1:]
            future_df = pd.DataFrame({x_col: future_dates, target: result["predictions"]})
            future_df["type"] = "Forecast"
            hist_df = df_model[[x_col, target]].copy()
            hist_df["type"] = "Historical"
            combined = pd.concat([hist_df, future_df], ignore_index=True)

            fig = branded_line(combined, x=x_col, y=target, color_col="type",
                               title=f"{target.replace('_',' ').title()} — Historical + Forecast")
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("📋 Forecast Values")
            st.dataframe(future_df[[x_col, target]].round(2), use_container_width=True)
        else:
            # No date column — use index
            df_model = df[[target]].dropna().reset_index()
            df_model.rename(columns={"index": "row"}, inplace=True)
            result = simple_linear_forecast(df_model, "row", target, steps)
            st.metric("R² Score", f"{result['r_squared']:.3f}")
            st.metric("Trend", result["trend"].title())
            
            future_rows = list(range(len(df_model), len(df_model) + steps))
            future_df = pd.DataFrame({"row": future_rows, target: result["predictions"], "type": "Forecast"})
            df_model["type"] = "Historical"
            combined = pd.concat([df_model, future_df], ignore_index=True)
            fig = branded_line(combined, x="row", y=target, color_col="type",
                               title=f"{target} Trend + Forecast")
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("👈 Configure the model and click **Run Forecast** to generate predictions.")
        st.markdown("""
        **How it works:**
        1. Fits a Linear Regression on your historical data.
        2. Projects the trend forward for the selected number of steps.
        3. Displays R² score to indicate model confidence.
        
        > 💡 For best results, use a dataset with a clear time column (date, year, month).
        """)
