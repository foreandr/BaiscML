# import tensorflow
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model  # SCIKIT LEARN LIBRARY
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import math
# import yahoo_fin.stock_info as si
# from yahoo_fin.stock_info import get_data
import yfinance


# import matplotlib
def tickerUpper(ticker):
    return str(ticker.upper())


def getTicker(ticker):
    return yfinance.Ticker(tickerUpper(ticker))


msft = getTicker("msft")
msft_h = msft.history(period="1y")  # ALREADY A DATAFRAME
msft_h.columns.str.strip()

open_column = msft_h.iloc[:, 0]
close_column = msft_h.iloc[:, 3]
high_column = msft_h.iloc[:, 1]
low_column = msft_h.iloc[:, 2]
volume_column = msft_h.iloc[:, 4]
dividends_column = msft_h.iloc[:, 5]
stock_Splits_column = msft_h.iloc[:, 6]

Y = msft_h.Close # get the entire column of closing data
msft_h = msft_h.drop(['Close'], axis='columns') # Drop price table
X = msft_h[['Open', 'High', 'Low', 'Volume', 'Dividends', 'Stock Splits']]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.99)

model = linear_model.LinearRegression()
model.fit(x_train, y_train) # TRYING TO PREDICT CLOSING PRICE?

#print(model.predict(x_test))
#print(y_test)
print(model.score(x_test, y_test)) # 99 % ACCURACY???
