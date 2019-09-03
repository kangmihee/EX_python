# [분류분석 문제1]
# 문1] 소득 수준에 따른 외식성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('testdata.txt', delimiter=' ')
print(data)
print(type(data))

data = data.drop(data.loc[(data['요일']!='토') & (data['요일']!='일')].index)
print(data)

# 학습데이터와 검정데이터 분류 7:3
train, test = train_test_split(data, test_size=0.3, random_state = 0) 
print(train.shape) # (14, 3)
print(test.shape)  # (7, 3)

formula = '외식유무 ~ 소득수준 ' 
result = smf.logit(formula=formula, data=train).fit()
print(result)
print(result.summary())

pred = result.predict(data)
print('추정값: \n', np.rint(pred))
