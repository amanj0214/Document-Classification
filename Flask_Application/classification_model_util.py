# Created by Amandeep at 6/15/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

import pandas as pd
import numpy as np
from sklearn.feature_selection import chi2
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.calibration import CalibratedClassifierCV
from sklearn.pipeline import Pipeline
import boto3
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
            self.train_model()
        return self.model

    def train_model(self):
        """
        Train the model.
        :return:
        """
        df = pd.read_csv("shuffled-full-set-hashed.csv", header=None)
        #df = self.load_data()
        df.columns = ['Category', 'Content']

        (features_train, labels_train) = (df.loc[1:50, 'Content'].values.astype('U'), df.loc[1:50, 'Category'])

        ### TfidfVectorizer
        tfidfv = TfidfVectorizer(ngram_range=(1, 2), min_df=0.01, max_df=0.44, norm='l2')

        ## Selector.
        selector = SelectKBest(chi2, k=1000)

        ## Linear SVC model.
        linear_svc = LinearSVC()

        calibrated_svc = CalibratedClassifierCV(linear_svc, method='sigmoid')

        linearsvc = Pipeline([('vect', tfidfv),
                              ('selector', selector),
                              ('clf', calibrated_svc),
                              ])
        linearsvc.fit(features_train, labels_train)
        self.model = linearsvc

    def load_data(self):
        """
        Function to load data from S3
        :return:
        """
        if sys.version_info[0] < 3:
            from StringIO import StringIO  # Python 2.x
        else:
            from io import StringIO  # Python 3.x

        aws_id = "AMAN_AWS_ID"
        aws_secret = "AMAN_AWS_SECRET"

        client = boto3.client('s3', aws_access_key_id=aws_id,
                              aws_secret_access_key=aws_secret)

        bucket_name = 'classification-data-hw'

        object_key = 'shuffled-full-set-hashed.csv'
        csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
        body = csv_obj['Body']
        csv_string = body.read().decode('utf-8')

        df = pd.read_csv(StringIO(csv_string), header=None)
        return df


# Load and train model when the app is getting deployed.
model_util = ModelUtil()
classifier = model_util.get_model()