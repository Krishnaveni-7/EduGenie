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

def get_gemini_model():
    for name in ["models/gemini-3.8-flash", "models/gemini-3.7-flash", "models/gemini-2.5-flash", "models/gemini-1.5-pro"]:
        try:
            return genai.GenerativeModel(model_name=name)
        except Exception:
            continue
    return genai.GenerativeModel(model_name="models/gemini-3.5-flash-lite")

def answer_question_with_gemini(question: str) -> str:
    try:
        model = get_gemini_model()
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"Error in QnA: {e}"
