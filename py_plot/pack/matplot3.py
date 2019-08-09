'''
Created on 2019. 7. 30.

@author: acorn
'''
# 그래프의 종류
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

# fig = plt.figure()
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)
# ax1.hist(np.random.randn(10), bins=10, alpha=0.9) # alpha=0.9 : 투명도, 0에 가까울수록 투명도가 올라감.
# ax2.plot(np.random.randn(10))
# plt.show()

data = [50, 80, 100, 70, 90]

# bar plot
# plt.bar(range(len(data)), data)
# plt.show()

# (가로) bar plot
# error = np.random.rand(len(data)) # 신뢰구간값, 오차값, 편차값을 나타낼때 사용.
# plt.barh(range(len(data)), data, xerr=error, alpha=0.5)
# plt.show()

# pie(원형 파이) plot
# plt.pie(data, explode=(0, 0.1, 0, 0, 0), colors=['yellow','blue','red'])
# plt.show()

# box plot 
# plt.boxplot(data)
# plt.show()

# bubble plot
# n = 30
# np.random.seed(42)
# x = np.random.rand(n)
# y = np.random.rand(n)
# color = np.random.rand(n)
# scale = np.pi * (np.random.rand(n) * 15) ** 2
# plt.scatter(x, y, s=scale, c=color)
# plt.show()

from pandas import Series
sdata = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10)) # cumsum() : 누적합
print(sdata)
plt.plot(sdata)
plt.show()

import pandas as pd

fdata = pd.DataFrame(np.random.randn(1000, 4),
                     index=pd.date_range('1/1/2000', periods=1000), columns=list('abcd'))
fdata = fdata.cumsum()
print(fdata.head())
plt.plot(fdata)
plt.show()