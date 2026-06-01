import streamlit as st
from utils import ask_gemini, summarise_notes, generate_quiz

st.title("AI study assistant")
uploaded_file = st.file_uploader("Upload your notes", type = ["txt"])
if uploaded_file:
    content = uploaded_file.read().decode()#("utf8")
    #st.subheader("Your Notes")
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

        st.subheader("Summary")
        st.write(summary)

    if st.button("Generate quiz"):
        with st.spinner("Creating quiz..."):
            quiz = generate_quiz(content)

        st.subheader("Quiz")
        st.write(quiz)