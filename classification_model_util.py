# Created by Amandeep at 6/15/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

from sklearn.externals import joblib

model = None


def load_model():
    classifier = open('model.pkl', 'rb')
    model = joblib.load(classifier)


def get_model():
    return model