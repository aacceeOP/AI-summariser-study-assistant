import os 
from google import genai
from dotenv import load_dotenv

load_dotenv()

def ask_gemini(notes, question):
    client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

    prompt = f"""
You are a helpful study assitant.

Use only the notes below to answer the question 

Notes:
{notes}

Question:
{question}
"""
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = prompt)

    return response.text


def summarise_notes(notes):
    client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
    prompt = f"""
Summarise these notes for a student. 

Include 
1. Key ideas
2. Important definitions
3. Things to remember

Notes:
{notes}
"""
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = prompt)

    return response.text


def generate_quiz(notes):
    client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
    prompt = f"""
Create a short quiz from these notes.

Include 
- 5 questions
- A mix of mcq and short answer questions
- answers at the bottom

Notes:
{notes}
"""
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = prompt)

    return response.text