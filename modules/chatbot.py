import os
import re
import warnings
warnings.filterwarnings("ignore")

import google.generativeai as genai

# Safely load dotenv only if installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

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

# Read API key from environment variable or set your key here
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

model = None
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        print("Gemini initialization warning:", e)


def get_response(user_input):
    if not user_input or not user_input.strip():
        return "I'm listening! You can ask about stores, restaurants, offers, parking, or navigation."

    query = user_input.strip()
    query_lower = query.lower()

    # 1. Emergency & Help
    if any(word in query_lower for word in ["emergency", "fire", "security", "first aid", "help desk"]):
        return get_emergency()

    # 2. Navigation & Directions
    if any(word in query_lower for word in ["reach", "navigate", "route to", "way to", "how to go", "direction"]):
        nav_result = get_navigation(query)
        if "unavailable" not in nav_result:
            return nav_result

    # 3. Floor-Wise Food & Store Searches
    if "ground floor" in query_lower and ("food" in query_lower or "restaurant" in query_lower or "cafe" in query_lower):
        return get_food_by_floor("Ground Floor")
    if "first floor" in query_lower and ("food" in query_lower or "restaurant" in query_lower or "cafe" in query_lower):
        return get_food_by_floor("First Floor")
    if "second floor" in query_lower and ("food" in query_lower or "restaurant" in query_lower or "cafe" in query_lower):
        return get_food_by_floor("Second Floor")
    if "third floor" in query_lower and ("food" in query_lower or "restaurant" in query_lower or "cafe" in query_lower):
        return get_food_by_floor("Third Floor")

    if "ground floor" in query_lower:
        return get_stores_by_floor("Ground Floor")
    if "first floor" in query_lower:
        return get_stores_by_floor("First Floor")
    if "second floor" in query_lower:
        return get_stores_by_floor("Second Floor")
    if "third floor" in query_lower:
        return get_stores_by_floor("Third Floor")

    # 4. Parking Info
    if any(word in query_lower for word in ["park", "parking", "car", "vehicle"]):
        return get_parking_info()

    # 5. Offers & Discounts
    if any(word in query_lower for word in ["offer", "discount", "deal", "sale"]):
        return get_offers()

    # 6. Jobs & Careers
    if any(word in query_lower for word in ["job", "career", "vacancy", "hiring", "opening"]):
        return get_jobs()

    # 7. Events & Movies
    if any(word in query_lower for word in ["event", "movie", "cinema", "show", "activity"]):
        return get_events()

    # 8. All Directory Lists
    if "all stores" in query_lower or "store directory" in query_lower:
        return get_all_stores()
    if "all food" in query_lower or "food court" in query_lower or "restaurants" in query_lower:
        return get_all_food()
    if "all facilities" in query_lower:
        return get_all_facilities()

    # 9. Store Categories
    categories = ["fashion", "sportswear", "electronics", "footwear", "gaming", "entertainment", "cafe"]
    for cat in categories:
        if cat in query_lower:
            return get_stores_by_category(cat)

    # 10. Specific Store Search
    store_result = search_store(query)
    if store_result:
        return store_result

    # 11. Specific Food Search
    food_result = search_food(query)
    if food_result:
        return food_result

    # 12. Facilities (Washroom, ATM, Elevator, etc.)
    facility_result = search_facility(query)
    if facility_result:
        return facility_result

    # 13. General AI Fallback with Gemini
    if model:
        try:
            prompt = f"""
            You are a polite, helpful Smart Mall Assistant.
            Answer this mall visitor's question briefly in 1 to 2 clear sentences.
            If it is completely unrelated to a shopping mall, guide them politely to mall services.
            Visitor question: {query}
            """
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text.strip()
        except Exception as e:
            print("Gemini fallback error:", e)

    # Friendly default if AI is unavailable or offline
    return (
        "I couldn't find an exact match in our mall directory. "
        "You can ask me about stores (e.g., 'Where is Nike?'), food outlets, "
        "today's offers, parking, or floor navigation."
    )


if __name__ == "__main__":
    print("🛍️ Smart Mall Assistant Terminal Test")
    print("Type 'exit' to quit.\n")
    while True:
        user = input("You: ")
        if user.lower() == "exit":
            break
        print("Assistant:\n", get_response(user), "\n")