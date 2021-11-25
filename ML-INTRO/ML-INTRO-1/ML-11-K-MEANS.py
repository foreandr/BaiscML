# K is a free parameter
# how to determine proper number of k\
# BIG MISTAKE SOMEWHERE IN HERE

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('Datasets\\dataset4.csv')
#plt.scatter(df['Age'], df['Income($)'])
#plt.show()

Y = df['Income($)']

km = KMeans(n_clusters=3) # NUMBER OF CLUSTERS
y_predicted = km.fit_predict(df[['Age', 'Income($)']]) # FIT AND PREDICT SAME TIME
#print(y_predicted)

df['cluster'] = y_predicted

df0 = df[df.cluster == 0]
df1 = df[df.cluster == 1]
df2 = df[df.cluster == 2]
plt.scatter(df0.Age, df0['Income($)'], color='green')
plt.scatter(df1.Age, df1['Income($)'], color='blue')
plt.scatter(df2.Age, df2['Income($)'], color='red')
#plt.show()

scalar = MinMaxScaler()
scalar.fit(df[['Income($)']]) # scale 0-1
df['Income($)'] = scalar.transform(df[['Income($)']]) # NEED DOUBLE ARRAY
#print(df)

scalar.fit(df[['Age']]) # scale 0-1
df.Age = scalar.transform(df[['Age']])
#print(df)

km2 = KMeans(n_clusters=3)
y_predicted2 = km.fit_predict(df[['Age', 'Income($)']])
df['cluster'] = y_predicted2
print(df)

df0 = df[df.cluster == 0]
df1 = df[df.cluster == 1]
df2 = df[df.cluster == 2]
plt.scatter(df0.Age, df0['Income($)'], color='green')
plt.scatter(df1.Age, df1['Income($)'], color='blue')
plt.scatter(df2.Age, df2['Income($)'], color='red')
plt.show()

