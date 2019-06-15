# Created by Amandeep at 6/15/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

from sklearn.externals import joblib


class ModelUtil:
    model = None

    def __init__(self):
        pass

    def get_model(self):
        if self.model == None:
            #classifier = open('model_2.pkl', 'rb')
            classifier = open('model_light.pkl', 'rb')
            self.model = joblib.load(classifier)
        return self.model

model_util = ModelUtil()
classifier = model_util.get_model()