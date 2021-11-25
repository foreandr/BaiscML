import requests
import helper
import csv
import pandas as pd
from textblob import TextBlob
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# fill text file with comments
#helper.createListOfComments(helper.wanted_subreddit1)

# open file populate array with text
full_list = helper.readFile('file.txt')

frequency_dist = nltk.FreqDist(full_list)
twoDVec = []

twoDVec = helper.populateArray(frequency_dist)

frequency2 = nltk.FreqDist(twoDVec)


helper.printSentimentList(full_list)


