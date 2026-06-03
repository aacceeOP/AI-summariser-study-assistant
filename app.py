import streamlit as st
from utils import ask_gemini, summarise_notes, generate_quiz, generate_mcq
from pypdf import PdfReader

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "quiz" not in st.session_state:
    st.session_state.quiz = ""

if "mcq" not in st.session_state:
    st.session_state.mcq = ""

def parse_mcq(mcq_text):
    lines = mcq_text.split("\n")
    question = ""
    options = {}
    answer = ""

    current_key = None

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        if line.startswith("QUESTION:"):
            current_key = "QUESTION"
            question = line.replace("QUESTION:", "").strip()

        elif line.startswith("A:"):
            current_key = "A"
            options["A"] = line.replace("A:", "").strip()

        elif line.startswith("B:"):
            current_key = "B"
            options["B"] = line.replace("B:", "").strip()

        elif line.startswith("C:"):
            current_key = "C"
            options["C"] = line.replace("C:", "").strip()

        elif line.startswith("D:"):
            current_key = "D"
            options["D"] = line.replace("D:", "").strip()

        elif line.startswith("ANSWER:"):
            current_key = "ANSWER"
            answer = line.replace("ANSWER:", "").strip()

        else:
            if current_key == "QUESTION":
                question += " " + line
            elif current_key in options:
                options[current_key] += " " + line
            elif current_key == "ANSWER":
                answer += line.strip()
        
    return question, options, answer





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

    if st.button("Generate MCQ"):
        with st.spinner("Creating MCQ..."):
            st.session_state.mcq = generate_mcq(content)

    if st.session_state.mcq:
        st.subheader("Interactive Quiz")
        
        mcq_question, mcq_options, correct_answer = parse_mcq(st.session_state.mcq)
        st.write(mcq_question)
        selected_answer = st.radio("Choose your answer:", ["A", "B", "C", "D"], format_func = lambda option: f"{option}: {mcq_options.get(option, "")}" )

        if st.button("Check answer"):
            if selected_answer == correct_answer.strip():
                st.success("Correct!")

            else:
                st.error(f"Incorrect. The correct answer is {correct_answer}.")