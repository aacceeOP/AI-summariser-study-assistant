import streamlit as st
from utils import ask_gemini, summarise_notes, generate_quiz
from pypdf import PdfReader

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "quiz" not in st.session_state:
    st.session_state.quiz = ""


st.title("AI study assistant")
uploaded_file = st.file_uploader("Upload your notes", type = ["txt", "pdf"])
if uploaded_file:
    if uploaded_file.name.endswith(".txt"):
        content = uploaded_file.read().decode()

    elif uploaded_file.name.endswith(".pdf"):
        pdf = PdfReader(uploaded_file)

        content = ""
        for page in pdf.pages:
            content += page.extract_text() + "\n"

            
    st.text_area("Your Notes", content, height = 300)

    question = st.text_input("Ask a question")
    if question:
        st.write("You asked: {temp_1}".format(temp_1 = question))
        with st.spinner("Thinking..."):
            answer = ask_gemini(content, question)
        st.write("Answer: {answers}".format(answers = answer))

    if st.button("Summarise notes"):
        with st.spinner("Summarising..."):
            summary = summarise_notes(content)
            st.session_state.summary = summary

    if st.session_state.summary:
        st.subheader("Summary")
        st.write(st.session_state.summary)

    if st.button("Generate quiz"):
        with st.spinner("Creating quiz..."):
            quiz = generate_quiz(content)
            st.session_state.quiz = quiz

    if st.session_state.quiz:
        st.subheader("Quiz")
        st.write(st.session_state.quiz)