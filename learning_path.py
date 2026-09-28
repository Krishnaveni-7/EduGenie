import os
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
        prompt = (
            f"Generate a personalized, structured learning roadmap for '{topic}'. "
            f"Organize concepts from beginner to advanced difficulty, and recommend useful "
            f"resources such as videos, articles, documentation, or books."
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error in Learning Path: {e}"
