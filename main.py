import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get secrets from environment
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
SHEET_AUTH = os.getenv("SHEET_AUTH")

# Personal details
gender = os.getenv("GENDER")
height_cm = float(os.getenv("HEIGHT_CM"))
weight_kg = float(os.getenv("WEIGHT_KG"))
age = int(os.getenv("AGE"))

link = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("What exercises did you do today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

# Send request to Nutritionix API
response = requests.post(url=link, headers=headers, json=parameters)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety headers using Basic Auth
sheet_headers = {
    "Authorization": SHEET_AUTH,
    "Content-Type": "application/json"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Send data to Sheety
    sheet_response = requests.post(
        url=SHEET_ENDPOINT,
        json=sheet_inputs,
        headers=sheet_headers
    )

    print(sheet_response.text)
