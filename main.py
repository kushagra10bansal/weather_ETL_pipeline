from src.extract import fetch_all_weather, save_raw_data
from src.validate import validate_weather_data
from src.transform import transform_weather_data
from src.load import save_parquet, upload_to_s3

weather = fetch_all_weather()
valid_weather = validate_weather_data(weather)
save_raw_data(valid_weather)
df = transform_weather_data(valid_weather)
parquet_file = save_parquet(df)
upload_to_s3(
    parquet_file,
    "weather-etl-kb-2026"
)