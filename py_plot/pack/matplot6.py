'''
Created on 2019. 7. 30.

@author: acorn
'''
# yahoo가 제공하는 주식시세
import pandas as pd
from pandas_datareader import data

kosdaq = pd.read_pickle('kosdaq.pickle')
kospi = pd.read_pickle('kospi.pickle')
print(kosdaq.head())
print(kospi.head())
print()

start_date = '2018-01-01'
tickers = ['003380.KQ','251270.KS'] # 제일홀딩스, 넷마블게임즈
holding_df = data.get_data_yahoo(tickers[0], start_date)
net_df = data.get_data_yahoo(tickers[1], start_date)

print('제일 홀딩스 주식 : \n', holding_df.head(3), '\n')
print('넷마블 게임즈 주식 : \n', net_df.head(3))

holding_df.to_pickle('./holding.pickle')
net_df.to_csv('./net.csv')
net_df.to_excel('./net.xlsx')

import matplotlib.pyplot as plt
plt.plot(net_df)
plt.show()

plt.plot(holding_df)
plt.show()