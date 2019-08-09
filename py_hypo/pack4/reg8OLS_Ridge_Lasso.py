# LuneaeRegression의 기본 알고리즘은 OLS (최소제곱법) - 정규화 선형회귀 방법은 모형이 과도하게 최적화 됨(overFiting)
# Ridge : 가중치들의 제곱합을 최소화
# Lasso : 가중치의 절대값 합의 최소화
# ElasticNet : 가중치의 절대값과 제곱합을 동시에 제약조건으로 사용

# iris
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression as lm
import matplotlib.pyplot as plt


iris = load_iris()
print(iris.data)
print(iris.feature_names)
print(iris.target)
print(iris.target_names)

iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
iris_df['target'] = iris.target
iris_df['target_names'] = iris.target_names[iris.target]
print(iris_df.head(3),'\n')


# train dataset(학습데이터), test dataset(검정데이터)로 데이터 분리 (7:3)
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(iris_df, test_size = 0.3)

print('train:',train_set.shape) # 105
print('test:',test_set.shape)  # 45
print()

#----------------------------------------
# 선형회귀분석방법1 - 선형회귀(최소제곱) OLS 알고리즘을 사용

model_ols = lm().fit(X=train_set.iloc[:,[2]], y=train_set.iloc[:,[3]]) # 대문자로 작성
#print(model_ols.coef_)
#print(model_ols.intercept_)
#print('ols predict : \n',model_ols.predict(test_set.iloc[:,[2]])) # 생성괸 모델 검증
#print('실제값:\n', train_set.iloc[:,[3]])

# 학습과 검정 예측 비교값 
print('방법1(ols)-학습과 검정 예측 비교값 : ',model_ols.score(X=train_set.iloc[:,[2]], y=train_set.iloc[:,[3]]))
print('방법1(ols)-학습과 검정 예측 비교값 : ',model_ols.score(X=test_set.iloc[:,[2]], y=test_set.iloc[:,[3]]))

plt.scatter(train_set.iloc[:,[2]], train_set.iloc[:,[3]], color='green')
plt.plot(test_set.iloc[:,[2]], model_ols.predict(test_set.iloc[:,[2]]))
plt.show()


#----------------------------------------
# 선형회귀분석방법2 - Ridge 알고리즘을 사용 - 과대/과소적합을 최소화, 다중공선성 방지네 효과적

model_ridge = Ridge().fit(X=train_set.iloc[:,[2]], y=train_set.iloc[:,[3]]) # 대문자로 작성
#print(model_lasso.coef_)
#print(model_lasso.intercept_)
#print('ols predict : \n',model_ridge.predict(test_set.iloc[:,[2]])) # 생성괸 모델 검증
#print('실제값:\n', train_set.iloc[:,[3]])

# 학습과 검정 예측 비교값 
print('방법2(Ridge)-학습과 검정 예측 비교값 : ',model_ridge.score(X=train_set.iloc[:,[2]], y=train_set.iloc[:,[3]]))
print('방법2(Ridge)-학습과 검정 예측 비교값 : ',model_ridge.score(X=test_set.iloc[:,[2]], y=test_set.iloc[:,[3]]))

plt.scatter(train_set.iloc[:,[2]], train_set.iloc[:,[3]], color='blue')
plt.plot(test_set.iloc[:,[2]], model_ridge.predict(test_set.iloc[:,[2]]))
plt.show()


#----------------------------------------
# 선형회귀분석방법3 - Lasso 알고리즘을 사용 - 과대/과소 적합을 최소화, 많은 변수들을 다룰때 효과적 

model_lasso = Lasso().fit(X=train_set.iloc[:,[2]], y=train_set.iloc[:,[3]]) # 대문자로 작성
#print(model_ridge.coef_)
#print(model_ridge.intercept_)
#print('ols predict : \n',model_lasso.predict(test_set.iloc[:,[2]])) # 생성괸 모델 검증
#print('실제값:\n', train_set.iloc[:,[3]])

# 학습과 검정 예측 비교값 
print('방법3(Lasso)-학습과 검정 예측 비교값 : ',model_lasso.score(X=train_set.iloc[:,[2]], y=train_set.iloc[:,[3]]))
print('방법3(Lasso)-학습과 검정 예측 비교값 : ',model_lasso.score(X=test_set.iloc[:,[2]], y=test_set.iloc[:,[3]]))

plt.scatter(train_set.iloc[:,[2]], train_set.iloc[:,[3]], color='red')
plt.plot(test_set.iloc[:,[2]], model_lasso.predict(test_set.iloc[:,[2]]))
plt.show()


