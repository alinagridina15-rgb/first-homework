import requests
import os

BASE_URL = "https://images-api.nasa.gov"


search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

search_response = requests.get(search_url, params=search_params)
search_response.raise_for_status()

search_data = search_response.json()

# Витягуємо nasa_id
items = search_data["collection"]["items"]
nasa_ids = []

for item in items:
    nasa_id = item["data"][0].get("nasa_id")
    if nasa_id:
        nasa_ids.append(nasa_id)
    if len(nasa_ids) >= 2:
        break

print("NASA IDs:", nasa_ids)


def download_best_jpg(nasa_id, filename):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()

    asset_data = asset_response.json()


    jpg_links = [
        item["href"]
        for item in asset_data["collection"]["items"]
        if item["href"].lower().endswith(".jpg")
    ]

    if not jpg_links:
        raise Exception(f"No JPG found for nasa_id={nasa_id}")


    jpg_url = jpg_links[0]

    img_response = requests.get(jpg_url)
    img_response.raise_for_status()

    with open(filename, "wb") as f:
        f.write(img_response.content)

    print(f"Downloaded: {filename}")


download_best_jpg(nasa_ids[0], "mars_photo1.jpg")
download_best_jpg(nasa_ids[1], "mars_photo2.jpg")
