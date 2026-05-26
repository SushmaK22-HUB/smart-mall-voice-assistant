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
                f"{store['name']} is on the "
                f"{store['floor']}, near "
                f"{store['location']}."
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

    for item in food:
        if food_name.lower() in item["name"].lower():

            return (
                f"{item['name']} is on "
                f"{item['floor']} near "
                f"{item['location']}."
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

    for item in food:
        result += f"{item['name']} ({item['floor']})\n"

    return result