import urllib.request as urllib2
from bs4 import BeautifulSoup # for pulling data out fo HTML AND XML # HAD TO FORCE REINSTALL
import requests
import re
import pandas as pd
from pandas import Series, DataFrame
from ipywidgets import FloatProgress
from IPython.display import display
from time import sleep
import pickle
'''
reinstall command 
pip install beautifulsoup4 --force-reinstall
'''

response = urllib2.urlopen("https://en.wikipedia.org/wiki/Natural_language_processing")

html_doc = response.read() #html_doc now contains entire html string as bytes
soup = BeautifulSoup(markup=html_doc, features='html.parser') # formatted html code now | type bs4

#print(type(soup))
#print(soup)


# Formating the parsed html file
strhtm = soup.prettify()

#FIND all instances of a particular string TAG tag that
#for x in soup.find_all('div'): print(x.string)



