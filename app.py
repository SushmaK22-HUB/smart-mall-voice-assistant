import streamlit as st

from modules.speech_to_text import listen
from modules.chatbot import get_response

st.title("🛍️ Smart Mall Voice Assistant")

st.write("Welcome to the AI-powered mall assistant.")

if st.button("🎤 Speak Now"):

    st.write("Listening...")

    user_text = listen()

    st.success(f"You said: {user_text}")

    response = get_response(user_text)

    st.info(f"Assistant: {response}")