import os 
from google import genai
from dotenv import load_dotenv

load_dotenv()


MODEL_NAME = "gemini-2.5-flash"
def call_gemini(prompt):
    try:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            return "ERROR: GEMINI API KEY IS MISSING."
        
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(model = MODEL_NAME, contents = prompt)
        return response.text
    except Exception:
        return "ERROR: GEMINI IS CURRENTLY UNAVAILABLE. PLEASE TRY AGAIN LATER."

def ask_gemini(notes, question):
    

    prompt = f"""
You are a helpful study assitant.

Use only the notes below to answer the question 

Notes:
{notes}

Question:
{question}
"""
   

    return call_gemini(prompt)


def summarise_notes(notes):
   
    prompt = f"""
Summarise these notes for a student. 

Include 
1. Key ideas
2. Important definitions
3. Things to remember

Notes:
{notes}
"""
    

    return call_gemini(prompt)


def generate_quiz(notes):
    
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
    

    return call_gemini(prompt)


def generate_mcq(notes):
    
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
    

    return call_gemini(prompt)



def generate_flashcards(notes):
    prompt = f"""
Create 10 flashcards from these notes.

return only in this exact format:

FRONT:
<question or term>

BACK:
<answer or explanation>

FRONT:
<question or term>

BACK:
<answer or explanation>

Notes:
{notes}
"""

    return call_gemini(prompt)