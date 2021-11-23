import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier


digits = load_digits()

df = pd.DataFrame(digits.data)
df['target'] = digits.target

x_train, x_test, y_train, y_test = train_test_split(df.drop(['target'],axis='columns'), df['target'], test_size=0.2)
model = RandomForestClassifier(n_estimators=100) # can change to all kinds of things
model.fit(x_train, y_train)
print(model.score(x_test, y_test))
