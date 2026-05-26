import json

with open("data/stores.json", "r") as file:

    stores = json.load(file)


def search_by_category(category):

    results = []

    for store in stores:

        if category.lower() in store["category"].lower():

            results.append(store)

    return results
def search_by_floor(floor):

    results = []

    for store in stores:

        if floor.lower() in store["floor"].lower():

            results.append(store)

    return results