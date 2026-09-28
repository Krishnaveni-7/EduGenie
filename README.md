# EduGenie: AI-Powered Learning Assistant

EduGenie is an intelligent educational companion that combines cloud-scale generative reasoning (**Google Gemini**) and lightweight local inference (**MBZUAI/LaMini-Flan-T5**) with **FastAPI** to deliver concept explanations, academic Q&A, automatic quiz generation, text summarization, and customized learning roadmaps.

---

## Features

- **Academic & General Q&A**: Real-time accurate answers to student questions powered by Google Gemini.
- **Simplified Concept Explanation**: Clear, beginner-friendly explanations tailored for school students using the locally hosted `MBZUAI/LaMini-Flan-T5-783M` model.
- **Text Summarization**: Condenses long articles, textbook passages, and study notes into concise, key revision summaries.
- **Interactive Quiz Generator**: Automatically creates 3 multiple-choice questions (MCQs) with four options each, complete with instant in-browser answer validation and feedback.
- **Personalized Learning Roadmaps**: Generates step-by-step learning paths (Beginner, Intermediate, and Advanced) with estimated timelines, recommended resources, and adaptive learning tips.

---

## Project Structure

```text
EduGenie/
├── static/
│   └── style.css             # Responsive styling and card UI
├── templates/
│   └── index.html            # Frontend HTML with interactive JavaScript
├── explanation_module.py     # Local LaMini-Flan-T5 model inference
├── learning_path.py          # Gemini-powered learning path generator
├── main.py                   # FastAPI application & RESTful routing
├── qna.py                    # Gemini-powered Q&A logic
├── quiz_module.py            # Gemini-powered MCQ quiz generation and grading
├── requirements.txt          # Python package dependencies
├── summary_module.py         # Gemini-powered text summarization
└── README.md                 # Project documentation
```

---

## Tech Stack

- **Backend**: Python 3.10+, FastAPI, Uvicorn
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
- **AI Models**:
  - Google Gemini API (`gemini-3.8-flash`)
  - Hugging Face Transformers (`MBZUAI/LaMini-Flan-T5-783M`) & PyTorch
- **Templating**: Jinja2

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Krishnaveni-7/EduGenie.git
cd EduGenie
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API Key
Create a `.env` file in the root directory:
```text
GEMINI_API_KEY=your_google_gemini_api_key_here
```
Or export it directly in your environment:
- **Windows (PowerShell):** `$env:GEMINI_API_KEY="your_api_key_here"`
- **Linux / macOS:** `export GEMINI_API_KEY="your_api_key_here"`

### 4. Run the Application
```bash
uvicorn main:app --reload
```

Open your browser and navigate to **http://127.0.0.1:8000** to start using EduGenie.

---

## License
MIT License
