import pandas as pd
import numpy as np
import os
import sys
from src.InsurancePrediction.logger import logging
from src.InsurancePrediction.exception import CustomException
from dataclasses import dataclass
from src.InsurancePrediction.utils.utils import save_object
from src.InsurancePrediction.utils.utils import evaluate_model

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'Elasticnet': ElasticNet()
            }

            model_report = evaluate_model(X_train, y_train, X_test, y_test, models)

            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary
            best_model_name, best_model_score = max(model_report.items(), key=lambda x: x[1])

            best_model = models[best_model_name]

            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            logging.error('Exception occurred at Model Training', exc_info=True)
            raise CustomException(e, sys.exc_info())
