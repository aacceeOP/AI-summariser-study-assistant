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

for the mcq questions, please make it so that its in this format

QUESTION:
<question>

A:
<option A>

B:
<option B>

C:
<option C>

D:
<option D>

Notes:
{notes}
"""
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = prompt)

    return response.text


def generate_mcq(notes):
    client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
    prompt = f"""
Create 5 multiple choice question from these notes. 
all 4 options must be distinct.
only one option may be correct. 

Retrun only in this exact format:
QUESTION:
<question>

A:
<option A>

B:
<option B>

C:
<option C>

D:
<option D>

ANSWER:
<correct option letter>

Notes:
{notes}
"""
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = prompt)

    return response.text