from src.InsurancePrediction.components.data_ingestion import DataIngestion
from src.InsurancePrediction.components.data_transformation import DataTransformation
from src.InsurancePrediction.components.model_trainer import ModelTrainer
from src.InsurancePrediction.exception import CustomException
import sys

class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            return train_data_path, test_data_path
        except Exception as e:
            raise CustomException(str(e), sys.exc_info())

    def start_data_transformation(self, train_data_path, test_data_path):
        try:
            data_transformation = DataTransformation()
            train_arr, test_arr = data_transformation.initialize_data_transformation(train_data_path, test_data_path)
            return train_arr, test_arr
        except Exception as e:
            raise CustomException(str(e), sys.exc_info())

    def start_model_training(self, train_arr, test_arr):
        try:
            model_trainer = ModelTrainer()
            model_trainer.train(train_arr, test_arr)  # Assuming 'train' is the correct method name
        except Exception as e:
            raise CustomException(str(e), sys.exc_info())

    def start_training(self):
        try:
            train_data_path, test_data_path = self.start_data_ingestion()
            train_arr, test_arr = self.start_data_transformation(train_data_path, test_data_path)
            self.start_model_training(train_arr, test_arr)
        except CustomException as e:
            # Handle custom exceptions here, log or re-raise if needed
            print("Custom exception occurred:", e)
        except Exception as e:
            # Handle other exceptions
            print("An unexpected error occurred:", e)

# Example usage:
if __name__ == "__main__":
    training_pipeline = TrainingPipeline()
    training_pipeline.start_training()
