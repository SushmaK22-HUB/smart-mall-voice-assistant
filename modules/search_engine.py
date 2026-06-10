import json

# ---------------- LOAD JSON FILES ---------------- #

with open("data/stores.json", "r") as file:
    stores = json.load(file)

with open("data/facilities.json", "r") as file:
    facilities = json.load(file)

with open("data/parking.json", "r") as file:
    parking = json.load(file)

with open("data/offers.json", "r") as file:
    offers = json.load(file)

with open("data/jobs.json", "r") as file:
    jobs = json.load(file)

with open("data/events.json", "r") as file:
    events = json.load(file)

with open("data/emergency.json", "r") as file:
    emergency = json.load(file)

with open("data/food.json", "r") as file:
    food = json.load(file)


# ---------------- STORE SEARCH ---------------- #

def search_store(store_name):

    for store in stores:

        if store_name.lower() in store["name"].lower():

            return (
                f"🏬 Store: {store['name']}\n\n"
                f"📂 Category: {store['category']}\n"
                f"📍 Floor: {store['floor']}\n"
                f"📌 Location: {store['location']}"
            )

    return None

# ---------------- FACILITY SEARCH ---------------- #

def search_facility(facility_name):

    for facility in facilities:
        if facility_name.lower() in facility["name"].lower():

            return (
                f"{facility['name']} is available on "
                f"{facility['floor']} near "
                f"{facility['location']}."
            )

    return None


# ---------------- PARKING INFO ---------------- #

def get_parking_info():

    return (
        f"Car Parking available at "
        f"{parking['floor']}. "
        f"Charges: {parking['charges']}"
    )


# ---------------- OFFERS ---------------- #

def get_offers():

    result = "Current Offers:\n"

    for offer in offers:
        result += (
            f"{offer['store']} - "
            f"{offer['offer']}\n"
        )

    return result


# ---------------- JOBS ---------------- #

def get_jobs():

    result = "Available Jobs:\n"

    for job in jobs:
        result += (
            f"{job['company']} - "
            f"{job['role']}\n"
        )

    return result


# ---------------- EVENTS ---------------- #

def get_events():

    result = "Upcoming Events:\n"

    for event in events:
        result += (
            f"{event['event']} - "
            f"{event['date']}\n"
        )

    return result


# ---------------- EMERGENCY ---------------- #

def get_emergency():

    result = "Emergency Information:\n"

    for item in emergency:
        result += (
            f"{item['type']} - "
            f"{item['location']}\n"
        )

    return result


# ---------------- FOOD SEARCH ---------------- #

def search_food(food_name):

    for category in food:

        for restaurant in category["restaurants"]:

            if food_name.lower() in restaurant["name"].lower():

                return (
                    f"{restaurant['name']} is on "
                    f"{restaurant['floor']}."
                )

    return None


# ---------------- ALL STORES ---------------- #

def get_all_stores():

    result = "Available Stores:\n"

    for store in stores:
        result += f"{store['name']} ({store['floor']})\n"

    return result


# ---------------- ALL FACILITIES ---------------- #

def get_all_facilities():

    result = "Available Facilities:\n"

    for facility in facilities:
        result += f"{facility['name']} ({facility['floor']})\n"

    return result


# ---------------- ALL FOOD OUTLETS ---------------- #

def get_all_food():

    result = "Food Outlets:\n"

    for category in food:

        for restaurant in category["restaurants"]:

            result += (
                f"{restaurant['name']} "
                f"({restaurant['floor']})\n"
            )

    return result

# ---------------- FLOOR-WISE STORES ---------------- #

def get_stores_by_floor(floor_name):

    result = f"Stores on {floor_name}:\n"

    found = False

    for store in stores:

        if floor_name.lower() in store["floor"].lower():

            result += f"{store['name']}\n"
            found = True

    if found:
        return result

    return f"No stores found on {floor_name}."

# ---------------- FOOD BY FLOOR ---------------- #

def get_food_by_floor(floor_name):

    result = f"Food Outlets on {floor_name}:\n"

    found = False

    for item in food:

        if floor_name.lower() in item["floor"].lower():

            result += f"{item['name']}\n"
            found = True

    if found:
        return result

    return f"No food outlets found on {floor_name}."

# ---------------- STORE CATEGORY SEARCH ---------------- #

def get_stores_by_category(category_name):

    result = f"{category_name.title()} Stores:\n"

    found = False

    for store in stores:

        if category_name.lower() in store["category"].lower():

            result += f"{store['name']}\n"
            found = True

    if found:
        return result

    return f"No stores found in category: {category_name}"

# ---------------- STORE NAVIGATION ---------------- #

def get_navigation(store_name):

    for store in stores:

        if store_name.lower() in store["name"].lower():

            return (
                f"To reach {store['name']}, "
                f"go to {store['floor']} "
                f"near {store['location']}."
            )

    return None