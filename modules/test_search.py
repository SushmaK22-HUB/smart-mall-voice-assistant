from search_engine import search_by_floor
from search_engine import get_all_floors

print("=== ALL STORES FLOOR-WISE ===\n")

for floor in get_all_floors():
    print(f"\n===== {floor} =====")

    stores = search_by_floor(floor)

    for store in stores:
        print(
            f"{store['name']} | {store['category']} | {store['location']}"
        )