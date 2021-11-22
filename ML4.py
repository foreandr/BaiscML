import pandas as pd
from sklearn import linear_model  # SCIKIT LEARN LIBRARY


df = pd.read_csv("testfile2.csv")
df.columns = df.columns.str.strip()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  # Remove NAN column
# print(df)

# One hot encoding
dummies = pd.get_dummies((df.town))
# print(dummies)

# Put dataframes togehter
merged = pd.concat([df, dummies], axis='columns')
#print(merged)

# Drop original town column
# DROP 1 DUMMY VARIABLE ALWAYS ??
final = merged.drop(['town', '\'west windsor\''], axis='columns') # NOTICE CHANGE IN SECOND TEST
#print(final)

model = linear_model.LinearRegression()
x = final.drop('price', axis='columns')
x = x.loc[:, ~df.columns.str.contains('^Unnamed')]  # Remove NAN column
#print(x)
y = final.price
model.fit(x, y)
#print(model.predict([[3400, 0, 0]]))
#print(model.score(x, y)) # ACCURACY %


#------------------------------------------------------