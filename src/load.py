import os
from datetime import datetime

from src.utils import logger


def save_parquet(df):

    os.makedirs("data/processed", exist_ok=True)

    filename = datetime.now().strftime(
        "weather_%Y%m%d_%H%M%S.parquet"
    )

    path = os.path.join(
        "data",
        "processed",
        filename
    )

    df.to_parquet(path, index=False)

    logger.info(f"Saved {path}")

    return path