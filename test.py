#Testing Grounds
import yfinance
import requests_cache
#First we need to understand what we're going to do.
#One module of The Turk MUST include the ability to fetch ALL stock data.

#We must have a tickers list that is sorted from A - Z
#And must also have info beside such as sector (APPL, Technology) in order to easily query
tickers = ["AAPL", "BTC"]

#We must have a currency to compare the data with such as USD, GBP
dovuz = "USD" # veya GBP

session = requests_cache.CachedSession('yfinance.cache')
session.headers['User-Agent'] = 'theturk'
ticker = yfinance.Ticker("msft", session=session)


txt = ""

for key, value in ticker.info.items():
    txt += f"{key} - {value}\n"

with open("test.txt", "w") as file:
    file.write(txt)