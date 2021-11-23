import tensorflow # released by Google
import keras
import sklearn.linear_model
import torch # Facebook
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

(x_train, x_test), (y_train, y_test) = keras.datasets.mnist.load_data() # Get minist dataset
print(x_train[0]) # print one instance as array
#plt.matshow(x_train[0])
#plt.show()

#flatten 2d array into 1d array
x_train_flattened = x_train.reshape(len(x_train), 28 * 28)
x_test_flattened = x_test.reshape(len(x_test), 28 * 28)

# Create neural network
'''
1. Sequential means it's a stack in
2. 
3.
'''
model = keras.Sequential([
    keras.layers.Dense(10, (784,), activation='sigmoid') # Every layer is connecter with every other layer
])
'''
1.Adam helps train efficiently
2. sparse_categorical_crossentropy
    Output class is categories?
    mean_squarred_error is what I normally use
3.
'''
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy', # weird loss function
    metrics=['accuracy']
)
model.fit(x_test_flattened, x_test_flattened, epochs=5) # Epochs new parameter


