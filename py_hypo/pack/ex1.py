# 도수분포표 : 특정구간에 속하는 자료의 수를 나타낸 표

import pandas as pd
from pandas import DataFrame

frame = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ex_studentlist.csv')
print(frame)
print('\n',frame.info())
print('\n',frame.describe())

data1 = frame.groupby(['bloodtype'])['bloodtype'].count()
print('\n',data1)

data2 = pd.crosstab(index=frame['bloodtype'], columns="count")
print('\n',data2)

data3 = pd.crosstab(index=frame['bloodtype'], columns=frame['sex'])
print('\n bloodtype, sex, count : \n',data3)

data4 = pd.crosstab(index=frame['bloodtype'], columns=frame['sex'], margins=True)
print('\n bloodtype, sex, count : \n',data4)

