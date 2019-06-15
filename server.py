# Created by Amandeep at 6/15/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

# Import libraries
from flask import Flask, request, jsonify, send_from_directory, render_template
import pickle
import traceback
import json
from flask_cors import CORS
import model_training

app = Flask(__name__)


@app.route('/predict',methods=['POST'])
def get_predictions():
    return jsonify(details)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Load the model
    app.run(port=4444, debug=True)
