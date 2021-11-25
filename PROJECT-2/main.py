import helper
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import nltk
from textblob import TextBlob


finviz_URL = 'https://finviz.com/quote.ashx?t='
tickers=['AMZN', 'MSFT', 'AMD']


news_tables = {}
for ticker in tickers:
    url = finviz_URL + ticker
    req = Request(url=url, headers={'user-agent':'my-app'})
    response = urlopen(req)

    html = BeautifulSoup(response, features="lxml") # ("lxml")

    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table
#    print(html)

#for i in news_tables:
#    print(i)

amzn_data = news_tables['AMZN']
amzn_rows = amzn_data.findAll('tr')# not sure what tr is
#print(amzn_rows)


for i in amzn_rows:
    text = (i.a.text) # go through the html tag | index-><a> -> .text
    timestamp = i.td.text
    print(timestamp + ": " + text)
