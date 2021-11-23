import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

df = pd.read_csv("Datasets/dataset5.csv")

df['spam']=df['Category'].apply(lambda x:1 if x=='spam' else 0) # CREATES A NEW COLUMN SATISFYING



x_train, x_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)

V = CountVectorizer() # Params
X_train_count = V.fit_transform(x_train.values) # not sure

model = MultinomialNB()
model.fit(X_train_count, y_train) # X train count is the text converted into a number matrix

emails = [
    "Hello Andre, it's nice to see you again. I sure hope you'll get in touch with me about this personal email",
    "20% OFF FREE FLESHLIGHTS FOR EVERYBODY CALL NOW!!"
] # why didn't I have to change this to pass it in ?
emails_count = V.transform(emails) # not sure what transform does here
print(model.predict(emails_count)) # Accurately guesses
x_test_count_matrix = V.transform(x_test)
print(model.score(x_test_count_matrix, y_test)) # 98%

clf = Pipeline([ # 2 Step Pipeline in 2 steps
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB)
])

clf.fit(x_train, y_train) # error in this code somewhere
print(clf.score(x_test,y_test))