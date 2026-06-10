import google.generativeai as genai

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

# ---------------- GEMINI CONFIG ---------------- #

GEMINI_API_KEY = "AIzaSyDUsXj1hbV8CQmKPsXsVadex7JwH77FE5c"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- MAIN RESPONSE FUNCTION ---------------- #

def get_response(user_input):

    user_input_lower = user_input.lower()

    # ---------- FOOD FLOOR SEARCH ---------- #

    if "food on third floor" in user_input_lower:
        return get_food_by_floor("Third Floor")

    if "restaurants on third floor" in user_input_lower:
        return get_food_by_floor("Third Floor")

    if "food court" in user_input_lower:
        return get_food_by_floor("Third Floor")

    # ---------- FLOOR SEARCH ---------- #

    if "stores on first floor" in user_input_lower:
        return get_stores_by_floor("First Floor")

    if "stores in first floor" in user_input_lower:
        return get_stores_by_floor("First Floor")

    if "stores on second floor" in user_input_lower:
        return get_stores_by_floor("Second Floor")

    if "stores in second floor" in user_input_lower:
        return get_stores_by_floor("Second Floor")

    if "stores on third floor" in user_input_lower:
        return get_stores_by_floor("Third Floor")

    if "stores in third floor" in user_input_lower:
        return get_stores_by_floor("Third Floor")

    # ---------- ALL STORES ---------- #

    if "all stores" in user_input_lower or "stores list" in user_input_lower:
        return get_all_stores()

    # ---------- ALL FACILITIES ---------- #

    if "all facilities" in user_input_lower:
        return get_all_facilities()

    # ---------- ALL FOOD ---------- #

    if "all food" in user_input_lower or "food outlets" in user_input_lower:
        return get_all_food()

    # ---------- ALL JOBS ---------- #

    if "all jobs" in user_input_lower:
        return get_jobs()

    # ---------- ALL OFFERS ---------- #

    if "all offers" in user_input_lower:
        return get_offers()

    # ---------- ALL EVENTS ---------- #

    if "all events" in user_input_lower:
        return get_events()
    
    # ---------- CATEGORY SEARCH ---------- #

    if "fashion stores" in user_input_lower:
        return get_stores_by_category("Fashion")

    if "sportswear stores" in user_input_lower:
        return get_stores_by_category("Sportswear")
    
    # ---------- NAVIGATION ---------- #

    if "reach nike" in user_input_lower:
        return get_navigation("Nike")

    if "route to nike" in user_input_lower:
        return get_navigation("Nike")

    if "navigate to nike" in user_input_lower:
        return get_navigation("Nike")

    if "reach zara" in user_input_lower:
        return get_navigation("Zara")

    if "route to zara" in user_input_lower:
        return get_navigation("Zara")

    if "navigate to zara" in user_input_lower:
        return get_navigation("Zara")

    # ---------- STORE SEARCH ---------- #

    store_result = search_store(user_input)

    if store_result:
        return store_result

    # ---------- FACILITY SEARCH ---------- #

    facility_result = search_facility(user_input)

    if facility_result:
        return facility_result

    # ---------- FOOD SEARCH ---------- #

    food_result = search_food(user_input)

    if food_result:
        return food_result

    # ---------- PARKING ---------- #

    if "parking" in user_input_lower:
        return get_parking_info()

    # ---------- OFFERS ---------- #

    if "offer" in user_input_lower:
        return get_offers()

    # ---------- JOBS ---------- #

    if "job" in user_input_lower:
        return get_jobs()

    # ---------- EVENTS ---------- #

    if "event" in user_input_lower:
        return get_events()

    # ---------- EMERGENCY ---------- #

    if (
        "emergency" in user_input_lower
        or "exit" in user_input_lower
        or "fire" in user_input_lower
    ):
        return get_emergency()
    

    # ---------- GEMINI FALLBACK ---------- #

    try:

        response = model.generate_content(
            f"""
            You are a Smart Mall Assistant.

            Rules:
            - Keep answers short.
            - Focus only on mall-related help.
            - Be polite.
            - Do not give long explanations.

            User Question:
            {user_input}
            """
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# ---------------- TERMINAL TEST ---------------- #

if __name__ == "__main__":

    print("🛍️ Smart Mall AI Assistant Started")
    print("Type 'exit' to stop\n")

    while True:

        user = input("You: ")

        if user.lower() == "exit":

            print("Assistant: Thank you for visiting Smart Mall")
            break

        answer = get_response(user)

        print("\nAssistant:", answer)
        print()