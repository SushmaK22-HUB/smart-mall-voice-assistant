from search_engine import search_by_category
from search_engine import search_by_floor
from search_engine import get_all_floors

print("\n=== Available Floors ===")
for floor in get_all_floors():
    print(floor)

print("\n=== Stores on First Floor ===")
for store in search_by_floor("First Floor"):
    print(
        f"{store['name']} | {store['category']} | {store['location']}"
    )

print("\n=== Stores on Third Floor ===")
for store in search_by_floor("Third Floor"):
    print(
        f"{store['name']} | {store['category']} | {store['location']}"
    )

print("\n=== Electronics Stores ===")
for store in search_by_category("Electronics"):
    print(
        f"{store['name']} | {store['floor']} | {store['location']}"
    )