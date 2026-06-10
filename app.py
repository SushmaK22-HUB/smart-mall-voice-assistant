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

if "selected_map" not in st.session_state:
    st.session_state.selected_map = None

if "search_count" not in st.session_state:
    st.session_state.search_count = 0    

# ---------------- CHAT HISTORY ---------------- #

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "search_count" not in st.session_state:
    st.session_state.search_count = 0    

# ---------------- PATHS ---------------- #

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGO_PATH = os.path.join(BASE_DIR, "assets", "mall_logo.jpg")
MAP_PATH = os.path.join(BASE_DIR, "assets", "mall_map.jpg")

GROUND_FLOOR_PATH = os.path.join(BASE_DIR, "assets", "ground_floor.jpg")
FIRST_FLOOR_PATH = os.path.join(BASE_DIR, "assets", "first_floor.jpg")
SECOND_FLOOR_PATH = os.path.join(BASE_DIR, "assets", "second_floor.jpg")
THIRD_FLOOR_PATH = os.path.join(BASE_DIR, "assets", "third_floor.jpg")

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

# ---------------- FLOOR MAPS ---------------- #

st.subheader("🗺️ Floor Maps")

col1, col2 = st.columns(2)

with col1:

    if st.button("Ground Floor"):
        st.image(
            GROUND_FLOOR_PATH,
            caption="Ground Floor",
            use_container_width=True
        )

    if st.button("First Floor"):
        st.image(
            FIRST_FLOOR_PATH,
            caption="First Floor",
            use_container_width=True
        )

with col2:

    if st.button("Second Floor"):
        st.image(
            SECOND_FLOOR_PATH,
            caption="Second Floor",
            use_container_width=True
        )

    if st.button("Third Floor"):
        st.image(
            THIRD_FLOOR_PATH,
            caption="Third Floor",
            use_container_width=True
        )


# ---------------- VOICE ASSISTANT ---------------- #

st.subheader("🎤 Voice Assistant")

if st.button("🎤 Speak Now"):

    st.write("Listening...")

    user_text = listen()

    st.success(f"You said: {user_text}")

    response = get_response(user_text)

    st.session_state.selected_map = None

    # Auto floor map
    if "First Floor" in response:
        st.session_state.selected_map = FIRST_FLOOR_PATH

    elif "Second Floor" in response:
        st.session_state.selected_map = SECOND_FLOOR_PATH

    elif "Third Floor" in response:
        st.session_state.selected_map = THIRD_FLOOR_PATH

    elif "Ground Floor" in response:
        st.session_state.selected_map = GROUND_FLOOR_PATH

    # Analytics
    st.session_state.search_count += 1

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
st.subheader("💡 Quick Suggestions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Nike"):
        st.success(get_response("Nike"))

with col2:
    if st.button("KFC"):
        st.success(get_response("KFC"))

with col3:
    if st.button("Parking"):
        st.success(get_response("Parking"))

with col4:
    if st.button("Offers"):
        st.success(get_response("Offers"))

user_query = st.text_input(
    "Ask about stores, food, parking, jobs, offers..."
)

if st.button("Search"):

    if user_query:

        response = get_response(user_query)

        st.session_state.selected_map = None

        # Auto floor map
        if "First Floor" in response:
            st.session_state.selected_map = FIRST_FLOOR_PATH

        elif "Second Floor" in response:
            st.session_state.selected_map = SECOND_FLOOR_PATH

        elif "Third Floor" in response:
            st.session_state.selected_map = THIRD_FLOOR_PATH

        elif "Ground Floor" in response:
            st.session_state.selected_map = GROUND_FLOOR_PATH

        # Analytics
        st.session_state.search_count += 1

        # Save conversation
        st.session_state.chat_history.append(
            ("You", user_query)
        )

        st.session_state.chat_history.append(
            ("Assistant", response)
        )

        st.success(response)


# ---------------- AUTO FLOOR MAP ---------------- #

if st.session_state.selected_map:

    st.subheader("📍 Recommended Floor Map")

    st.image(
        st.session_state.selected_map,
        use_container_width=True
    )
# ---------------- CHAT HISTORY ---------------- #

st.subheader("💬 Conversation")

if st.button("🗑 Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# Create downloadable text
chat_text = ""

for speaker, message in st.session_state.chat_history:
    chat_text += f"{speaker}: {message}\n"

st.download_button(
    label="📥 Download Chat History",
    data=chat_text,
    file_name="mall_chat_history.txt",
    mime="text/plain"
)

# Display conversation

if len(st.session_state.chat_history) == 0:

    st.info("No conversation yet.")

else:

    for speaker, message in st.session_state.chat_history:

        if speaker == "You":

            st.write(f"👤 {speaker}: {message}")

        else:

            st.success(f"🤖 {speaker}: {message}")

# ---------------- SEARCH ANALYTICS ---------------- #

st.subheader("📈 Search Analytics")

st.metric(
    label="Total Searches",
    value=st.session_state.search_count
)            

# ---------------- FOOTER ---------------- #

st.divider()

st.caption(
    "Smart Mall AI Assistant | Phase 1 MVP"
)