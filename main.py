from src.extract import fetch_all_weather
from src.extract import save_raw_data

weather = fetch_all_weather()

save_raw_data(weather)