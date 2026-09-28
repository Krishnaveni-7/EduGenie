import os
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY", "")
if not api_key and os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY="):
                api_key = line.split("=", 1)[1].strip()
                break

if api_key:
    genai.configure(api_key=api_key)

def get_learning_recommendations(topic: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="models/gemini-3.8-flash")
        # Direct generation for whatever topic/request the user provides
        response = model.generate_content(f"Provide learning guidance and recommendations for: {topic}")
        return response.text.strip()
    except Exception as e:
        return f"Error in Learning Path: {e}"
