from sklearn import linear_model  # SCIKIT LEARN LIBRARY
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold # Litlte bit better separating our things, in a uniform way
from sklearn.model_selection import cross_val_score

def get_score(model, x_train, x_test, y_train, y_test ):
    model.fit(x_train, y_train)
    return model.score(x_test, y_test)

digits = load_digits()
Y = digits.target
#digits = digits.drop(['target'], axis='columns')
X = digits.data
#x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

model = linear_model.LinearRegression()
model2 = linear_model.LogisticRegression(max_iter=1000000)
model3 = SVC()

# SAME METHODS HERE MORE OR LESS
kf = KFold(n_splits=10) # HOW MANY ITERATIONS
folds = StratifiedKFold(n_splits=3) # could change these

scores_l = []
scores_svm = []
scores_rf = []

for train_index, test_index in kf.split(digits.data):
    x_train, x_test, y_train, y_test = digits.data[train_index], digits.data[test_index], digits.target[train_index], digits.target[test_index]
    scores_l.append(get_score(model,x_train, x_test, y_train, y_test))
    scores_svm.append(get_score(model2, x_train, x_test, y_train, y_test))
    scores_rf.append(get_score(model3, x_train, x_test, y_train, y_test))

print(scores_l)
print(scores_svm)
print(scores_rf)

print(cross_val_score(model), digits.data, digits.target)


