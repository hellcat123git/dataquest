import plotly.express as px
import pandas as pd

PALETTE = {
    "primary": "#6366f1",
    "accent": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "bg": "#0f1117",
    "surface": "#1e2130"
}

def line_chart(df: pd.DataFrame, x: str, y: str, title: str):
    fig = px.line(df, x=x, y=y, title=title, template="plotly_dark",
                  color_discrete_sequence=[PALETTE["primary"]])
    fig.update_layout(paper_bgcolor=PALETTE["bg"], plot_bgcolor=PALETTE["surface"])
    return fig

def bar_chart(df: pd.DataFrame, x: str, y: str, title: str):
    fig = px.bar(df, x=x, y=y, title=title, template="plotly_dark",
                 color_discrete_sequence=[PALETTE["accent"]])
    fig.update_layout(paper_bgcolor=PALETTE["bg"], plot_bgcolor=PALETTE["surface"])
    return fig

def scatter_chart(df: pd.DataFrame, x: str, y: str, color: str = None, title: str = ""):
    fig = px.scatter(df, x=x, y=y, color=color, title=title, template="plotly_dark")
    fig.update_layout(paper_bgcolor=PALETTE["bg"], plot_bgcolor=PALETTE["surface"])
    return fig

def correlation_heatmap(df: pd.DataFrame, title: str = "Correlation Matrix"):
    corr = df.select_dtypes(include="number").corr()
    fig = px.imshow(corr, title=title, template="plotly_dark",
                    color_continuous_scale="RdBu_r")
    fig.update_layout(paper_bgcolor=PALETTE["bg"])
    return fig
