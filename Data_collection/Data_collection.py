import yfinance as yf
import pandas as pd

data = yf.download('RELIANCE.NS')

print(data)

data.to_csv('RELIANCE-NS.csv')

equity_details = pd.read_csv('EQUITY_L.csv')


equity_details.SYMBOL

for name in equity_details.SYMBOL[:]:
    try:
        data=yf.download(f'{name}.NS')
        data.to_csv(f'../Data/{name}.csv')
    except Exception as e:
        print(f'{name} ===> {e}')
