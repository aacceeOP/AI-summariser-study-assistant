import streamlit as st
st.title("AI study assistant")
uploaded_file = st.file_uploader("Upload your notes", type = ["txt"])
if uploaded_file:
    content = uploaded_file.read().decode()
    st.subheader("Your Notes")
    st.text_area(content, height = 300)

question = st.text_input("Ask a question")
if question:
    st.write("You asked: {temp_1}".format(temp_1 = question))