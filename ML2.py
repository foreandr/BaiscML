import pandas as pd
from sklearn import linear_model  # SCIKIT LEARN LIBRARY
import math
import pickle

#JOBLIB MIGHT BE BETTER WITH BIG NUMPY ARRAYS

# column_names = ['area', 'bedrooms', 'age', 'price', 'Unnamed']
df = pd.read_csv("testfile.csv")
# print(df)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  # rRemove NAN column
# print(df)

df.columns = df.columns.str.strip()  # Something to do with whitespace

med_bed = math.floor(df.bedrooms.median())  # GetMedian
# print(med_bed)

# Assign med to ALL empty spots in bedroom
df.bedrooms = df.bedrooms.fillna(med_bed)  # doesn't work.
#print(df)

model = linear_model.LinearRegression()
model.fit(df[['area','bedrooms','age']], df.price)
#print(reg.coef_) # all coefficients
# print(reg.intercept_) # y intercept
print(model.predict([[2600, 3, 20]]))

with open('model_picke', 'wb') as f: # DUMPD pickle python model It's a binary file # WRITE BINARY
    pickle.dump(model, f)

with open('model_picke', 'rb') as f: # READBINARY
    model2 = pickle.load(f)
print(model2.predict([[2600, 3, 20]]))
#UserWarning: X does not have valid feature names, but LinearRegression was