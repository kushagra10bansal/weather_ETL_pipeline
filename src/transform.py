import pandas as pd


def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)


def transform_weather_data(weather_data):

    transformed = []

    for record in weather_data:

        transformed.append({
            "City": record["name"],
            "Weather": record["weather"][0]["main"],
            "Description": record["weather"][0]["description"],
            "Temperature_C": kelvin_to_celsius(record["main"]["temp"]),
            "Feels_Like_C": kelvin_to_celsius(record["main"]["feels_like"]),
            "Humidity": record["main"]["humidity"],
            "Pressure": record["main"]["pressure"],
            "Wind_Speed": record["wind"]["speed"],
            "Timestamp": pd.to_datetime(record["dt"], unit="s")
        })

    return pd.DataFrame(transformed)