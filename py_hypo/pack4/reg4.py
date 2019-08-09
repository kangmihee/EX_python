# statsmodels.formula.api 가 제공하는 ols() 함수 : 가장 기본적인 결정론적 선형회귀 방법

import pandas as pd
import statsmodels.formula.api as smf 
import numpy as np

df = pd.read_csv("../testdata/drinking_water.csv")
print(df.head())
print(df.corr()) # r(상관계수)확인

model = smf.ols(formula='만족도 ~ 적절성', data = df).fit() #만족도(종속변수), 적절성(독립변수)
print(model.summary())

print('\n회귀계수 : \n',model.params)
print('\n결정계수 : \n',model.rsquared)
print('\np값 : \n',model.pvalues)
print('\n모델에 의헤 예측된 값 : \n',model.predict()[0:5]) #[3.73 2.99 3.73 2.25 2.25]
print('\n실제 값 : \n',df['만족도'].head())             # 3 2 4 2 2

from matplotlib.pylab import plt
plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도, 1) # 1차원?
plt.plot(df.적절성, df.적절성  * slope + intercept,'b') # slope:기울기, intercept:절편
plt.show()

# 다중 회귀 선형회귀모델
model2 = smf.ols(formula='만족도  ~ 적절성 +친밀도', data=df).fit()
print(model2.summary()) # 0.05보다 크면 독립변수로 사용x














