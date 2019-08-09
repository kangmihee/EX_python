# 회귀분석 문제 2) 
# github.com/pykwon/python에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.
#   - 국어 점수를 입력하면 수학 점수 예측
#   - 국어, 영어 점수를 입력하면 수학 점수 예측

import pandas as pd
import statsmodels.formula.api as smf 
import numpy as np
import statsmodels.api
import matplotlib.pyplot as plt

df = pd.read_csv("../testdata/student.csv")

kor_score = float(input('국어점수 : '))
eng_score = float(input('영어점수 : '))

# 국어 점수를 입력하면 수학 점수 예측
result = smf.ols(formula='수학 ~ 국어', data=df).fit()
print(result.summary().tables[1])

# 국어, 영어 점수를 입력하면 수학 점수 예측
result2 = smf.ols(formula='수학 ~ 국어 + 영어', data=df).fit()
print(result2.summary().tables[1])

print('국어 점수를 입력한  수학 점수 예측 :', 0.5705 * kor_score + 32.1069)
print('국어,영어 점수를 입력한 수학 점수 예측 :', (0.5942 * eng_score) + (0.1158 * kor_score) + 22.6238)


