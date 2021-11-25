import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.svm import SVC

pd.set_option('display.max_columns', 500) # USEFUL FOR TERMINAL

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

df0 = df[df.target==0]
df1 = df[df.target==1]
df2 = df[df.target==2]

#print(df.head())
Y = df['target']
X = df.drop(['target' ], axis='columns')

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
model = SVC() # Can change parameters here
model.fit(x_train, y_train)
print(model.score(x_test,y_test)) # It is perfect I don't like that


