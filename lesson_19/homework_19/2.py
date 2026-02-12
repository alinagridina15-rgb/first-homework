import os
import requests

BASE_URL = "http://127.0.0.1:8080"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "test.jpg")

# ---------- POST ----------
with open(IMAGE_PATH, "rb") as img:
    response = requests.post(
        f"{BASE_URL}/upload",
        files={"image": img}
    )

print("UPLOAD:", response.status_code, response.json())


image_url = response.json()["image_url"]
filename = image_url.split("/")[-1]

# ---------- GET JSON  ----------
headers = {"Content-Type": "text"}
response = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)
if response.status_code == 200:
    print("GET JSON:", response.status_code, response.json())
else:
    print("GET JSON error:", response.status_code, response.text)

# ---------- GET Image ----------
headers = {"Content-Type": "image"}
response = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)
if response.status_code == 200:
    download_path = os.path.join(BASE_DIR, "downloaded_" + filename)
    with open(download_path, "wb") as f:
        f.write(response.content)
    print("GET Image: 200, image saved to", download_path)
else:
    print("GET Image error:", response.status_code, response.text)

# ---------- DELETE ----------
response = requests.delete(f"{BASE_URL}/delete/{filename}")
try:
    print("DELETE:", response.status_code, response.json())
except:
    print("DELETE:", response.status_code, response.text)
