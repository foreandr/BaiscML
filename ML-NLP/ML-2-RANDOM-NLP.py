import nltk
string = 'adf;ahsdfkljanpewi;fbnap;s dbnfp;iak;ajfpi anpiahn890p4hnp10f89nf1 490p8hnfe13 nfdiopahf08971h80 f13nb08gf1bnrfiub df1807fb 18bfdksjobf10873bf' #dict
frequency_dist = nltk.FreqDist(string)
print(frequency_dist.pprint())

large_words = dict([(k,v) for k,v in frequency_dist.items() if len(k)>3])
frequency_dist = nltk.FreqDist(large_words)
#frequency_dist.plot(50,cumulative=False) # useful not working

from wordcloud import WordCloud
wcloud = WordCloud().generate_from_frequencies(frequency_dist)
import matplotlib.pyplot as plt
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off") (-0.5, 399.5, 199.5, -0.5)
plt.show()
