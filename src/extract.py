import json
import requests
import os
from datetime import datetime

from config.config import API_KEY, BASE_URL
from src.utils import logger


def fetch_weather(city):

    logger.info(f"Fetching weather for {city}")

    params = {
        "q": city,
        "appid": API_KEY
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    return response.json()

def load_city_list():

    with open("config/cities.json", "r") as file:
        cities = json.load(file)

    return cities["cities"]

def fetch_all_weather():

    weather_data = []

    cities = load_city_list()

    for city in cities:

        try:

            city_weather = fetch_weather(city)

            weather_data.append(city_weather)

            logger.info(f"{city} fetched successfully")

        except Exception as e:

            logger.error(f"Failed for {city}")

            logger.error(e)

    return weather_data

def save_raw_data(weather_data):

    os.makedirs("data/raw", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"data/raw/weather_raw_{timestamp}.json"

    with open(filename, "w") as file:

        json.dump(weather_data, file, indent=4)

    logger.info(f"Raw data saved to {filename}")

    return filename