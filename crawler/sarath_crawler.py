import requests

url = "https://sarathcitycapitalmall.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

with open("homepage.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Saved successfully")
