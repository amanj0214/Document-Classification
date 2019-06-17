# Created by Amandeep at 6/17/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

from flask import json
import classification_model_util
import json


def get_request_data(request):
    """
    validates the reuqest and returns data
    :param request:
    :return: data on which predictions are to be made.
    """
    data = None
    if (request.method == 'GET') and ('words' in request.args):
        data = [request.args['words']]
    elif request.method == 'POST' and request.json is not None and ('words' in request.json):
        data = [request.json['words']]
    return data


def get_predictions(data):
    """
    get the document category prediction for the data.
    :param data:
    :return: Dictionary with prediction and confidence.
    """
    prediction = classification_model_util.classifier.predict(data).tolist()[0]
    confidence = classification_model_util.classifier.predict_proba(data).max() * 100
    confidence = round(confidence, 2)
    #print("my_prediction", prediction)
    dict = {"prediction": prediction, "confidence": confidence}
    return dict