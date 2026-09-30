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

def summarize_text(text: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="models/gemini-3.5-flash-lite")
        response = model.generate_content(f"Summarize the following text clearly: {text}")
        return response.text.strip()
    except Exception as e:
        return f"Error in Summary: {e}"
