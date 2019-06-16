# Created by Amandeep at 6/15/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

import pandas as pd
import numpy as np
from sklearn.feature_selection import chi2
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.pipeline import Pipeline
import boto3
import sys


class ModelUtil:
    model = None

    def __init__(self):
        pass

    def get_model(self):
        if self.model == None:
            self.train_model()
        return self.model

    def train_model(self):
        #df = pd.read_csv("shuffled-full-set-hashed.csv", header=None)
        df = self.load_data()
        df.columns = ['Category', 'Content']

        (features_train, labels_train) = (df.loc[1:40, 'Content'].values.astype('U'), df.loc[1:40, 'Category'])

        ### TfidfVectorizer
        tfidfv = TfidfVectorizer(ngram_range=(1, 2), min_df=0.01, max_df=0.44, norm='l2')

        ## Selector
        selector = SelectKBest(chi2, k=1000)

        clf = LinearSVC()

        linearsvc = Pipeline([('vect', tfidfv),
                              ('selector', selector),
                              ('clf', clf),
                              ])
        linearsvc.fit(features_train, labels_train)
        self.model = linearsvc

    def load_data(self):
        if sys.version_info[0] < 3:
            from StringIO import StringIO  # Python 2.x
        else:
            from io import StringIO  # Python 3.x

        # get your credentials from environment variables
        aws_id = 'AKIAI6MTK372VSBZUJCQ'
        aws_secret = 'SIVH9SQDAEtmz7WrPzcXa6cvVS2ox0lPMl3T6Z3o'

        client = boto3.client('s3', aws_access_key_id=aws_id,
                              aws_secret_access_key=aws_secret)

        bucket_name = 'classification-data-hw'

        object_key = 'shuffled-full-set-hashed.csv'
        csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
        body = csv_obj['Body']
        csv_string = body.read().decode('utf-8')

        df = pd.read_csv(StringIO(csv_string), header=None)
        return df

model_util = ModelUtil()
classifier = model_util.get_model()