from sklearn import linear_model  # SCIKIT LEARN LIBRARY
import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("Datasets/testfile2.csv")
df.columns = df.columns.str.strip()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
dummies = pd.get_dummies((df.town))
merged = pd.concat([df, dummies], axis='columns')
final = merged.drop(['town', '\'west windsor\''], axis='columns')

X = final[['area','\'monroe township\'','\'robbinsville\'']]
Y = final['price']

# SPLT DATASET, CHOOSE HOW MUCH
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

model = linear_model.LinearRegression()
model.fit(x_train, y_train)
print(model.predict(x_test))
print(y_test)
print(model.score(x_test,y_test))
