AI Study Assistant

An AI-powered study assistant built with Python, Streamlit, and Google Gemini.

I built this project to explore how generative AI can support students in their revision. Starting from a simple question-answering application, I gradually expanded it into a full-featured AI study assistant by adding summaries, quizzes, flashcards, multiple file uploads, error handling, and a keyword-based Retrieval-Augmented Generation (RAG) pipeline. Along the way, I gained hands-on experience with prompt engineering, Streamlit, session state management, and Git while learning how modern AI applications are designed and built.


⸻


✨ Highlights
📄 Upload multiple PDF and TXT notes
❓ Ask questions about uploaded notes
📝 Generate AI-powered summaries
📚 Create downloadable study quizzes
🎯 Interactive multiple-choice quizzes with scoring
🗂 Generate AI flashcards
🔍 Keyword-based Retrieval-Augmented Generation (RAG)
⬇️ Download summaries and quizzes


⸻


📖 Features
📄 Multiple File Upload
Upload multiple PDF and TXT files simultaneously. The application combines all uploaded notes into a single knowledge base for studying.
❓ Ask Questions
Ask natural language questions about your uploaded notes. The application retrieves the most relevant sections before sending them to Google Gemini to generate accurate answers.
📝 AI Summary
Generate concise summaries highlighting key concepts, important definitions, and revision points.
📚 Study Quiz
Generate revision quizzes containing a mixture of multiple-choice and short-answer questions. Quizzes can be downloaded as text files for offline revision.
🎯 Interactive Quiz
Test your understanding through an interactive multiple-choice quiz featuring:
Instant feedback
Score tracking
Question navigation
Generate a new quiz at any time
🗂 Flashcards
Generate AI-powered flashcards for revision. Navigate between cards, reveal answers, and generate a new set whenever required.
🔍 Retrieval-Augmented Generation (RAG)
Instead of sending the entire document to the language model, the application:
Splits uploaded notes into smaller chunks
Retrieves the most relevant chunks based on the user’s question
Sends only the relevant context to Gemini
Prevents hallucinations by responding only using information from the uploaded notes


⸻


🛠 Technologies
Python
Streamlit
Google Gemini API
PyPDF2
python-dotenv
Git & GitHub


⸻


📚 What I Learned
Building this project helped me gain practical experience in:
Prompt engineering with Google Gemini
Building AI applications using Streamlit
Managing application state with Streamlit Session State
Parsing AI-generated outputs into structured data
Implementing a keyword-based Retrieval-Augmented Generation (RAG) pipeline
Supporting multiple PDF and TXT file uploads
Applying modular software design principles
Using Git feature branches and GitHub for incremental development


⸻


🚀 Installation
Clone the repository
git clone <repository-url>
Install dependencies
pip install -r requirements.txt
Create a 
.env
file
GEMINI_API_KEY=your_api_key_here
Run the application
streamlit run app.py


⸻


📁 Project Structure
AI Study Assistant/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
├── .env
└── assets/


⸻


🔮 Future Improvements
Semantic search using embeddings
Vector database integration (ChromaDB / FAISS)
Conversation memory
Source citations for retrieved answers
Spaced repetition flashcards
Export flashcards to Anki
User authentication
Cloud deployment


⸻


👨‍💻 Author
Aidan Lee