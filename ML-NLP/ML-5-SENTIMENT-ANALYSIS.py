from textblob import TextBlob
import speech_recognition as sr
#================================================
#You want to do a sentiment analysis.
#Polarity = Polarity lies in the range of [-1,1] where 1 means a positive statement and -1 means a negative statement.
#Subjectivity = Subjectivity refers that mostly it is a public opinion and not factual information [0,1].

review = "I like this phone. screen quality and camera clarity is really good."

review2 = "This tv is not good. Bad quality, no clarity, worst experience"

#TextBlob has a pre trained sentiment prediction model
blob = TextBlob(review)
#print(blob.sentiment)