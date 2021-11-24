from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup as bs, BeautifulSoup


# FUNCTIONS
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    print(title)

html2 = urlopen('http://www.pythonscraping.com/pages/page1.html')
'''
# ANOTHER POPULAR PARSER
#pip3 install lxml

try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')
'''
getTitle('http://www.pythonscraping.com/pages/page1.html')
