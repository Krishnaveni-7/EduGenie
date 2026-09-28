import re
import json
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

def clean_json_block(text: str) -> str:
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()

def generate_quiz(text: str, num_questions: int = 5) -> list:
    try:
        model = genai.GenerativeModel(model_name="models/gemini-3.8-flash")
        prompt = f"""You are an intelligent educational quiz generator.

Analyze the following input or topic:
"{text}"

Generate multiple-choice questions. If the user explicitly requested a specific number of questions in their text (for example "10 questions on Python"), generate that exact number. If no number is specified, generate {num_questions} questions.

Each question must include:
- A "question" string
- A list of 4 plausible "options"
- A correct "answer" string that exactly matches one of the 4 options.

Format your response strictly as a valid JSON array of objects:
[
  {{
    "question": "Question text?",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "Option A"
  }}
]
"""
        response = model.generate_content(prompt)
        quiz_text = response.text.strip()
        cleaned_text = clean_json_block(quiz_text)
        return json.loads(cleaned_text)
    except Exception as e:
        return [{"error": f"Error in Quiz: {e}"}]
