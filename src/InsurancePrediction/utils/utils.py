import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException  # Correct import

from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        logging.error("Error occurred while saving object to file:", exc_info=True)  # Log full traceback
        raise CustomException(str(e))  # Raise custom exception

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for model_name, model in models.items():
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
            report[model_name] = test_model_score

        return report

    except Exception as e:
        logging.error("Exception occurred during model evaluation:", exc_info=True)
        raise CustomException(str(e))

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.error("Error occurred while loading object from file:", exc_info=True)
        raise CustomException(str(e))
