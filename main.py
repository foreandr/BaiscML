# import tensorflow
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

import seaborn as sn
import math
# import yahoo_fin.stock_info as si
# from yahoo_fin.stock_info import get_data
import yfinance


digits = load_digits()

df = pd.DataFrame(digits.data)
df['target'] = digits.target

x_train, x_test, y_train, y_test = train_test_split(df.drop(['target'],axis='columns'), df['target'], test_size=0.2)
model = RandomForestClassifier(n_estimators=100) # can change to all kinds of things
model.fit(x_train, y_train)
print(model.score(x_test, y_test))



