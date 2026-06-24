import streamlit as st
from utils import ask_gemini, summarise_notes, generate_quiz, generate_mcq, generate_flashcards
from pypdf import PdfReader

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "quiz" not in st.session_state:
    st.session_state.quiz = ""

if "mcq" not in st.session_state:
    st.session_state.mcq = ""

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "last_correct" not in st.session_state:
    st.session_state.last_correct = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "flashcards" not in st.session_state:
    st.session_state.flashcards = ""

if "current_card" not in st.session_state:
    st.session_state.current_card = 0

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

def parse_mcq(mcq_text):
    lines = mcq_text.split("\n")
    
    questions = []
    question = ""
    options = {}
    answer = ""

    current_key = None

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        if line.startswith("QUESTION:"):
            if question and options and answer:
                questions.append({"question": question, "options": options, "answer": answer.strip()})
            current_key = "QUESTION"
            question = line.replace("QUESTION:", "").strip()
            options = {}
            answer = ""
            

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

    if question and options and answer:
        questions.append({"question": question, "options": options, "answer": answer.strip()})
        
    return questions





st.title("AI study assistant")
uploaded_files = st.file_uploader("Upload your notes", type = ["txt", "pdf"], accept_multiple_files = True)



if uploaded_files:
    content = ""
    for uploaded_file in uploaded_files:

        if uploaded_file.name.endswith(".txt"):
            file_content = uploaded_file.read().decode()
            content += f"\n\n---{uploaded_file.name} ---\n\n"
            content += file_content

        elif uploaded_file.name.endswith(".pdf"):
            try:
                pdf = PdfReader(uploaded_file)

                file_content = ""
                for page in pdf.pages:
                    text = page.extract_text()
                    if text is not None:
                        file_content += text + "\n"

                content += f"\n\n---{uploaded_file.name} ---\n\n"
                content += file_content

            except Exception:
                st.error("Unable to read {uploaded_file.name}.")
                st.stop()

        if not content.strip():
            st.error("The uploaded file appears to be empty.")
            st.stop()

    with st.expander("📚 View Notes"):
        st.text_area("Your Notes", content, height = 300)


    tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "❓ Ask Questions",
    "📄 Summary",
    "📝 Study Quiz",
    "🎯 Interactive Quiz",
    "🗂 Flashcards"])

    

    with tab1:
        question = st.text_input("Ask a question")
        col1, col2, col3 = st.columns([1, 1, 6])
        with col1:
            ask_clicked = st.button("Ask")
        with col2:
            clear_clicked = st.button("Clear")


        if ask_clicked:
            if question:
                st.write("You asked: {temp_1}".format(temp_1 = question))
                with st.spinner("Thinking..."):
                    answer = ask_gemini(content, question)
                if answer.startswith("ERROR:"):
                    st.error(answer)
                else:
                    st.session_state.chat_history.append({"question": question, "answer": answer})

        if st.session_state.chat_history:
            st.subheader("Chat History")
            for chat in st.session_state.chat_history:
                st.write(f"**You:** {chat['question']}")
                st.write(f"**AI:** {chat['answer']}")      
                st.divider()

        if clear_clicked:
            st.session_state.chat_history = []
            st.rerun()          

    with tab2:
        if st.button("Summarise notes"):
            with st.spinner("Summarising..."):
                summary = summarise_notes(content)
                if summary.startswith("ERROR:"):
                    st.error(summary)
                else:
                    st.session_state.summary = summary

                

        if st.session_state.summary:
            st.subheader("Summary")
            st.write(st.session_state.summary)
            st.download_button(label = "Download Summary", data = st.session_state.summary, file_name = "summary.txt", mime = "text/plain")

    with tab3:
        if st.button("Generate study quiz"):
            with st.spinner("Creating quiz..."):
                quiz = generate_quiz(content)
                if quiz.startswith("ERROR:"):
                    st.error(quiz)
                else:
                    st.session_state.quiz = quiz

                

        if st.session_state.quiz:
            st.subheader("Quiz")
            st.markdown(st.session_state.quiz)
            st.download_button(label = "Download Study Quiz", data = st.session_state.quiz, file_name = "study_quiz.txt", mime = "text/plain")

    with tab4:
        if st.button("start interactive Quiz"):
            with st.spinner("Creating MCQ..."):
                mcq = generate_mcq(content)
                if mcq.startswith("ERROR:"):
                    st.error(mcq)
                else:
                    st.session_state.mcq = mcq
                    st.session_state.current_question = 0
                    st.session_state.score = 0
                    st.session_state.answered = False
                    st.session_state.last_correct = None
                

        if st.session_state.mcq:
            st.subheader("Interactive Quiz")
            
            mcq_list = parse_mcq(st.session_state.mcq)
            current_index = st.session_state.current_question
            
            if current_index >= len(mcq_list):
                st.subheader("Quiz Complete!")
                st.write(f"Final Score: {st.session_state.score} / {len(mcq_list)}")

                if st.button("Generate new Quiz"):
                    with st.spinner("Creating new quiz..."):
                        mcq = generate_mcq(content)
                        if mcq.startswith("ERROR:"):
                            st.error(mcq)
                        else:
                            st.session_state.mcq = mcq
                            st.session_state.current_question = 0
                            st.session_state.score = 0
                            st.session_state.answered = False
                            st.session_state.last_correct = None
                            st.rerun()
                st.stop()

            current_mcq = mcq_list[current_index]

            st.write(f"Score: {st.session_state.score} / {len(mcq_list)}")
            st.write(f"Question {current_index + 1} of {len(mcq_list)}")
            st.write(current_mcq["question"])

            selected_answer = st.radio("Choose your answer:", ["A", "B", "C", "D"], format_func = lambda option: f"{option}: {current_mcq['options'].get(option, '')}" )

            if not st.session_state.answered:
                if st.button("Check answer"):

                    correct_answer = current_mcq["answer"].strip()
                    if selected_answer == correct_answer:
                        st.session_state.score += 1
                        st.session_state.last_correct = True

                    else:
                        st.session_state.last_correct = False
                    
                    st.session_state.answered = True
                    st.rerun()

            else:
                if st.session_state.last_correct:
                    st.success("Correct!")
                else:
                    st.error(f"Incorrect. The correct answer is {current_mcq['answer']}.")
                
                if st.button("Next question"):
                    st.session_state.current_question += 1
                    st.session_state.answered = False
                    st.session_state.last_correct = None
                    st.rerun()

    
    with tab5:
        if not st.session_state.flashcards:

            if st.button("Generate Flashcards"):
                with st.spinner("Creating flascards..."):
                    flashcards = generate_flashcards(content)

                if flashcards.startswith("ERROR:"):
                    st.error(flashcards)

                else:
                    st.session_state.flashcards = flashcards
                    st.session_state.current_card = 0
                    st.session_state.show_answer = False
                    st.session_state.show_answer = False
                    st.rerun()

            
        else:
            if st.button("Generate New Flashcards"):
                with st.spinner("Creating new flashcards..."):
                    flashcards = generate_flashcards(content)

                if flashcards.startswith("ERROR:"):
                    st.error(flashcards)
                else:
                    st.session_state.flashcards = flashcards
                    st.session_state.current_card = 0
                    st.session_state.show_answer = False
                    st.rerun()

            st.subheader("Raw Flashcards Output")
            st.write(st.session_state.flashcards)
                    
