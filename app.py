# Import necessary modules
from flask import Flask, request, render_template
from src.InsurancePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline

# Create Flask application instance
app = Flask(__name__)

# Define route for the home page
@app.route('/')
def home_page():
    return render_template("index.html")

# Define route for predicting datapoint
@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        # Retrieve form data
        age = float(request.form.get('age'))
        bmi = float(request.form.get('bmi'))
        children = float(request.form.get('children'))
        sex = request.form.get('sex')
        smoker = request.form.get('smoker')
        region = request.form.get('region')
        
        # Create CustomData object
        data = CustomData(age=age, bmi=bmi, children=children, sex=sex, smoker=smoker, region=region)
        
        # Get data as dataframe
        final_data = data.get_data_as_dataframe()
        
        # Create PredictPipeline object
        predict_pipeline = PredictPipeline()
        
        # Make prediction
        pred = predict_pipeline.predict(final_data)
        
        # Round the prediction result
        result = round(pred[0], 2)
        
        # Render result template with the prediction result
        return render_template("result.html", final_result=result)

# Execution begins here
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
