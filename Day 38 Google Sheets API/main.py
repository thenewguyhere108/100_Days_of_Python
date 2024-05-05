import requests
import datetime
from secrets import *

api_key = nutrinox_api_key
app_id = nutrinox_app_id
SHEETY_URL = sheety_url
now = datetime.datetime.now()


nutritionx_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
workout = input("What did you do today ? : ")

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
    "Content-Type": "application/json",
}

parameters = {
    "query": workout,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

request = requests.post(url=nutritionx_url, headers=headers, json=parameters)
data = request.json()
sheet_endpoint = requests.get(url=SHEETY_URL)
sheet_data = sheet_endpoint.json()
row_no = len(sheet_data["sheet1"]) + 1

for i in data["exercises"]:
    row_no += 1
    sheet_data = {
        "sheet1": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": str(i["name"]).title(),
            "duration": str(i["duration_min"]),
            "calories": i["nf_calories"],
            "id": row_no}
    }

    post_request = requests.post(url=SHEETY_URL, json=sheet_data)

print("Your google sheet is successfully updated")
