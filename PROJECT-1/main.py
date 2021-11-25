import matplotlib
import helper
import myFunctions
import yfinance as yf
from matplotlib import pyplot
import pandas as pd
from sklearn import linear_model
# PLOTS
myPlot = matplotlib.pyplot
msft = myFunctions.getTicker('msft')

msft_history = msft.history(period="max")
# print(type(msft_history)) # Dataframe
#print(msft_history)

# AI operations
df = msft_history


#for i in msft_history:
#    print(i)


myFunctions.plotChart(myPlot, msft_history, "red",msft ,"Stocks")
#myPlot.show()