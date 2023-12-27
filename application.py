from flask import Flask, request, render_template
from waitress import serve
from src.logger import logging
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=int(request.form.get('writing_score')),
            writing_score=int(request.form.get('reading_score'))
        )

        pred_df = data.get_data_as_data_frame()
        logging.info(f"Input data: {pred_df}")

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        logging.info(f"Prediction results: {results}")

        return render_template('home.html', results=results[0] if results else None)

if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=8000)