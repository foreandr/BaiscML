import pandas as pd
import matplotlib.pyplot as plt
# LOAD CSV IN PANDAS DATAFRAME

df = pd.read_csv("testfile.csv")
first_column = df.iloc[:, 0] # MAKES NO ESNE?
second_column = df.iloc[:, 1]

print(first_column)
print(first_column)
# Plot scatterpot


plt.xlabel("")
plt.ylabel("")
plt.scatter(first_column, second_column, color ='red') #
plt.show()

#reg = linear_model.LinearRegression() # object for linear regression
#reg.fit(df[[first_column]], second_column) # TRAIN linear regression model
#reg.predict(np.array([3500]).reshape(1, 1))