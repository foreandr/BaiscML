import urllib.request as urllib2
import nltk
from bs4 import BeautifulSoup # for pulling data out fo HTML AND XML # HAD TO FORCE REINSTALL
import requests
import re
import pandas as pd
from pandas import Series, DataFrame
from ipywidgets import FloatProgress
from IPython.display import display
from time import sleep
import pickle
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import speech_recognition as sr
from gtts import gTTS

