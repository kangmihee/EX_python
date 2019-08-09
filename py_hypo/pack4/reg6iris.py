# 상관관계에 의해 회귀모델의 성넝이 영향

import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
print(iris.head(3))
print(type(iris))

# 시각화
# sns.pairplot(iris)
# plt.show()
print('\n상관관계 :\n',iris.corr())


#-----------------------------
# 단순회귀분석
#result = smf.ols(formula='sepal_length ~ sepal_width', data=iris).fit()
result = smf.ols(formula='sepal_length ~ petal_length', data=iris).fit()
print('\n',result.summary()) # 기울기:-0.2234  , 절편:6.5262

#print('\nR squared : ', result.rsquared)  # 0.0138
#print('P value : \n', result.pvalues)     # 1.518983e-01 < 0.05

print('\nR squared : ', result.rsquared) # 0.759
print('P value : \n', result.pvalues)    # 1.038667e-47 < 0.05

print('\n예측값:',result.predict()[0])
print('실제값:',iris.sepal_length[0])


#-----------------------------
# 다중회귀분석
result2 = smf.ols(formula='sepal_length ~ petal_length + petal_width', data=iris).fit()
print('\n',result2.summary())

columns_selected = "+".join(iris.columns.difference(['sepal_length','sepal_width','species']))
my_formula = "sepal_length ~ " + columns_selected
result3 = smf.ols(formula=my_formula, data=iris).fit()
print(result3.summary()) # 위 코드와 동일하게 사용 R에서는 데이터를  ~. 로 전체지정 가능하지만  python은 불가능















