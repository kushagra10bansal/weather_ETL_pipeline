from src.utils import logger


def validate_weather_data(weather_data):

    valid_records = []

    for record in weather_data:
        try:
            required_fields = [
                "name",
                "main",
                "weather",
                "wind",
                "dt"
            ]

            if not all(field in record for field in required_fields):
                logger.warning(f"Skipping record. Missing fields: {record}")
                continue

            valid_records.append(record)

        except Exception as e:
            logger.error(e)

    logger.info(f"Valid Records : {len(valid_records)}")

    return valid_records