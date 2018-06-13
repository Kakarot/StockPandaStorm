import pandas_datareader.data as web
import pandas_datareader
from datetime import datetime

start = datetime(2018, 3, 12)
end = datetime(2018, 6, 12)


print("Displaying trade data for last executions on IEX. Provides last sale price, size and time.\n")
lastTradeData = pandas_datareader.get_last_iex()
print(lastTradeData)


#Garbage code because I'm full of bad practice while learning
#f = web.DataReader('F', 'iex', start, end)
#f = web.IEXLasts(symbols='AGS', start= start, end= end)
#f = pandas_datareader.data.DataReader('F', 'iex', start, end)
#g = pandas_datareader.get_iex_symbols()

#print(f)
#print(g)
