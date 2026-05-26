import os
import streamlit as st

from modules.speech_to_text import listen
from modules.chatbot import get_response
from modules.search_engine import (
    get_all_stores,
    get_all_food,
    get_jobs,
    get_offers,
    get_events,
    get_emergency
)

# ---------------- CHAT HISTORY ---------------- #

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- PATHS ---------------- #

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGO_PATH = os.path.join(BASE_DIR, "assets", "mall_logo.jpg")
MAP_PATH = os.path.join(BASE_DIR, "assets", "mall_map.jpg")

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Smart Mall Voice Assistant",
    page_icon="🛍️",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.image(LOGO_PATH, width=250)

st.title("🛍️ Smart Mall Voice Assistant")

st.write("Welcome to the AI-powered mall assistant.")

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.header("Mall Services")

    st.write("🛍 Stores")
    st.write("🍔 Food")
    st.write("🚗 Parking")
    st.write("💼 Jobs")
    st.write("🎁 Offers")
    st.write("📅 Events")
    st.write("🚨 Emergency")

st.markdown("---")

st.subheader("📊 Statistics")

st.write("Stores:", len(get_all_stores().splitlines()) - 1)

st.write("Food Outlets:", len(get_all_food().splitlines()) - 1)    

# ---------------- QUICK SERVICES ---------------- #

st.subheader("Quick Services")

if st.button("🍔 View Food Outlets"):
    st.text(get_all_food())

if st.button("📋 View All Stores"):

    st.subheader("🛍 Store Directory")

    stores_text = get_all_stores()

    st.code(stores_text)

if st.button("💼 View Jobs"):
    st.text(get_jobs())

if st.button("🎁 View Offers"):
    st.text(get_offers())

if st.button("🎉 View Events"):
    st.text(get_events())

if st.button("🚨 Emergency Information"):
    st.text(get_emergency())

# ---------------- SHORTCUT BUTTONS ---------------- #

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("🛍 Stores"):
        st.info("Try asking: Where is Nike?")

    if st.button("🍔 Food"):
        st.info("Try asking: KFC")

with col2:

    if st.button("🚗 Parking"):
        st.info("Try asking: Parking")

    if st.button("💼 Jobs"):
        st.info("Try asking: Jobs")

with col3:

    if st.button("🎁 Offers"):
        st.info("Try asking: Offers")

    if st.button("🚨 Emergency"):
        st.info("Try asking: Emergency Exit")

# ---------------- MALL MAP ---------------- #

st.subheader("🗺️ Mall Map")

if st.button("Show Mall Map"):

    st.image(
        MAP_PATH,
        caption="Sarath City Capital Mall Map",
        use_container_width=True
    )

# ---------------- VOICE ASSISTANT ---------------- #

st.subheader("🎤 Voice Assistant")

if st.button("🎤 Speak Now"):

    st.write("Listening...")

    user_text = listen()

    st.success(f"You said: {user_text}")

    response = get_response(user_text)

    # Save conversation
    st.session_state.chat_history.append(
        ("You", user_text)
    )

    st.session_state.chat_history.append(
        ("Assistant", response)
    )

    st.info(f"Assistant: {response}")

# ---------------- TEXT SEARCH ---------------- #

st.subheader("⌨️ Type Your Question")

st.caption(
    "Examples: Where is Nike? | KFC | Parking | "
    "All Stores | Jobs | Offers | Events | Emergency"
)

user_query = st.text_input(
    "Ask about stores, food, parking, jobs, offers..."
)

if st.button("Search"):

    if user_query:

        response = get_response(user_query)

        # Save conversation
        st.session_state.chat_history.append(
            ("You", user_query)
        )

        st.session_state.chat_history.append(
            ("Assistant", response)
        )

# ---------------- CHAT HISTORY ---------------- #

st.subheader("💬 Conversation")
if st.button("🗑 Clear Chat"):

    st.session_state.chat_history = []

    st.rerun()

if len(st.session_state.chat_history) == 0:

    st.info("No conversation yet.")

else:

    for speaker, message in st.session_state.chat_history:

        if speaker == "You":

            st.write(f"👤 {speaker}: {message}")

        else:

            st.success(f"🤖 {speaker}: {message}")

# ---------------- FOOTER ---------------- #

st.divider()

st.caption(
    "Smart Mall AI Assistant | Phase 1 MVP"
)