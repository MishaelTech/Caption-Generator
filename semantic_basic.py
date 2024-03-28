import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("IMAGE_TEXT_API_URL")
headers = {"Authorization": os.getenv("IMAGE_TEXT_HEADERS")}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("Image\cat.jpg")
print(output[0]["generated_text"])
