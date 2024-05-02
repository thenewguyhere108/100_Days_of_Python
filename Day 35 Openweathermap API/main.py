import requests
import os

MY_LAT = 25.21
MY_LONG = 55.21
API_KEY = os.environ.get("API_KEY")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 6
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = response.json()
rain_check = False
for i in data["list"]:
    if 600 > i["weather"][0]["id"] > 200:
        rain_check = True

if rain_check:
    print("It's gonna rain today , Please take an umbrella")
