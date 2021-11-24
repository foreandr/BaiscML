import sklearn
import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model  # SCIKIT LEARN LIBRARY
df = pd.read_csv("Datasets/dataset.csv")
df.columns = df.columns.str.strip()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.head()
# plt.scatter(df.satisfaction_level, df.salary)
# plt.show()

#print(df.shape)
# (11175, 10)

x_train, x_test, y_train, y_test = train_test_split(df[['satisfaction_level', 'last_evaluation', 'number_project',
                    'average_montly_hours', 'time_spend_company', 'Work_accident', 'salary',
                    'promotion_last_5years']], df.left, test_size=0.2) # TOOK OUT ONE OF THE COLUMNS

model = sklearn.linear_model.LogisticRegression(max_iter=1000000) # changing max iter allows bigger regression

model.fit(x_train, y_train) # execute to train

print(model.score(x_test,y_test)) # yikes

# SIGMOID FUNCTION
# RETURN A NUMBER BETWEEN 0 AND 1
# LOGISTIC REGRESSION NT REAL VALUE OUTPUT
# Feed linear equation to sigmoid function
# CLASSIFICATION
# binary classification 1 || 0