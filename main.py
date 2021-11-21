#import tensorflow
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model # SCIKIT LEARN LIBRARY

# LOAD CSV IN PANDAS DATAFRAME
df = pd.read_csv("testfile.csv")
#first_column = df.iloc[:, 0] # MAKES NO ESNE?
second_column = df.iloc[:, 1]
# Plot scatterpot


plt.xlabel("")
plt.ylabel("")
plt.scatter(df.area, second_column, color ='red') #
plt.show()

reg = linear_model.LinearRegression() # object for linear regression
reg.fit(df[['area']], second_column) # TRAIN linear regression model