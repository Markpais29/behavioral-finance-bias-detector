import yfinance as yf
import pandas as pd
from datetime import datetime

stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA',
          'NVDA', 'META', 'JPM', 'BAC', 'NFLX',
          'SPY']

start_date = '2019-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')

data = yf.download(stocks, start=start_date, end=end_date)

close = data['Close']
volume = data['Volume']

close = close.fillna(method='ffill')
volume = volume.fillna(0)

close.to_csv('close_prices.csv')
volume.to_csv('volumes.csv')

print("Data downloaded & saved")
