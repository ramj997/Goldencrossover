
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
"""
# reading csv file
# try to take input from user

data = pd.read_csv('../Data collection/Data/3IINFOLTD.csv')

# data wrangling
# dropping unwanted column and rows, changing names, getting data in required format

data = data.drop(index=[0, 1])
data = data.rename(columns={'Price': 'Date'})
data['Date'] = pd.to_datetime(data['Date'])
data['Date'] = data['Date'].dt.date
data = data.set_index('Date')
data = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
tochange = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
data[tochange] = data[tochange].apply(pd.to_numeric, errors='coerce')

# plotting data
data[-400:].Close.plot(figsize=(15, 8))
"""

# Golden Crossover
# when a 20-day simple moving average (SMA) crosses above a 50-day SMA, it's a buy signal, and when the 50-day SMA crosses above the 20-day SMA, it's a sell signal


def GoldenCrossverSignal(name, data_point):
    path = f'../Data/{name}.csv'
    # data = pd.read_csv(path, parse_dates=['Date'], index_col='Date')
    data = pd.read_csv(path)
    data = data.drop(index=[0, 1])
    data = data.rename(columns={'Price': 'Date'})
    data['Date'] = pd.to_datetime(data['Date'])
    data['Date'] = data['Date'].dt.date
    data = data.set_index('Date')
    data = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
    tochange = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    data[tochange] = data[tochange].apply(pd.to_numeric, errors='coerce')

    data['20_SMA'] = data.Close.rolling(window=20, min_periods=1).mean()
    data['50_SMA'] = data.Close.rolling(window=50, min_periods=1).mean()
    data['Signal'] = 0
    data['Signal'] = np.where(data['20_SMA'] > data['50_SMA'], 1, 0)
    data['Position'] = data.Signal.diff()
    plt.figure(figsize=(20, 10))
    # plot close price, short-term and long-term moving averages
    data.iloc[-data_point:]['Close'].plot(color='k', label='Close Price')
    data.iloc[-data_point:]['20_SMA'].plot(color='b', label='20-day SMA')
    data.iloc[-data_point:]['50_SMA'].plot(color='g', label='50-day SMA')
    # plot ‘buy’ signals
    plt.plot(data.iloc[-data_point:][data.iloc[-data_point:]['Position'] == 1].index,
             data.iloc[-data_point:]['20_SMA'][data.iloc[-data_point:]['Position'] == 1],
             '^', markersize=15, color='g', label='buy')
    # plot ‘sell’ signals
    plt.plot(data.iloc[-data_point:][data.iloc[-data_point:]['Position'] == -1].index,
             data.iloc[-data_point:]['20_SMA'][data.iloc[-data_point:]['Position'] == -1],
             'v', markersize=15, color='r', label='sell')
    plt.ylabel('Price in Rupees', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    plt.title(name, fontsize=20)
    plt.legend()
    plt.grid()
    plt.show()
    df_pos = data.iloc[-data_point:][(data.iloc[-data_point:]['Position'] == 1) | (data['Position'] == -1)].copy()
    df_pos['Position'] = df_pos['Position'].apply(lambda x: 'Buy' if x == 1 else 'Sell')
    print(tabulate(df_pos[['Close', 'Position']], headers='keys', tablefmt='psql'))


GoldenCrossverSignal('ALPA', 900)












