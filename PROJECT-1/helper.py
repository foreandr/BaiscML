import yfinance as yf
import matplotlib
import time
def tickerUpper(ticker):
    return str(ticker.upper())
def getTicker(ticker):
    return yf.Ticker(tickerUpper(ticker))






