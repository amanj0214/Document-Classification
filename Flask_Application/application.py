# Created by Amandeep at 6/15/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

# Import libraries
from flask import Flask, request, jsonify, render_template, Response
import json
import application_util

# EB looks for an 'application' callable by default.
application = Flask(__name__)


@application.route('/predict',methods=['POST', 'GET'])
def predict():
    data = application_util.get_request_data(request)
    print(data)
    if data is not None:
        result = application_util.get_predictions(data)
    else:
        result = "[Error]: The words are not found in your request." \
                 "Valid formats are :" \
                 "curl -i -X GET 'Content-type: application/json' GET http://127.0.0.1:4444/predict?words='WORDS+IN+DOCUMENT' OR" \
                 "curl -i -H 'Content-type: application/json' -X POST http://127.0.0.1:4444/predict -d '{'words':'WORDS IN MY DOCUMENT'}'"
    resp = jsonify(result)
    resp.status_code = 200
    return resp


@application.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@application.errorhandler(400)
def not_found(error=None):
    message = {
            'status': 400,
            'message': 'Bad Request: Server could not understand - ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@application.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    # Load the model
    application.run(port=4444, debug=True)
