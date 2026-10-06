import google.generativeai as genai
import pandas as pd
import json
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_data_summary(df: pd.DataFrame, domain: str, problem: str) -> str:
    """
    Takes a dataframe, sends the first 50 rows as context to Gemini,
    and returns a 3-bullet-point executive summary.
    """
    sample = df.head(50).to_json(orient="records", indent=2)
    
    prompt = f"""
    You are a senior data analyst specializing in {domain}.
    The team is solving this problem: "{problem}"
    
    Here is a sample of the dataset (first 50 rows in JSON):
    {sample}
    
    Based on this data, provide EXACTLY 3 actionable bullet points of insights.
    Format your response as:
    • [Insight 1]
    • [Insight 2]  
    • [Insight 3]
    
    Be specific. Use numbers from the data. Keep each bullet under 30 words.
    """
    
    response = model.generate_content(prompt)
    return response.text

def predict_trend(df: pd.DataFrame, target_column: str) -> str:
    """
    Asks Gemini to predict the trend of a given column.
    """
    stats = df[target_column].describe().to_dict()
    
    prompt = f"""
    You are a forecasting analyst. Here are the statistics for the column '{target_column}':
    {json.dumps(stats, indent=2)}
    
    In 2-3 sentences, describe the trend you observe and what is likely to happen next.
    Be direct and data-driven.
    """
    response = model.generate_content(prompt)
    return response.text

def answer_question(df: pd.DataFrame, question: str) -> str:
    """
    A simple Q&A function. User asks a question about the data, Gemini answers.
    """
    sample = df.head(100).to_json(orient="records")
    prompt = f"""
    You are a data assistant. Here is a dataset sample:
    {sample}
    
    Answer this question concisely: {question}
    """
    response = model.generate_content(prompt)
    return response.text
