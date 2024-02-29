import pandas as pd
import numpy as np
from src.InsurancePrediction.logger import logging

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

@dataclass
class CustomException(Exception):
    message: str

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data", "insurance.csv")))
            logging.info("Dataset read successfully as a DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw dataset saved in the artifacts folder")

            logging.info("Performing train-test split")
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train-test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data ingestion completed")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.error("Exception occurred during data ingestion")
            raise CustomException(str(e))

# Example usage:
if __name__ == "__main__":
    data_ingestion = DataIngestion()
    try:
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        print("Train data path:", train_data_path)
        print("Test data path:", test_data_path)
    except CustomException as e:
        print("Custom exception occurred:", e.message)
