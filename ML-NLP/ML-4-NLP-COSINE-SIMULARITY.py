from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

blob = TextBlob("John is learning natural language processing")
#for np in blob.noun_phrases:
    #print(np)

documents = (
"I like NLP",
"I am exploring NLP",
"I am a beginner in NLP",
"I want to learn NLP",
"I like advanced NLP"
)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
#compute similarity for first sentence with rest of the sentences
print(cosine_similarity(tfidf_matrix[0:1],tfidf_matrix))