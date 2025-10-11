# 🏋️‍♂️ Fitness Tracker Automation

A **Python-based fitness tracker** that logs your daily exercises and calculates calories burned using the **Nutritionix API**, then records the data into a **Google Sheet** via **Sheety API**. Automate your workout logging in a few simple steps!  

---

## Features

- 📝 Input natural language exercise descriptions (e.g., `"ran 5 km and did 30 push-ups"`).  
- 🔥 Automatically calculates **calories burned**, duration, and exercise type.  
- 📅 Logs **date and time** for each exercise.  
- 💾 Stores workout data in a **Google Sheet** for easy tracking.  
- 🔒 Uses `.env` for secure storage of API keys and personal details.  

---

## Demo

What exercises did you do today? ran 5 km and cycled 20 minutes

The script will then log each exercise into your Google Sheet with:

| Date       | Time    | Exercise | Duration (min) | Calories |
|------------|---------|----------|----------------|----------|
| 11/10/2025 | 14:32:10 | Running  | 30             | 250      |
| 11/10/2025 | 14:32:10 | Cycling  | 20             | 180      |

---

## Installation

1.Create a .env file in the root directory with the following:
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
SHEET_ENDPOINT=your_sheety_endpoint
SHEET_AUTH=Basic your_sheety_auth
GENDER=male
HEIGHT_CM=175
WEIGHT_KG=70
AGE=25

## Technologies

Python 3
Requests – For making HTTP requests.
Nutritionix API – For exercise recognition and calorie calculation.
Sheety API – For Google Sheet integration.
dotenv – For managing environment variables securely.
