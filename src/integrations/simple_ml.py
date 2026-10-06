import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np

def simple_linear_forecast(df: pd.DataFrame, x_col: str, y_col: str, steps: int = 5):
    """
    Fits a simple linear regression and forecasts N future steps.
    Use this when you need a 'prediction' feature without complex models.
    """
    df_clean = df[[x_col, y_col]].dropna()
    
    # If x is datetime, convert to ordinal
    if pd.api.types.is_datetime64_any_dtype(df_clean[x_col]):
        df_clean = df_clean.copy()
        df_clean[x_col] = pd.to_datetime(df_clean[x_col]).map(pd.Timestamp.toordinal)
    
    X = df_clean[[x_col]].values
    y = df_clean[y_col].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Forecast future values
    last_x = X[-1][0]
    future_x = np.array([[last_x + i] for i in range(1, steps + 1)])
    predictions = model.predict(future_x)
    
    return {
        "r_squared": round(model.score(X, y), 3),
        "predictions": predictions.tolist(),
        "trend": "increasing" if model.coef_[0] > 0 else "decreasing"
    }
