# Created by Amandeep at 6/15/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

import pandas as pd
import numpy as np
from sklearn.feature_selection import chi2
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.pipeline import Pipeline


class ModelUtil:
    model = None

    def __init__(self):
        pass

    def get_model(self):
        if self.model == None:
            self.train_model()
        return self.model

    def train_model(self):
        df = pd.read_csv("shuffled-full-set-hashed.csv", header=None)
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


model_util = ModelUtil()
classifier = model_util.get_model()