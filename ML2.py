import pandas as pd
from sklearn import linear_model  # SCIKIT LEARN LIBRARY
import math

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

reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']], df.price)
#print(reg.coef_) # all coefficients
# print(reg.intercept_) # y intercept
print(reg.predict([[2600, 3, 20]]))

#UserWarning: X does not have valid feature names, but LinearRegression was