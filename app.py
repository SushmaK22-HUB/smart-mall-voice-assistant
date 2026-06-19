import os
import streamlit as st

from modules.speech_to_text import listen
from modules.text_to_speech import speak
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
MALL_EXTERIOR = os.path.join(BASE_DIR, "assets", "mall_exterior.jpg")
MALL_INTERIOR = os.path.join(BASE_DIR, "assets", "mall_interior.jpg")

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Smart Mall Voice Assistant",
    page_icon="🛍️",
    layout="wide"
)

st.markdown("""
<style>

/* Background Image */
.stApp {
    background-image: linear-gradient(
        rgba(0,0,0,0.55),
        rgba(0,0,0,0.55)
    ),
    url("https://images.unsplash.com/photo-1519567241046-7f570eee3ce6");
    
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Main text */
h1,h2,h3 {
    color: white !important;
}

.hero p {
    color: #f0f0f0 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(20,20,20,0.75);
    backdrop-filter: blur(10px);
}

/* Buttons */
.stButton > button {
    border-radius: 15px;
    height: 50px;
    border: none;
    background: linear-gradient(
        135deg,
        #ff7b00,
        #ff4d4d
    );
    color: white;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
}

/* Statistics Cards */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.18);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 20px;
    padding: 20px;
}
            
[data-testid="stMetricValue"] {
    color: white !important;
}

[data-testid="stMetricLabel"] {
    color: white !important;
}            

/* Text Input */
input {
    border-radius: 15px !important;
}

/* Hero Banner */
.hero {
    text-align:center;
    padding:40px;
    background:rgba(0,0,0,0.45);
    border-radius:20px;
    margin-bottom:30px;
}

.hero h1 {
    font-size:70px;
    color:white;
    font-weight:bold;
}

.hero p {
    font-size:24px;
    color:#f0f0f0;
}
            
textarea {
    color: black !important;
    background-color: white !important;
}

.stCode {
    color: black !important;
}            
            
div[data-testid="metric-container"] {
    transition: 0.3s;
}

div[data-testid="metric-container"]:hover {
    transform: translateY(-5px);
}            

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<div style="
background: rgba(20,20,20,0.75);
padding:30px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.1);
text-align:center;
">

<h1 style="color:#ff7b00;">
🎙️ Smart Mall Voice Assistant
</h1>

<h3 style="color:white;">
Assistant Online
</h3>

<p style="color:#cccccc;">
Find stores, restaurants, offers, jobs and navigation using voice commands.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("## ⚡ Quick Actions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("🏬 Find Store", use_container_width=True)

with col2:
    st.button("🍔 Food Court", use_container_width=True)

with col3:
    st.button("🎁 Offers", use_container_width=True)

with col4:
    st.button("💼 Jobs", use_container_width=True)

st.markdown("## 🏬 Popular Stores")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="
    background: rgba(255,255,255,0.12);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    font-weight:bold;
    ">
    🍎 Apple Store
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
    background: rgba(255,255,255,0.12);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    font-weight:bold;
    ">
    👟 Nike
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
    background: rgba(255,255,255,0.12);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    font-weight:bold;
    ">
    👗 Zara
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="
    background: rgba(255,255,255,0.12);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    font-weight:bold;
    ">
    ☕ Starbucks
    </div>
    """, unsafe_allow_html=True)   

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
st.markdown("""
<div style="
background:white;
color:black;
padding:15px;
border-radius:10px;
font-weight:bold;
text-align:center;
">
🏬 Welcome to Smart Mall. Search stores, restaurants, offers, events and navigate floors instantly.
</div>
""", unsafe_allow_html=True)

st.subheader("📊 Mall Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🛍 Stores",
        len(get_all_stores().splitlines()) - 1
    )

with col2:
    st.metric(
        "🍔 Food Outlets",
        len(get_all_food().splitlines()) - 1
    )

with col3:
    st.metric(
        "🔍 Searches",
        st.session_state.search_count
    )

# ---------------- QUICK SERVICES ---------------- #
st.subheader("🔥 Today's Top Offers")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
    background:white;
    color:black;
    padding:15px;
    border-radius:10px;
    text-align:center;
    ">
    👖 Levi's - Flat 50% Off
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
    background:white;
    color:black;
    padding:15px;
    border-radius:10px;
    text-align:center;
    ">
    🍔 KFC - Buy 1 Get 1 Free
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
    background:white;
    color:black;
    padding:15px;
    border-radius:10px;
    text-align:center;
    ">
    👟 Nike Summer Sale
    </div>
    """, unsafe_allow_html=True)

st.divider()    
st.subheader("⚡ Quick Services")
st.subheader("⭐ Popular Stores")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="
    background:white;
    color:black;
    padding:15px;
    border-radius:10px;
    text-align:center;
    font-weight:bold;
    ">
    👟 Nike
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
    background:white;
    color:black;
    padding:15px;
    border-radius:10px;
    text-align:center;
    font-weight:bold;
    ">
    👗 Zara
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
    background:white;
    color:black;
    padding:15px;
    border-radius:10px;
    text-align:center;
    font-weight:bold;
    ">
    📱 Apple Store
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="
    background:white;
    color:black;
    padding:15px;
    border-radius:10px;
    text-align:center;
    font-weight:bold;
    ">
    ☕ Starbucks
    </div>
    """, unsafe_allow_html=True)


if st.button("🍔 View Food Outlets"):
    st.text_area(
        "Food Outlets",
        get_all_food(),
        height=250
    )

