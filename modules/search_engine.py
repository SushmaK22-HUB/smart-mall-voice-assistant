import json

# Load JSON data
with open("data/stores.json", "r", encoding="utf-8") as file:
    stores = json.load(file)


# Search by category
def search_by_category(category):
    results = []

    for store in stores:
        if category.lower() in store["category"].lower():
            results.append(store)

    return results


# Search by floor
def search_by_floor(floor):
    results = []

    for store in stores:
        if floor.lower() in store["floor"].lower():
            results.append(store)

    return results


# Get all floors
def get_all_floors():
    floors = set()

    for store in stores:
        floors.add(store["floor"])

    return sorted(list(floors))