import re
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


pages = set()
# CHANGE THE RECUSRION COUNTER MANUALLY OR PYTHON WILL AUTO STOP AT 100
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')): # Enter what you want searched here?
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
#getLinks('')

pages = set()
def getLinks2(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span')
        .find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks2('')

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
#getTitle('http://www.pythonscraping.com/pages/page1.html')


html2 = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html2, 'html.parser')
#for child in bs.find('table',{'id':'giftList'}).children:
    #print(child)


images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
#for image in images:
#    print(image['src']) # wonder if I could save these images
