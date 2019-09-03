# 날씨관련정보로 내일 비 여부 확인 분류

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/weather.csv')
print(data.head(2))
print(data.shape)   # (366, 12)

data2 = pd.DataFrame()
data2 = data.drop(['Date', 'RainToday'], axis = 1) # 필요없는 columns삭제
print(data2.head(2))

data2['RainTomorrow'] = data2['RainTomorrow'].map({'Yes':1, 'No':2}) # 데이터 변경
print(data2.head(2))

# 학습데이터와 검정데이터 분류 7:3
train, test = train_test_split(data2, test_size=0.3, random_state = 0) # random_stats = 0 : 랜던값 으로 추출된 값 고정
print(train.shape) # (256, 10)
print(test.shape)  # (110, 10)

#my_formula = 'RainTomorrow ~ MinTemp + MaxTemp + Rainfall + ...' 
#my_formula = 'RainTomorrow ~ MinTemp + MaxTemp + Cloud' 
columns_select = "+".join(train.columns.difference(['RainTomorrow'])) # RainTomorrow를 제외한 모든 columns를 사용
my_formula = 'RainTomorrow ~ ' + columns_select
print(my_formula)

#result = smf.glm(formula = my_formula, data = train, family = sm.families.Binomial()).fit()
result = smf.logit(formula=my_formula, data=train).fit()
print(result)
print(result.summary())
print(result.params)

import numpy as np
pred = result.predict(test)
#print('추정값: \n', np.rint(result.predict(test))) # 0 또는 1로 보이기
print('추정값: \n', np.rint(pred[:5]))

# 정확도 확인 
from sklearn.metrics import accuracy_score
conf_tab = result.pred_table()
print('\nconfusion matrix :\n', conf_tab)
print('분류정확도 : ', (conf_tab[0][0] + conf_tab[1][1])/ len(data2)) # 약61% (독립변수 조정  필요)

