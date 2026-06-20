import json

with open("data/stores.json", "r", encoding="utf-8") as file:
    stores = json.load(file)

def get_response(query):
    query = query.lower()

    for store in stores:
        store_name = store["name"].lower()

        if store_name in query:
            if len(store_name) > 2:
                return f"{store['name']} is on {store['floor']} at {store['location']}."

    return "Sorry, I couldn't find that store."
    # Store search
    for store in stores:
        if store["name"].lower() in query:
            return f"{store['name']} is on {store['floor']} at {store['location']}."

    # Food options
    if "food" in query or "dining" in query or "restaurant" in query:
        food_stores = [s["name"] for s in stores
                       if s["category"] in ["Food", "Cafe", "Restaurant", "Desserts"]]
        return "Dining options available are: " + ", ".join(food_stores)

    # Electronics
    if "electronics" in query:
        electronics = [s["name"] for s in stores
                       if s["category"] == "Electronics"]
        return "Electronics stores available are: " + ", ".join(electronics)

    # Fashion
    if "fashion" in query:
        fashion = [s["name"] for s in stores
                   if "Fashion" in s["category"]]
        return "Fashion stores available are: " + ", ".join(fashion)

    return "Sorry, I couldn't find that store."
while True:
    query = input("Ask a question: ")

    if query.lower() == "exit":
        break

    print(get_response(query))