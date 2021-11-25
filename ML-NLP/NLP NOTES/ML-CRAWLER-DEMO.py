import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import pytesseract # THINGS FOR READING IMAGES WITH TEXT AND READING THE TEXT ON THEM #captcha defeater?
#import socks # for rerouting traffic - USE IN CONJUNCTION WITH TOR
import socket
class Content:
    """
    Common base class for all articles/pages
    """
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def getPage(url):
        req = requests.get(url)
        return BeautifulSoup(req.text, 'html.parser')

    def print(self):
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))

class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
    def safeGet(self, pageObj, selector):
        """
        Utility function used to get a content string from a
        Beautiful Soup object and a selector. Returns an empty
        string if no object is found for the given selector
        """
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join(
        [elem.get_text() for elem in selectedElems])
        return ''
    def parse(self, site, url):
        """
        Extract content from a given page URL
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
