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
    relevant_chunks = retrieve_relevant_chunks(notes, question)

    
    if not relevant_chunks:
        return "I couldn't find anything related to your question in the uploaded notes."
    
    context = "\n\n".join(relevant_chunks)

    prompt = f"""
You are a helpful study assitant.

Use only the notes below to answer the question.

if the answer is not found in the contexxt, simply say that it is not available in the uploaded notes. do not make up information. 

Context:
{context}

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


def parse_flashcards(flashcards_text):
    cards = []
    blocks = flashcards_text.split("FRONT:")
    for block in blocks[1:]:
        if "BACK:" in block:
            front, back = block.split("BACK:", 1)

            cards.append({"front": front.strip(), "back": back.strip()})

    return cards



def split_into_chunks(text, chunk_size=1000, overlap = 200):
    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")
    
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start+= chunk_size - overlap

    return chunks



def retrieve_relevant_chunks(notes, question, top_k = 3):
    chunks = split_into_chunks(notes)
    
    stop_words = {
    "a", "an", "and", "are", "as", "at", "be", "by",
    "for", "from", "how", "in", "is", "it", "of", "on",
    "or", "the", "to", "what", "when", "where", "which",
    "who", "why", "with"
}

    question_words = [
        word.strip(".,?!:;()[]{}\"'")
        for word in question.lower().split()
    ]

    question_words = [
        word
        for word in question_words
        if word and word not in stop_words
]

    scored_chunks = []

    for chunk in chunks:
        chunk_lower = chunk.lower()

        score = 0

        for word in question_words:
            score += chunk_lower.count(word)

        question_phrase = " ".join(question_words)
        if question_phrase and question_phrase in chunk_lower:
            score += 3

        scored_chunks.append((score, chunk))
    scored_chunks.sort(key = lambda item: item[0], reverse = True)

    relevant_chunks = [chunk for score, chunk in scored_chunks[:top_k] if score > 0]

    return relevant_chunks
