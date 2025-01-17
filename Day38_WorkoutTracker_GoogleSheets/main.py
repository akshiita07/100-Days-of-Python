import os
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv("Day38_WorkoutTracker_GoogleSheets/.env")

nutrition_api_key = os.getenv("API_KEY")
nutrition_app_id = os.getenv("APP_ID")
print(f"Nutrition api key: {nutrition_api_key}")
print(f"Nutrition app id: {nutrition_app_id}")

today=datetime.now()

# print the exercise stats for plain text input: https://docx.syndigo.com/developers/docs/nutritionix-api-guide
nutrition_headers={
    "x-app-id":nutrition_app_id,
    "x-app-key":nutrition_api_key,
    "Content-Type": "application/json",
}
nutrition_parameters={
    "query":input("Which exercises did you perform today: "),   #eg: swam for 1 hour
    "weight_kg":63,
    "height_cm":172,
    "age":20,
}
nutrition_repsonse=requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",headers=nutrition_headers,json=nutrition_parameters)
nutrition_repsonse.raise_for_status #to check if any status error
# print(nutrition_repsonse.text)
# print(nutrition_repsonse.status_code)
# print(nutrition_repsonse.json())
result=nutrition_repsonse.json()

# GOOGLE SHEETS: https://dashboard.sheety.co/
basic_username="akshitapathak"
basic_password=os.getenv("SHEETY_PASSWORD")
token=os.getenv("BEARER_TOKEN")

for exercise in result["exercises"]:
    sheety_parameters={
        "workout":{
            "date":today.strftime("%d/%m/%Y"),
            "time":today.strftime("%H:%M:%S"),
            "exercise":exercise["name"].title(),   #convert to title case
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"],
        }
    }
    
    # USING BASIC AUTHENTICATION:
    # sheety_repsonse=requests.post(url="https://api.sheety.co/6e94b3d5304ddf6d53ea8022eb513017/myWorkoutsPythonDay38/workouts",json=sheety_parameters,auth=(basic_username,basic_password))

    # USING BEARER AUTHENTICATION:
    sheety_header={
        "Authorization": f"Bearer {token}"
    }
    sheety_repsonse=requests.post(url="https://api.sheety.co/6e94b3d5304ddf6d53ea8022eb513017/myWorkoutsPythonDay38/workouts",json=sheety_parameters,headers=sheety_header)
    
# google sheet: https://docs.google.com/spreadsheets/d/1eRIFPRjAGrI2tDGUyOpApzmGlEqdbrZLgUqTw2MVwz0/edit?gid=0#gid=0