if st.button("📋 View All Stores"):

    st.subheader("🛍 Store Directory")

    stores_text = get_all_stores()

    st.text_area(
    "Store Directory",
    stores_text,
    height=300
)

if st.button("💼 View Jobs"):
    st.text_area(
        "Available Jobs",
        get_jobs(),
        height=250
    )

if st.button("🎁 View Offers"):
    st.text_area(
        "Current Offers",
        get_offers(),
        height=250
    )

if st.button("🎉 View Events"):
    st.text_area(
        "Upcoming Events",
        get_events(),
        height=250
    )

if st.button("🚨 Emergency Information"):
    st.text_area(
        "Emergency Information",
        get_emergency(),
        height=250
    )
st.divider()
st.image(
    MALL_INTERIOR,
    width=700
)    
st.subheader("📸 Mall Gallery")

col1, col2 = st.columns(2)

with col1:
    st.image(MALL_EXTERIOR)

with col2:
    st.image(MALL_INTERIOR)

# ---------------- FLOOR MAPS ---------------- #
st.divider()
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

st.markdown("---")

st.markdown("""
<div style="
background: rgba(20,20,20,0.75);
padding:25px;
border-radius:20px;
border:1px solid rgba(255,123,0,0.3);
text-align:center;
margin-bottom:20px;
">

<h2 style="color:#ff7b00;">
🎙️ AI Voice Assistant
</h2>

<p style="color:white;">
Assistant Online
</p>

<p style="color:#cccccc;">
Ask about stores, food, jobs, offers, events and mall navigation.
</p>

</div>
""", unsafe_allow_html=True)

if st.button("🎙️ Start Voice Assistant", use_container_width=True):

    st.write("Listening...")

    user_text = listen()

    st.markdown(
    f"""
    <div style="
        background: rgba(255,255,255,0.12);
        color:white;
        padding:18px;
        border-radius:15px;
        font-size:18px;
        margin-bottom:12px;
        border-left:4px solid #ff7b00;
    ">
    <b>🎤 You Said</b><br><br>
    {user_text}
    </div>
    """,
    unsafe_allow_html=True
    )

    response = get_response(user_text)

    speak(response)

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

    st.markdown(
f"""
<div style="
    background: rgba(255,123,0,0.15);
    color:white;
    padding:18px;
    border-radius:15px;
    font-size:18px;
    border-left:4px solid #ff7b00;
    margin-top:10px;
">
<b>🤖 Assistant</b><br><br>
{response}
</div>
""",
unsafe_allow_html=True
)

# ---------------- TEXT SEARCH ---------------- #

st.divider()

st.markdown("""
<div style="
background: rgba(20,20,20,0.75);
padding:25px;
border-radius:20px;
border:1px solid rgba(255,123,0,0.3);
text-align:center;
margin-bottom:20px;
">

<h2 style="color:#ff7b00;">
📍 Smart Mall Directory
</h2>

<p style="color:white;">
Find stores, food outlets, offers, parking and services instantly.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("### 💡 Quick Suggestions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Nike"):
        st.text_area(
            "Nike Result",
            get_response("Nike"),
            height=120
        )

with col2:
    if st.button("KFC"):
        st.text_area(
            "KFC Result",
            get_response("KFC"),
            height=120
        )

with col3:
    if st.button("Parking"):
        st.text_area(
            "Parking Result",
            get_response("Parking"),
            height=120
        )

with col4:
    if st.button("Offers"):
        st.text_area(
            "Offers Result",
            get_response("Offers"),
            height=120
        )

user_query = st.text_input(
    "Ask about stores, food, parking, jobs, offers..."
)

if st.button("🔍 Search Directory", use_container_width=True):

    if user_query:

        response = get_response(user_query)

        speak(response)

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

        st.markdown(
f"""
<div style="
background: rgba(255,255,255,0.12);
color:white;
padding:20px;
border-radius:15px;
border-left:4px solid #ff7b00;
font-size:18px;
margin-top:15px;
">
<b>🔍 Search Result</b><br><br>
{response}
</div>
""",
unsafe_allow_html=True
)


# ---------------- AUTO FLOOR MAP ---------------- #

if st.session_state.selected_map:

    st.subheader("📍 Recommended Floor Map")

    st.image(
        st.session_state.selected_map,
        use_container_width=True
    )
# ---------------- CHAT HISTORY ---------------- #

st.divider()
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

# Display conversation

if len(st.session_state.chat_history) == 0:

    st.info("No conversation yet.")

else:

    for speaker, message in st.session_state.chat_history:

        if speaker == "You":

            st.markdown(
                f"""
                <div style="
                    background-color:white;
                    color:black;
                    padding:10px;
                    border-radius:10px;
                    margin:5px 0;
                ">
                👤 {speaker}: {message}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div style="
                    background-color:white;
                    color:black;
                    padding:10px;
                    border-radius:10px;
                    margin:5px 0;
                ">
                🤖 {speaker}: {message}
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- SEARCH ANALYTICS ---------------- #

st.subheader("📈 Search Analytics")

st.metric(
    label="Total Searches",
    value=st.session_state.search_count
)            

# ---------------- FOOTER ---------------- #

st.divider()

st.markdown("""
<div style="
background: rgba(255,255,255,0.15);
padding: 20px;
border-radius: 15px;
text-align: center;
margin-top: 20px;
">

<h3 style="color:white;">
🛍️ Smart Mall AI Assistant
</h3>

<p style="color:white;">
Developed using Python, Streamlit, Voice Recognition and AI Search
</p>

<p style="color:white;">
Phase 3 MVP
</p>

</div>
""", unsafe_allow_html=True)