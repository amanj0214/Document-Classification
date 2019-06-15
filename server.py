# Created by Amandeep at 6/15/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

# Import libraries
from flask import Flask, request, jsonify, render_template
import pickle
import traceback
import json
from flask_cors import CORS
import classification_model_util

app = Flask(__name__)


@app.route('/predict',methods=['POST'])
def predict():
    data = [request.data]
    predictions = classification_model_util.classifier.predict(data).tolist()
    print("my_prediction", predictions)
    return jsonify(predictions)


@app.route('/')
def home():
	return render_template('home.html')


if __name__ == '__main__':
    # Load the model
    app.run(port=4444, debug=True)
