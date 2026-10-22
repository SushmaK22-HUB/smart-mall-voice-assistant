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
    get_emergency,
    get_stores_by_category,
    get_navigation
)

# ---------------- SESSION STATE ---------------- #

if "selected_map" not in st.session_state:
    st.session_state.selected_map = None

if "search_count" not in st.session_state:
    st.session_state.search_count = 0

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- ASSET PATHS ---------------- #

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GROUND_FLOOR_PATH = os.path.join(BASE_DIR, "assets", "ground_floor.jpg")
FIRST_FLOOR_PATH = os.path.join(BASE_DIR, "assets", "first_floor.jpg")
SECOND_FLOOR_PATH = os.path.join(BASE_DIR, "assets", "second_floor.jpg")
THIRD_FLOOR_PATH = os.path.join(BASE_DIR, "assets", "third_floor.jpg")

# ---------------- PAGE CONFIG & STITCH STYLING ---------------- #

st.set_page_config(
    page_title="Smart Mall AI Voice Assistant",
    page_icon="🛍️",
    layout="wide"
)

st.markdown("""
<style>
/* Clean High-Contrast Dark Theme */
.stApp {
    background: radial-gradient(circle at 50% 10%, #1e222d 0%, #0d0f14 100%);
    color: #ffffff !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Force All Headings to Pure White */
h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
    font-weight: 700 !important;
    letter-spacing: -0.5px;
}

/* Force All Text Elements to High-Contrast Bright White */
p, span, label, div {
    color: #ffffff;
}

/* Stitch Card Containers */
.stitch-card {
    background: rgba(24, 28, 38, 0.9);
    border: 1px solid rgba(255, 123, 0, 0.35);
    border-radius: 18px;
    padding: 24px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.stitch-card:hover {
    border-color: #ff7b00;
    transform: translateY(-2px);
}

/* Orange Gradient Primary Buttons */
.stButton > button {
    background: linear-gradient(135deg, #ff7b00 0%, #ff5500 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    height: 48px !important;
    box-shadow: 0 4px 15px rgba(255, 123, 0, 0.4) !important;
    transition: all 0.25s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 6px 22px rgba(255, 123, 0, 0.6) !important;
}

/* Text Input Styling with Bright White Text */
.stTextInput > div > div > input {
    background-color: rgba(20, 24, 33, 0.95) !important;
    color: #ffffff !important;
    font-size: 16px !important;
    border: 1.5px solid rgba(255, 123, 0, 0.4) !important;
    border-radius: 14px !important;
    padding: 12px 16px !important;
}

.stTextInput > div > div > input:focus {
    border-color: #ff7b00 !important;
    box-shadow: 0 0 12px rgba(255, 123, 0, 0.5) !important;
}

/* Tabs Styling with Crisp Bright Text */
button[data-baseweb="tab"] {
    color: #ffffff !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #ff7b00 !important;
    border-bottom-color: #ff7b00 !important;
}

/* Expanders with High Contrast */
.streamlit-expanderHeader {
    background-color: rgba(26, 30, 41, 0.85) !important;
    color: #ffffff !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    border: 1px solid rgba(255, 123, 0, 0.25) !important;
    border-radius: 12px !important;
}

/* Sidebar Dark Glass */
section[data-testid="stSidebar"] {
    background-color: #0b0d12 !important;
    border-right: 1px solid rgba(255, 123, 0, 0.25) !important;
}

/* Status Badge */
.status-pill {
    display: inline-flex;
    align-items: center;
    background: rgba(0, 230, 118, 0.18);
    color: #00ff88 !important;
    border: 1px solid rgba(0, 230, 118, 0.4);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ---------------- APPLICATION HEADER ---------------- #

st.markdown("""
<div style="text-align: center; margin-bottom: 25px;">
    <h1 style="color: #ff7b00; font-size: 44px; margin-bottom: 8px;">
        🎙️ Smart Mall AI Assistant
    </h1>
    <span class="status-pill">
        🟢 Assistant Online & Ready
    </span>
    <p style="color: #ffffff; font-size: 16px; margin-top: 10px; font-weight: 500;">
        Speak or type to navigate stores, food outlets, offers, events, and floor maps.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- HERO VOICE ASSISTANT SECTION ---------------- #

st.markdown("""
<div class="stitch-card" style="text-align: center; margin-bottom: 25px; border: 2px solid rgba(255,123,0,0.4);">
    <h3 style="color: #ffffff; margin-bottom: 6px; font-size: 24px;">
        Tap Below to Speak with AI
    </h3>
    <p style="color: #ffffff; font-size: 16px; margin-bottom: 20px;">
        Try saying: <b style="color: #ff9d3b;">"Where is Nike?"</b>, <b style="color: #ff9d3b;">"Food court on third floor"</b>, or <b style="color: #ff9d3b;">"Are pets allowed?"</b>
    </p>
</div>
""", unsafe_allow_html=True)

col_v1, col_v2, col_v3 = st.columns([1, 2, 1])
with col_v2:
    speak_button = st.button("🎙️ TAP TO SPEAK", use_container_width=True)

if speak_button:
    with st.spinner("Listening to your voice..."):
        user_text = listen()

    # Immediate Question Display
    st.markdown(f"""
    <div class="stitch-card" style="border-left: 5px solid #ff7b00; margin-top: 20px; padding: 18px;">
        <span style="color: #ff7b00; font-weight: 800; font-size: 14px; text-transform: uppercase;">🎤 You Asked</span>
        <p style="font-size: 19px; color: #ffffff; margin-top: 6px; margin-bottom: 0; font-weight: 600;">{user_text}</p>
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("Finding information..."):
        response = get_response(user_text)

    # Automatic Floor Map Detection
    st.session_state.selected_map = None
    if "first floor" in response.lower():
        st.session_state.selected_map = FIRST_FLOOR_PATH
    elif "second floor" in response.lower():
        st.session_state.selected_map = SECOND_FLOOR_PATH
    elif "third floor" in response.lower():
        st.session_state.selected_map = THIRD_FLOOR_PATH
    elif "ground floor" in response.lower():
        st.session_state.selected_map = GROUND_FLOOR_PATH

    # Analytics increment & History logging
    st.session_state.search_count += 1
    st.session_state.chat_history.append(("You", user_text))
    st.session_state.chat_history.append(("Assistant", response))

    # Instant Display of Assistant Response (Zero Delay!)
    st.markdown(f"""
    <div class="stitch-card" style="border-left: 5px solid #00e676; margin-top: 15px; padding: 18px;">
        <span style="color: #00e676; font-weight: 800; font-size: 14px; text-transform: uppercase;">🤖 Assistant Reply</span>
        <div style="font-size: 18px; color: #ffffff; margin-top: 6px; white-space: pre-wrap; line-height: 1.6;">{response}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.selected_map and os.path.exists(st.session_state.selected_map):
        st.markdown("<h4 style='color:#ff7b00; text-align:center; margin-top:20px;'>📍 Recommended Floor Map</h4>", unsafe_allow_html=True)
        st.image(st.session_state.selected_map, use_container_width=True)

    # Background audio speech (Never freezes the UI!)
    speak(response)

st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

# ---------------- SIDEBAR: UTILITIES, ANALYTICS & HISTORY ---------------- #

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding-bottom: 15px;">
        <h2 style="color: #ff7b00; margin-bottom: 4px;">🏬 Smart Mall</h2>
        <span class="status-pill">Interactive Kiosk</span>
    </div>
    """, unsafe_allow_html=True)

    # Emergency Quick Button
    if st.button("🚨 Emergency Assistance", use_container_width=True):
        st.error(get_emergency())

    st.markdown("<hr style='border: 1px solid rgba(255,123,0,0.25);'>", unsafe_allow_html=True)

    # Analytics Counter
    st.markdown("### 📈 Live Analytics")
    st.metric(label="Total Interactions", value=st.session_state.search_count)

    st.markdown("<hr style='border: 1px solid rgba(255,123,0,0.25);'>", unsafe_allow_html=True)

    # Conversation History
    st.markdown("### 💬 Chat History")
    if len(st.session_state.chat_history) == 0:
        st.markdown("<span style='color: #ffffff;'>No conversations recorded yet.</span>", unsafe_allow_html=True)
    else:
        for speaker, message in st.session_state.chat_history[-6:]:
            if speaker == "You":
                st.markdown(f"**👤 You:** <span style='color: #ffffff;'>{message}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"**🤖 AI:** <span style='color: #ffffff;'>{message}</span>", unsafe_allow_html=True)

        col_h1, col_h2 = st.columns(2)
        with col_h1:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()
        with col_h2:
            chat_text = "\n".join([f"{s}: {m}" for s, m in st.session_state.chat_history])
            st.download_button("📥 Save", data=chat_text, file_name="chat_history.txt", use_container_width=True)

    st.markdown("<hr style='border: 1px solid rgba(255,123,0,0.25);'>", unsafe_allow_html=True)
    st.markdown("<p style='color: #ffffff; font-size: 12px;'>Final Year B.E. AI & Data Science Project<br>Stanley College</p>", unsafe_allow_html=True)

# ---------------- MAIN CONTENT: 3 STITCH TABS ---------------- #

tab_home, tab_dir, tab_nav = st.tabs([
    "🏠 Home & Highlights", 
    "📋 Mall Directory", 
    "🗺️ Floor Navigation"
])

# ================= TAB 1: HOME & HIGHLIGHTS ================= #
with tab_home:
    st.markdown("<h3 style='color:#ff7b00; margin-top:15px;'>🔥 Today's Top Offers</h3>", unsafe_allow_html=True)
    col_o1, col_o2, col_o3 = st.columns(3)
    with col_o1:
        st.markdown("""
        <div class="stitch-card" style="text-align: center; height: 130px;">
            <h4 style="color: #ff7b00; margin-bottom: 5px;">🔥 Flat 50% OFF</h4>
            <b style="color: #ffffff; font-size: 17px;">Levi's</b><br>
            <span style="color:#ffffff; font-size:14px;">Summer Fashion Sale</span>
        </div>
        """, unsafe_allow_html=True)
    with col_o2:
        st.markdown("""
        <div class="stitch-card" style="text-align: center; height: 130px;">
            <h4 style="color: #ff7b00; margin-bottom: 5px;">🍔 BOGO Deal</h4>
            <b style="color: #ffffff; font-size: 17px;">Burger King</b><br>
            <span style="color:#ffffff; font-size:14px;">Buy 1 Get 1 Burger Free</span>
        </div>
        """, unsafe_allow_html=True)
    with col_o3:
        st.markdown("""
        <div class="stitch-card" style="text-align: center; height: 130px;">
            <h4 style="color: #ff7b00; margin-bottom: 5px;">👟 Mega Sale</h4>
            <b style="color: #ffffff; font-size: 17px;">Nike</b><br>
            <span style="color:#ffffff; font-size:14px;">Exclusive Sportswear Deals</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3 style='color:#ff7b00; margin-top:25px;'>⭐ Popular Stores</h3>", unsafe_allow_html=True)
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    with col_s1:
        st.markdown("""
        <div class="stitch-card" style="text-align: center;">
            <h4 style="color: #ffffff;">🍎 Apple</h4>
            <span style="color: #ffffff; font-size: 14px; font-weight: 500;">Second Floor • Tech</span>
        </div>
        """, unsafe_allow_html=True)
    with col_s2:
        st.markdown("""
        <div class="stitch-card" style="text-align: center;">
            <h4 style="color: #ffffff;">👟 Nike</h4>
            <span style="color: #ffffff; font-size: 14px; font-weight: 500;">Second Floor • Sports</span>
        </div>
        """, unsafe_allow_html=True)
    with col_s3:
        st.markdown("""
        <div class="stitch-card" style="text-align: center;">
            <h4 style="color: #ffffff;">👗 Zara</h4>
            <span style="color: #ffffff; font-size: 14px; font-weight: 500;">First Floor • Fashion</span>
        </div>
        """, unsafe_allow_html=True)
    with col_s4:
        st.markdown("""
        <div class="stitch-card" style="text-align: center;">
            <h4 style="color: #ffffff;">☕ Starbucks</h4>
            <span style="color: #ffffff; font-size: 14px; font-weight: 500;">Ground Floor • Café</span>
        </div>
        """, unsafe_allow_html=True)

# ================= TAB 2: DIRECTORY ================= #
with tab_dir:
    st.markdown("<h3 style='color:#ff7b00; margin-top:15px;'>🔍 Search Mall Directory</h3>", unsafe_allow_html=True)
    user_query = st.text_input("Type store, food, parking, offer, or facility...", key="dir_search_input")
    if st.button("Search Directory", use_container_width=True):
        if user_query.strip():
            dir_res = get_response(user_query)
            st.session_state.search_count += 1
            st.session_state.chat_history.append(("You", user_query))
            st.session_state.chat_history.append(("Assistant", dir_res))
            
            # Display result immediately
            st.markdown(f"""
            <div class="stitch-card" style="border-left: 5px solid #ff7b00; margin-top: 15px;">
                <h4 style="color:#ff7b00; margin-bottom:6px;">Search Results</h4>
                <div style="white-space: pre-wrap; font-size: 17px; color: #ffffff; line-height: 1.6;">{dir_res}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Speak in background
            speak(dir_res)

    st.markdown("<h4 style='color:#ffffff; margin-top:25px;'>📂 Browse by Category</h4>", unsafe_allow_html=True)
    cat_col1, cat_col2, cat_col3, cat_col4 = st.columns(4)
    with cat_col1:
        if st.button("👗 Fashion Stores", use_container_width=True):
            st.success(get_stores_by_category("Fashion"))
    with cat_col2:
        if st.button("🍔 Food Outlets", use_container_width=True):
            st.success(get_all_food())
    with cat_col3:
        if st.button("📱 Electronics", use_container_width=True):
            st.success(get_stores_by_category("Electronics"))
    with cat_col4:
        if st.button("💼 Career Openings", use_container_width=True):
            st.success(get_jobs())

    with st.expander("📋 View Complete Store Directory"):
        st.markdown(f"<div style='color: #ffffff; font-size: 15px; white-space: pre-wrap;'>{get_all_stores()}</div>", unsafe_allow_html=True)
    with st.expander("🎉 View Upcoming Mall Events"):
        st.markdown(f"<div style='color: #ffffff; font-size: 15px; white-space: pre-wrap;'>{get_events()}</div>", unsafe_allow_html=True)

# ================= TAB 3: NAVIGATION ================= #
with tab_nav:
    st.markdown("<h3 style='color:#ff7b00; margin-top:15px;'>🗺️ Interactive Floor Navigation</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#ffffff; font-size:15px;'>Select a floor to view its layout and store locations.</p>", unsafe_allow_html=True)

    f_col1, f_col2, f_col3, f_col4 = st.columns(4)
    with f_col1:
        if st.button("🏢 Ground Floor", use_container_width=True):
            st.session_state.selected_map = GROUND_FLOOR_PATH
    with f_col2:
        if st.button("⬆️ First Floor", use_container_width=True):
            st.session_state.selected_map = FIRST_FLOOR_PATH
    with f_col3:
        if st.button("⬆️ Second Floor", use_container_width=True):
            st.session_state.selected_map = SECOND_FLOOR_PATH
    with f_col4:
        if st.button("⬆️ Third Floor", use_container_width=True):
            st.session_state.selected_map = THIRD_FLOOR_PATH

    # Display Map
    if st.session_state.selected_map and os.path.exists(st.session_state.selected_map):
        st.image(st.session_state.selected_map, use_container_width=True)
    else:
        if os.path.exists(GROUND_FLOOR_PATH):
            st.image(GROUND_FLOOR_PATH, caption="Ground Floor (Default View)", use_container_width=True)
        else:
            st.info("Floor map image is currently loading.")

    st.markdown("<h4 style='color:#ff7b00; margin-top:20px;'>🧭 Direct Store Routing</h4>", unsafe_allow_html=True)
    nav_store_input = st.text_input("Enter a store name for route directions (e.g. Nike, Zara, KFC):", key="nav_input")
    if st.button("Get Navigation Route", use_container_width=True):
        if nav_store_input.strip():
            nav_directions = get_navigation(nav_store_input)
            st.success(nav_directions)
            speak(nav_directions)

# ---------------- FOOTER ---------------- #

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 20px; border-top: 1px solid rgba(255,123,0,0.25); color: #ffffff; font-size: 13px;">
    Smart Mall AI Voice Assistant • Built with Python, Streamlit & Google Gemini • Final Year Internship Project
</div>
""", unsafe_allow_html=True)