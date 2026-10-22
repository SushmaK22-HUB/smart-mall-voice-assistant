import os
import re
import warnings
warnings.filterwarnings("ignore")

import google.generativeai as genai

# Explicitly load .env from project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(BASE_DIR, ".env")

if os.path.exists(env_path):
    try:
        from dotenv import load_dotenv
        load_dotenv(env_path)
    except Exception:
        pass
    if not os.getenv("GEMINI_API_KEY"):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("GEMINI_API_KEY="):
                    os.environ["GEMINI_API_KEY"] = line.strip().split("=", 1)[1].strip("'\" ")

from modules.search_engine import (
    search_store,
    search_facility,
    search_food,
    get_parking_info,
    get_offers,
    get_jobs,
    get_events,
    get_emergency,
    get_all_stores,
    get_all_facilities,
    get_all_food,
    get_stores_by_floor,
    get_food_by_floor,
    get_stores_by_category,
    get_navigation
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

model = None
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-3.8-flash")
    except Exception as e:
        print("Gemini initialization warning:", e)


def get_response(user_input):
    if not user_input or not user_input.strip():
        return "I'm listening! You can ask about stores, restaurants, offers, parking, or navigation."

    query = user_input.strip()
    query_lower = query.lower()

    # 1. Mall Operating Hours & Timings
    if any(phrase in query_lower for phrase in ["timing", "timings", "hours", "close time", "closing time", "opening time", "when does the mall open", "when does the mall close"]):
        return (
            "🕒 Smart Mall Operating Hours:\n"
            "• Monday to Sunday: 10:00 AM – 10:00 PM\n"
            "• Food Court & Entertainment: Open until 11:30 PM\n"
            "• Hypermarket (Ground Floor): Opens early at 9:00 AM"
        )

    # 2. Pet Policy (Instant Smart Response - Never Fails)
    if "pet" in query_lower or "dog" in query_lower or "animal" in query_lower:
        return (
            "🐾 Pet Policy:\n"
            "Only certified service animals are permitted inside the mall. "
            "Regular pets are not allowed for the safety and comfort of all visitors."
        )

    # 3. Accessibility & Wheelchair Assistance
    if "wheelchair" in query_lower or "handicap" in query_lower or "elderly" in query_lower or "disabled" in query_lower:
        return (
            "♿ Accessibility Services:\n"
            "Complimentary wheelchair assistance is available at the Ground Floor Help Desk "
            "and all main entrances. Elevators are located in every wing."
        )

    # 4. Lost and Found & Child Safety
    if any(phrase in query_lower for phrase in ["lost child", "lost bag", "lost wallet", "lost phone", "lost and found", "lost item"]):
        return (
            "🚨 Lost & Found Assistance:\n"
            "Please report immediately to the Central Security Desk on the Ground Floor "
            "or contact Security Assistance from the sidebar for immediate broadcast."
        )

    # 5. Wi-Fi & Mobile Charging
    if "wifi" in query_lower or "internet" in query_lower:
        return "📶 Free Mall Wi-Fi is available! Connect to 'SmartMall_Guest_WiFi' and verify via OTP on your browser."
    if "charge" in query_lower or "charging" in query_lower:
        return "⚡ EV Charging stations are located in Basement Parking (B1). Mobile charging kiosks are available on First and Second Floors near the escalators."

    # 6. Emergency & Security
    if any(word in query_lower for word in ["emergency", "fire", "security", "first aid", "help desk"]):
        return get_emergency()

    # 7. Direct Navigation & Directions
    if any(word in query_lower for word in ["reach", "navigate", "route to", "way to", "how to go", "direction"]):
        nav_result = get_navigation(query)
        if "unavailable" not in nav_result:
            return nav_result

    # 8. Floor-Wise Food & Store Searches
    if "ground floor" in query_lower and any(w in query_lower for w in ["food", "restaurant", "cafe"]):
        return get_food_by_floor("Ground Floor")
    if "first floor" in query_lower and any(w in query_lower for w in ["food", "restaurant", "cafe"]):
        return get_food_by_floor("First Floor")
    if "second floor" in query_lower and any(w in query_lower for w in ["food", "restaurant", "cafe"]):
        return get_food_by_floor("Second Floor")
    if "third floor" in query_lower and any(w in query_lower for w in ["food", "restaurant", "cafe"]):
        return get_food_by_floor("Third Floor")

    if "ground floor" in query_lower:
        return get_stores_by_floor("Ground Floor")
    if "first floor" in query_lower:
        return get_stores_by_floor("First Floor")
    if "second floor" in query_lower:
        return get_stores_by_floor("Second Floor")
    if "third floor" in query_lower:
        return get_stores_by_floor("Third Floor")

    # Birthday & Event Celebrations
    if any(word in query_lower for word in ["birthday", "party", "celebrate", "celebration", "gathering"]):
        return (
            "🎉 Birthday & Party Celebrations:\n"
            "Yes! You can celebrate at our Fourth Floor Food Court or book party zones at "
            "the Gaming Zone (Fourth Floor) and select restaurants. Contact the Central Help Desk for group table reservations!"
        )

    # 9. Parking Information
    if any(word in query_lower for word in ["park", "parking", "car", "vehicle", "slot", "bike"]):
        return get_parking_info()

    # 10. Offers & Discounts
    # Gift Suggestions & Shopping Ideas
    if any(word in query_lower for word in ["gift", "present", "souvenir", "recommendation"]):
        return (
            "🎁 Great Gift Ideas at Smart Mall:\n"
            "• Perfumes & Cosmetics: Nykaa, The Body Shop (Ground Floor)\n"
            "• Tech & Gadgets: Apple Store, Croma (Second Floor)\n"
            "• Fashion & Watches: Zara, Titan, Fossil (First Floor)\n"
            "• Jewelry & Luxury: Tanishq (Ground Floor)"
        )

    # 11. Jobs & Careers
    if any(word in query_lower for word in ["job", "career", "vacancy", "hiring", "job opening", "job openings"]):
        return get_jobs()

    # 12. Events & Movies
    if any(word in query_lower for word in ["event", "movie", "cinema", "show", "activity"]):
        return get_events()

    # 13. All Directory Lists
    if "all stores" in query_lower or "store directory" in query_lower:
        return get_all_stores()
    if "all food" in query_lower or "food court" in query_lower or "restaurants" in query_lower:
        return get_all_food()
    if "all facilities" in query_lower:
        return get_all_facilities()

    # 14. Store Categories
    categories = ["fashion", "sportswear", "electronics", "footwear", "gaming", "entertainment", "cafe"]
    for cat in categories:
        if cat in query_lower:
            return get_stores_by_category(cat)

    # 15. Specific Store Search
    store_result = search_store(query)
    if store_result:
        return store_result

    # 16. Specific Food Search
    food_result = search_food(query)
    if food_result:
        return food_result

    # 17. Facilities
    facility_result = search_facility(query)
    if facility_result:
        return facility_result

    # 18. Live Gemini AI Fallback
    if GEMINI_API_KEY:
        try:
            genai.configure(api_key=GEMINI_API_KEY)
            active_model = genai.GenerativeModel("gemini-3.8-flash")
            prompt = f"""
            You are a polite, helpful Smart Mall Assistant.
            Answer this mall visitor's question briefly in 1 to 2 clear sentences.
            Visitor question: {query}
            """
            response = active_model.generate_content(prompt)
            if response and response.text:
                return response.text.strip()
        except Exception as e:
            print("Gemini fallback note:", e)

    # Default fallback
    return (
        "I couldn't find an exact match in our mall directory. "
        "You can ask me about stores (e.g., 'Where is Nike?'), food outlets, "
        "today's offers, parking, or floor navigation."
    )