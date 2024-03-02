from src.InsurancePrediction.pipelines.prediction_pipeline import CustomData

custdataobj = CustomData(37, 27.7, 3, "female", "no", "northwest")

data=custdataobj.get_data_as_dataframe()

print(data)
