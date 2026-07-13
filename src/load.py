import os
from datetime import datetime

import boto3

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

    logger.info(f"Saved locally: {path}")

    return path


def upload_to_s3(file_path, bucket_name):

    s3 = boto3.client("s3")

    file_name = os.path.basename(file_path)

    s3.upload_file(
        file_path,
        bucket_name,
        file_name
    )

    logger.info(f"Uploaded {file_name} to {bucket_name}")