# Created by Amandeep at 6/15/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

# Import libraries
from flask import Flask, request, jsonify, render_template
import json
import classification_model_util

# EB looks for an 'application' callable by default.
application = Flask(__name__)


@application.route('/predict',methods=['POST'])
def predict():
    data = [request.data]
    prediction = classification_model_util.classifier.predict(data).tolist()[0]
    confidence = classification_model_util.classifier.predict_proba(data).max() * 100
    confidence = round(confidence, 2)
    print("my_prediction", prediction)
    dict = {"prediction" : prediction, "confidence" : confidence}
    return jsonify(dict)



@application.route('/')
def home():
	return render_template('home.html')


if __name__ == '__main__':
    # Load the model
    application.run(port=4444, debug=True)
