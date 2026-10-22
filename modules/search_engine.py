import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_json_data(filename):
    file_path = os.path.join(DATA_DIR, filename)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning loading {filename}: {e}")
        return []

stores = load_json_data("stores.json")
facilities = load_json_data("facilities.json")
parking = load_json_data("parking.json")
offers = load_json_data("offers.json")
jobs = load_json_data("jobs.json")
events = load_json_data("events.json")
emergency = load_json_data("emergency.json")
food = load_json_data("food.json")


def search_store(query):
    query_lower = query.lower().strip()
    
    # Pass 1: Match whole store name in the user's sentence (e.g. "nike" in "where is nike")
    for store in stores:
        name = store.get("name", "").strip().lower()
        if name and re.search(rf"\b{re.escape(name)}\b", query_lower):
            return (
                f"🏬 Store: {store.get('name')}\n\n"
                f"📂 Category: {store.get('category', 'General')}\n"
                f"📍 Floor: {store.get('floor', 'N/A')}\n"
                f"📌 Location: {store.get('location', 'N/A')}"
            )
            
    # Pass 2: Partial match if user typed a keyword (e.g. "burger" matching "Burger King")
    for store in stores:
        name = store.get("name", "").strip().lower()
        if len(query_lower) >= 3 and query_lower in name:
            return (
                f"🏬 Store: {store.get('name')}\n\n"
                f"📂 Category: {store.get('category', 'General')}\n"
                f"📍 Floor: {store.get('floor', 'N/A')}\n"
                f"📌 Location: {store.get('location', 'N/A')}"
            )
    return None

def search_facility(query):
    query_lower = query.lower()
    for facility in facilities:
        name = facility.get("name", "").lower()
        if name and (name in query_lower or query_lower in name):
            return (
                f"ℹ️ {facility.get('name')} is available on "
                f"{facility.get('floor', 'N/A')} near "
                f"{facility.get('location', 'N/A')}."
            )
    return None


def get_parking_info():
    p_data = parking
    if isinstance(parking, list) and len(parking) > 0:
        p_data = parking[0]
        
    if isinstance(p_data, dict):
        return (
            f"🚗 Car Parking available at {p_data.get('floor', 'Basement')}. "
            f"Charges: {p_data.get('charges', 'Standard rates apply')}."
        )
    return "🚗 Parking information is currently unavailable."


def get_offers():
    if not offers:
        return "No current offers available."
    result = "🔥 Current Offers:\n\n"
    for offer in offers:
        store_name = offer.get("store_name", "Special Offer")
        offer_title = offer.get("offer_title", "")
        result += f"• {store_name}: {offer_title}\n"
    return result


def get_jobs():
    if not jobs:
        return "No job openings currently posted."
    result = "💼 Available Jobs:\n\n"
    for job in jobs:
        title = job.get("job_title", "Position")
        dept = job.get("department", "Mall")
        result += f"• {title} ({dept})\n"
    return result


def get_events():
    if not events:
        return "No upcoming events scheduled."
    result = "🎉 Upcoming Events:\n\n"
    for event in events:
        name = event.get("event_name", "Mall Event")
        date = event.get("date", "Coming Soon")
        result += f"• {name} - {date}\n"
    return result


def get_emergency():
    if not emergency:
        return "Emergency Contact: Security Desk on Ground Floor."
    result = "🚨 Emergency Assistance:\n\n"
    for item in emergency:
        service = item.get("service_name", "Emergency Service")
        location = item.get("location", "Help Desk")
        result += f"• {service}: {location}\n"
    return result


def search_food(query):
    query_lower = query.lower()
    for category in food:
        restaurants = category.get("restaurants", [])
        for restaurant in restaurants:
            name = restaurant.get("name", "").lower()
            if name and (name in query_lower or query_lower in name):
                return (
                    f"🍔 {restaurant.get('name')} is located on "
                    f"{restaurant.get('floor', 'Food Court')}."
                )
    return None


def get_all_stores():
    if not stores:
        return "No stores listed."
    result = "🏬 Available Stores:\n"
    for store in stores:
        result += f"• {store.get('name')} ({store.get('floor', 'N/A')})\n"
    return result


def get_all_facilities():
    if not facilities:
        return "No facilities listed."
    result = "ℹ️ Available Facilities:\n"
    for facility in facilities:
        result += f"• {facility.get('name')} ({facility.get('floor', 'N/A')})\n"
    return result


def get_all_food():
    if not food:
        return "No food outlets listed."
    result = "🍔 Food Outlets:\n"
    for category in food:
        for restaurant in category.get("restaurants", []):
            result += f"• {restaurant.get('name')} ({restaurant.get('floor', 'Food Court')})\n"
    return result


def get_stores_by_floor(floor_name):
    result = f"Stores on {floor_name}:\n"
    found = False
    for store in stores:
        if floor_name.lower() in store.get("floor", "").lower():
            result += f"• {store.get('name')}\n"
            found = True
    return result if found else f"No stores found on {floor_name}."


def get_food_by_floor(floor_name):
    result = f"Food Outlets on {floor_name}:\n"
    found = False
    for category in food:
        for restaurant in category.get("restaurants", []):
            if floor_name.lower() in restaurant.get("floor", "").lower():
                result += f"• {restaurant.get('name')}\n"
                found = True
    return result if found else f"No food outlets found on {floor_name}."


def get_stores_by_category(category_name):
    result = f"{category_name.title()} Stores:\n"
    found = False
    for store in stores:
        if category_name.lower() in store.get("category", "").lower():
            result += f"• {store.get('name')}\n"
            found = True
    return result if found else f"No stores found in category: {category_name}."


def get_navigation(store_name):
    query_lower = store_name.lower().strip()
    
    # 1. Search in Stores
    for store in stores:
        name = store.get("name", "").strip().lower()
        if name and (re.search(rf"\b{re.escape(name)}\b", query_lower) or query_lower in name or name in query_lower):
            return (
                f"To reach {store.get('name')}, go to {store.get('floor', 'designated floor')} "
                f"near {store.get('location', 'information desk')}."
            )
            
    # 2. Search in Food Outlets (for KFC, Burger King, Starbucks, etc.)
    for category in food:
        for restaurant in category.get("restaurants", []):
            name = restaurant.get("name", "").strip().lower()
            if name and (re.search(rf"\b{re.escape(name)}\b", query_lower) or query_lower in name or name in query_lower):
                return (
                    f"To reach {restaurant.get('name')}, go to {restaurant.get('floor', 'Food Court')}."
                )
                
    return f"Navigation directions for {store_name} are currently unavailable."