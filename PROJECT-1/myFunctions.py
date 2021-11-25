'''
Coder:
Date:
Post:
'''

import yfinance


# import matplotlib
def tickerUpper(ticker):
    return str(ticker.upper())


def getTicker(ticker):
    return yfinance.Ticker(tickerUpper(ticker))


'''
 :param myPlot_: 
 :param tickerHistory: 
 :param color: 
 :param ticker: 
 :return: 
 '''
def plotChart(myPlot_, tickerHistory, color, ticker, priceType, operator="", num = 0):
    # get stock info
    # I WOULD ALSO LIKE TO ADD , label="line2" AT THE END, but it doesn't work...
    # tickerHistory['Close'].plot(figsize=(16, 9), color=str(color), label="line2" ) # This line is ambiguous
    if (operator == "NO OPERATOR"):
        num = ""
    '''
    Line Explanation because this is extremely confusion to me even though I wrote it.
    1. [close] is a key to tickerHistory.
    2. .plot is a function in matplot lib.
    3. remove both ends is a function that removes specified stuff from an entered string.
    4. convert ticker obj to string to be parsed in the function
    '''
    tickerHistory['Close'].plot(label=f"{removeBothEnds(str(ticker), '>', '<')}", figsize=(10, 9), color=str(color))

    # tickerHistory['Close'].plot(label="tiddies") # THIS CHANGES THE COLOR??
    myPlot_.legend(loc='best')
    myPlot_.ylabel(f"{priceType} Price")
    myPlot_.xlabel("Date")


# changeh

def downloadCSV(ticker):
    data_df = yfinance.download(tickerUpper(ticker), start="2020-02-01", end="2020-03-20")  # timeframe
    data_df.to_csv(ticker + '.csv')


def getHistory_Y(years):
    return str(years) + "y"

def getHistory_M(months):
    return str(months) + "m"

def getHistory_D(days):
    return str(days) + "d"




def getStringUntil(string, target):
    data1 = ""
    for i in string:
        if (i != target):
            data1 += i
        else:
            #print(data1)
            return data1
    #print(data1)
    return data1

def getStringBegin(string, target):  # Would prefer to do a reverse for loop
    data2 = string.split(str(target), 1)[1]
    #print(data2)
    return data2

def removeBothEnds(string, end, beginning): # CHANGE FROM BEGINNING TO END SOMEHOW
    string_ = getStringUntil(string, end)
    #print(string_)
    string_2 = getStringBegin(string_, beginning)
    #print(string_2)
    return string_2
