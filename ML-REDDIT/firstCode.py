import nltk
from matplotlib import pyplot as plt

import helper
# open file populate array with text

full_list = helper.readFile('file.txt')

frequency_dist = nltk.FreqDist(full_list) # Frequency distribution

twoDVec = helper.populateArray(frequency_dist) # 1d vector of words

frequency2 = nltk.FreqDist(twoDVec) # frequency dist of words

newlist = helper.returnSentimentList(full_list) # all comments with some zing on em

x_polarity = []
y_subjectivity = []

for i in newlist:
    x_polarity.append(i.sentiment.polarity)
    y_subjectivity.append(i.sentiment.subjectivity)

plt.scatter(x_polarity, y_subjectivity)
# As the sentiment rises, the polarity widens
# obviously
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()
