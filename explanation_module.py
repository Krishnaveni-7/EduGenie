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

# Global model caches
_tokenizer = None
_model = None

def get_local_model():
    global _tokenizer, _model
    if _model is None:
        try:
            from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
            _tokenizer = AutoTokenizer.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
            _model = AutoModelForSeq2SeqLM.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
        except Exception:
            _model = False
    return _tokenizer, _model

def explain_topic(topic: str) -> str:
    # 1. Try local lightweight model if running in local environment
    try:
        tokenizer, model = get_local_model()
        if model and tokenizer:
            input_text = f"Explain the concept of '{topic}' in a simple and clear way for a school student."
            inputs = tokenizer(input_text, return_tensors="pt")
            outputs = model.generate(
                **inputs,
                max_new_tokens=150,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                do_sample=True
            )
            return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception:
        pass

    # 2. Cloud Serverless fallback for Vercel / Render Free Tier
    try:
        model = genai.GenerativeModel(model_name="models/gemini-3.5-flash-lite")
        prompt = f"Explain the concept of '{topic}' in a simple and clear way for a school student."
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error in Explanation: {e}"
