# 회귀분석(독립변수:연속형, 종속변수:연속형) 방법들 : 맛보기

import statsmodels.api as sm
from sklearn.datasets import make_regression # regression : 회귀
import numpy as np
from sklearn.cluster.tests.test_k_means import n_samples

np.random.seed(12)

#############################################################

# 방법 1 : make_regression - Model X
print('방법 1 :','***'*20,'\n')

x, y, coef = make_regression(n_samples=50, n_features=1, bias=100, coef=True) # coef=True : 기울기 반환
print('x:',x[0])
print('y:',y[0])
print('coef(기울기):',coef) # 기울기:89.47430739278907

# y = wx + b
ypred = 89.47430739278907 * -1.70073563 + 100
print('ypred:',ypred)

ypred_new = 89.47430739278907 * 5.0 + 100
print('ypred_new:',ypred_new)

x1 = x # 실습때사용
y1 = y

#############################################################

# 방법 2 : LinearRegression - Model O
print('\n\n방법 2 :','***'*20,'\n')

from sklearn.linear_model import LinearRegression
model = LinearRegression()
print('\n',model)

fit_model = model.fit(x1,y1) # 학습데이터로 모형 추정
print('\n기울기:',fit_model.coef_)    # 기울기 : 89.47430739
print('절편:',fit_model.intercept_)  # 절편 : 100.0

y_pred = fit_model.predict(x1)
print('\n\ny_pred:\n',y_pred)

print('\n새로운 값으로 예측결과 얻기 -----------------')
x_new, _, _ = make_regression(n_samples=5, n_features=1, bias=100, coef=True)
print('x_new:\n',x_new)
y_pred_new = fit_model.predict(x_new)
print('\ny_pred_new:\n',y_pred_new)


#############################################################

# 방법 3 : ols - Model O
print('\n\n방법 3 :','***'*20,'\n\n')

import statsmodels.formula.api as smf
import pandas as pd

x1 = x.flatten()
print('x1.shape:',x1.shape)
y1 = y
print('y1.shape:',y1.shape)

data = np.array([x1, y1])
df = pd.DataFrame(data.T)
df.columns = ['x1','y1']
print('\ndf:\n',df.head(5))

model2 = smf.ols(formula='y1 ~ x1', data = df).fit()
print(model2.summary()) # 절편(Intercept) : 100.0,  기울기(coef) : 89.4743
print(model2.predict()[0]) # 예측값(y, ypred와 같은값)



# 새로운 값으로 예측 
print('\n-------------새로운 값으로 예측------------- ')
print('\nx1 : ', x1[:2])
new2 = pd.DataFrame({'x1':[-1.7, 0.8]})
y_pred_new2 = model2.predict(new2)
print('\n예측값:\n',y_pred_new2)




























