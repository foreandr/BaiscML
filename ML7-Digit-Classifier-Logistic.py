import matplotlib.pyplot as plt
from sklearn import linear_model  # SCIKIT LEARN LIBRARY
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix
import seaborn as sn

digits = load_digits()

#print(digits.data[0])

# SHOW 8 BY 8 IMAGE
#plt.gray()
#plt.matshow(digits.images[0])
#plt.show()

x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)
model = linear_model.LogisticRegression(max_iter=10000)
model.fit(x_train, y_train)
y_predicted = model.predict(x_test)

cm = confusion_matrix(y_test, y_predicted) # WTF IS THIS?
plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True)
plt.xlabel("prdicted")
plt.ylabel('Truth')
plt.show()

print(model.score(x_test,y_test))

#print(digits.data[0:10])
print(model.predict(digits.data[0:10]))






