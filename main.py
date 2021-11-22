# import tensorflow
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model  # SCIKIT LEARN LIBRARY
import math

df = pd.read_csv("testfile2.csv")
df.columns = df.columns.str.strip()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  # rRemove NAN column
# print(df)

# One hot encoding
dummies = pd.get_dummies((df.town))
# print(dummies)

# Put dataframes togehter
merged = pd.concat([df, dummies], axis='columns')
print(merged)

# Drop original town column
# DROP 1 DUMMY VARIABLE ALWAYS ??
final = merged.drop(['town', 'robbinsville'], axis='columns')
print(final)
