import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city="Sirsa"):
    url = (
        f"http://api.weatherapi.com/v1/current.json"
        f"?key={API_KEY}&q={city}&aqi=no"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            return data["error"]["message"]

        location = data["location"]["name"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]

        return (
            f"Weather in {location}: "
            f"{temp}°C, {condition}. "
            f"Humidity is {humidity}%."
        )

    except Exception as e:
        return f"Weather Error: {e}"