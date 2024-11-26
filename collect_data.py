import requests
import pandas as pd
from datetime import datetime

API_KEY = "0cea2e46e3cc59f7ce7890311a6d8971"
CITY = "London"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather_data():
    response = requests.get(URL)
    data = response.json()
    weather_data = {
        "Temperature": data["main"]["temp"],
        "Humidity": data["main"]["humidity"],
        "Wind Speed": data["wind"]["speed"],
        "Weather Condition": data["weather"][0]["description"],
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Time": datetime.now().strftime("%H:%M:%S"),
    }
    return weather_data

# Collect data for 5 days
weather_records = []
for _ in range(5):
    weather_records.append(fetch_weather_data())

df = pd.DataFrame(weather_records)
df.to_csv("raw_data.csv", index=False)
