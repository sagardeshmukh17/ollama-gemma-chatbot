import streamlit as st
from backend import ask_ollama   # import function from backend.py

st.set_page_config(page_title="Ollama Chatbot - Gemma", layout="centered")

st.title("🧠 Ollama Chatbot (Gemma Model)")

# Input box
user_input = st.text_area("Ask something:", placeholder="Type your question here...")

# Button
if st.button("Send"):
    if user_input.strip() != "":
        with st.spinner("Thinking..."):
            answer = ask_ollama(user_input)
        st.success("Response:")
        st.write(answer)
    else:
        st.warning("Please enter a question before sending.")
