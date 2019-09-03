# [분류분석 문제2] 
# 게임,TV시청 데이터로 안경유무를 분류하시오.
# 안경 : 값1(착용X), 값2(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('../testdata/bodycheck.csv')
data['안경유무'] = data['안경유무'].map({1:0, 2:1}) # 착용X = 0, 착용O = 1
print(data)

formula = '안경유무  ~ 게임  + TV시청'

result = smf.glm(formula=formula, data=data).fit()
print(result.summary())

pred = result.predict(data)
print('추정값 : \n',np.around(pred))
