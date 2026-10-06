import streamlit as st

def render_metric_row(metrics: list[dict]):
    """
    metrics: [{"label": "Total Cases", "value": 12000, "delta": "+5%"}, ...]
    """
    cols = st.columns(len(metrics))
    for col, m in zip(cols, metrics):
        col.metric(label=m["label"], value=m["value"], delta=m.get("delta"))
