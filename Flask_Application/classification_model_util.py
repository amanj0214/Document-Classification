# Created by Amandeep at 6/15/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

from sklearn.externals import joblib
import sys


class ModelUtil:
    """
    A utility class for our document classification task.
    """
    model = None

    def __init__(self):
        pass

    def get_model(self):
        """
        Return the trained model, if model is not trained then trains the model and returns it.
        :return: Trained model is returned.
        """
        if self.model == None:
            classifier = open('model_small.pkl', 'rb')
            self.model = joblib.load(classifier)
        return self.model


# Load and train model when the app is getting deployed.
model_util = ModelUtil()
classifier = model_util.get_model()