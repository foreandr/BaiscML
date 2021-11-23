#import tensorflow
import sklearn.linear_model
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model  # SCIKIT LEARN LIBRARY
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold # Litlte bit better separating our things, in a uniform way
from sklearn.model_selection import cross_val_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import seaborn as sn
import math
# import yahoo_fin.stock_info as si
# from yahoo_fin.stock_info import get_data
import yfinance

df = pd.read_csv("Datasets/dataset5.csv")

df['spam']=df['Category'].apply(lambda x:1 if x=='spam' else 0) # CREATES A NEW COLUMN SATISFYING



x_train, x_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)

V = CountVectorizer() # Params
X_train_count = V.fit_transform(x_train.values) # not sure

model = MultinomialNB()
model.fit(X_train_count, y_train) # X train count is the text converted into a number matrix

emails = [
    "Hello Andre, it's nice to see you again. I sure hope you'll get in touch with me about this personal email",
    "20% OFF FREE FLESHLIGHTS FOR EVERYBODY CALL NOW!!"
] # why didn't I have to change this to pass it in ?
emails_count = V.transform(emails) # not sure what transform does here
print(model.predict(emails_count)) # Accurately guesses
x_test_count_matrix = V.transform(x_test)
print(model.score(x_test_count_matrix, y_test)) # 98%

clf = Pipeline([ # 2 Step Pipeline in 2 steps
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB)
])

clf.fit(x_train, y_train)
print(clf.score(x_test,y_test))
