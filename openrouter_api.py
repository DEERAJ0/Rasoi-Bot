import os
import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY") or st.secrets.get("OPENROUTER_API_KEY", None)
MODEL = "sarvamai/sarvam-m:free"  # Free model

def get_recipe(query):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://openrouter.ai",  # required
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": f"Give me a detailed recipe for {query} in Indian style. Include ingredients and steps."}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error fetching recipe: {e}"
