#import tensorflow
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model # SCIKIT LEARN LIBRARY

# LOAD CSV IN PANDAS DATAFRAME
df = pd.read_csv("testfile.csv")
print(df)
