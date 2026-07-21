# 📚 AI Study Assistant

An AI-powered study assistant built with Python, Streamlit, and Google Gemini.

This project started as a simple AI question-answering application and gradually evolved into a complete study assistant. Along the way, I added AI-generated summaries, quizzes, flashcards, support for multiple uploaded documents, and a Retrieval-Augmented Generation (RAG) pipeline to improve answer quality.

Through this project, I gained practical experience building AI applications, working with large language models, managing application state in Streamlit, and using Git feature branches to develop software incrementally.

---

## ✨ Features

- 📄 Upload multiple PDF and TXT notes
- ❓ Ask questions about uploaded notes
- 📝 Generate AI-powered summaries
- 📚 Create downloadable study quizzes
- 🎯 Interactive multiple-choice quizzes with scoring
- 🗂 Generate AI flashcards
- 🔍 Keyword-based Retrieval-Augmented Generation (RAG)
- ⬇️ Download summaries and quizzes

---

## 📖 Feature Overview

### 📄 Multiple File Upload
Upload multiple PDF and TXT files simultaneously. The application combines all uploaded notes into a single knowledge base for studying.

### ❓ Ask Questions
Ask natural language questions about your uploaded notes. The application retrieves the most relevant sections before sending them to Google Gemini, improving answer accuracy while reducing hallucinations.

### 📝 AI Summary
Generate concise summaries highlighting key concepts, important definitions, and revision points.

### 📚 Study Quiz
Generate downloadable revision quizzes containing a mixture of multiple-choice and short-answer questions.

### 🎯 Interactive Quiz
Test your understanding with an interactive multiple-choice quiz featuring:

- Instant feedback
- Score tracking
- Question navigation
- Generate a new quiz anytime

### 🗂 Flashcards
Generate AI-powered flashcards for revision. Navigate through cards, reveal answers, and generate a new set whenever required.

### 🔍 Retrieval-Augmented Generation (RAG)
Instead of sending the entire document to the language model, the application:

- Splits uploaded notes into smaller chunks
- Retrieves the most relevant chunks based on the user's question
- Sends only the retrieved context to Gemini
- Reduces hallucinations by answering only from the uploaded notes

---

## 🛠 Technologies

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- python-dotenv
- Git
- GitHub

---

## 📚 What I Learned

Building this project gave me practical experience with:

- Prompt engineering using Google Gemini
- Building AI web applications with Streamlit
- Managing application state using Streamlit Session State
- Parsing AI-generated outputs into structured data
- Implementing a keyword-based Retrieval-Augmented Generation (RAG) pipeline
- Supporting multiple PDF and TXT uploads
- Writing modular, maintainable Python code
- Using Git feature branches for incremental development
- Deploying applications with Streamlit Community Cloud

---

## 🚀 Installation

### Clone the repository
git clone https://github.com/<your-username>/AI-study-assistant.git

### Install dependencies
pip install -r requirements.txt

### Create a .env file
GEMINI_API_KEY=your_api_key_here

### Run the application
streamlit run app.py

---

## 📂 Project Structure
AI Study Assistant/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
├── .env
└── assets/

---

## 🚀 Future Improvements

- Semantic search using embeddings
- Vector database integration (ChromaDB or FAISS)
- Conversation memory
- Source citations for retrieved answers
- Spaced repetition flashcards
- Export flashcards to Anki
- User authentication

---

## 👨‍💻 Author

Aidan Lee