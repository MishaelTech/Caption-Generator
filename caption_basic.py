# https://huggingface.co/

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("TEXT_GENERATION_API_URL")
headers = {"Authorization": os.getenv("TEXT_GENERATION_HEADERS")}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "Question: which is the largest country in the world? Answer:",
})

print(output[0]["generated_text"])
