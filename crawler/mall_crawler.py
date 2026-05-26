import requests
from bs4 import BeautifulSoup
import json

url = "https://sarathcitycapitalmall.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

stores_data = []

# Find all text elements
stores = soup.find_all(["h2", "h3", "p", "a"])

for store in stores:

    text = store.get_text(strip=True)

    if text and len(text) < 40:

        stores_data.append({
            "name": text,
            "category": "Unknown",
            "floor": "Unknown"
        })

# Remove duplicates
unique_stores = []

seen = set()

for item in stores_data:

    if item["name"] not in seen:

        seen.add(item["name"])

        unique_stores.append(item)

# Save JSON
with open("data/stores.json", "w") as file:

    json.dump(unique_stores, file, indent=4)

print("Store data saved successfully!")