from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
# one hot encoding
text = ["I love NLP and I will learn NLP in 2month "]
Text = "I am learning NLP"

vectorizer = CountVectorizer()
vectorizer.fit(text)

# encode document
vector = vectorizer.transform(text)

# summarize & generating output
print(vectorizer.vocabulary_)
print(vector)

df = pd.get_dummies(Text.split()) # dummy tables for each char
#print(df.head())