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
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold # Litlte bit better separating our things, in a uniform way
from sklearn.model_selection import cross_val_score
import seaborn as sn
import math
# import yahoo_fin.stock_info as si
# from yahoo_fin.stock_info import get_data
import yfinance



