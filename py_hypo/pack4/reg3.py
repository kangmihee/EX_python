# 방법 3 : LInregress - Model O

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

score_iq = pd.read_csv("../testdata/score_iq.csv")
print('data:\n',score_iq.head(3))
print(score_iq.info())

# 상관관계분석
x = score_iq.iq
y = score_iq.score
print('\n상관계수:\n',np.corrcoef(x, y))
print('\n상관관계:\n',score_iq.corr())

# 시각화
# plt.scatter(x, y)
# plt.show()

# 단순 선형회귀
model = stats.linregress(x, y)
print('\nmodel :',model)
print('기울기 :',model.slope)    # 0.6514309527270085
print('절편 :',model.intercept) # -2.8564471221975936
print('상관계수(r)값 :',model.rvalue)  # 0.8822203446134705
print('p값 :',model.pvalue)     # 2.8476895206672287e-50
print('표준오차 :',model.stderr)  #  0.028577934409305384

# 점수예측 y = wx + b
y = 0.6514309527270085 * 135 -2.8564471221975936
print('\ny : ',y)

print('\n','**'*30)
print('제품의 친밀도, 적절성, 만족도 자료사용')
product = pd.read_csv("../testdata/product.csv")
print(product.head(3))
print(product.info())
print('상관계수 : \n',product.corr()) # b:적절성, c:만족도,  둘사이의 양의 상관관계 강함  0.766853

# 적절성에 따른 만족도 예측 모델 작성
model2 = stats.linregress(product['b'], product['c']) # b:적절성(독립변수), c:만족도(종속변수)
print('\nmodel2 :',model2)
print('기울기 :',model2.slope)
print('절편 :',model2.intercept)
print('상관계수(r)값 :',model2.rvalue)
print('p값 :',model2.pvalue)
print('표준오차 :',model2.stderr)

# 샘플데이터로 모델 작성 후 모집단 모델과 비교
idx = np.random.randint(1, len(product), 150) # 150개 random 수 
print('\nrandom idx : \n',idx)

samp_product = product.loc[idx]
print('\nsamp_product : \n',samp_product)

model3 = stats.linregress(samp_product['b'], samp_product['c']) # b:적절성(독립변수), c:만족도(종속변수)
print('\nmodel3 :',model3)

# model2 : LinregressResult(slope=0.7392761785971821, intercept=0.7788583344701907, rvalue=0.7668526996408374, pvalue=2.235344857549229e-52, stderr=0.03822605528717561)
# model3 : LinregressResult(slope=0.6829011913104416, intercept=0.9686989021256709, rvalue=0.7502130000912919, pvalue=2.2262019939159697e-28, stderr=0.049473518238232234)

# 회귀방정식 관련 함수 : 다항식을 작성
from scipy import polyval
# y = wx + b 라는 수식을 만듦
fit_value = polyval([model3.slope, model3.intercept], samp_product['b']) # slope:기울기, intercept:절편, samp_product['b']:x값
print('\n예측값 y : \n',fit_value) # 예측값 y 출력

plt.scatter(samp_product['b'], samp_product['c']) # 실제값
plt.plot(samp_product['b'], fit_value, 'r') # 예측값
plt.legend(['predict', 'real'])
plt.show()

# 새로운 값으로 예측
new_x = pd.DataFrame({'b':[1,1.5,2,6,10]})
fit_value2 = polyval([model3.slope, model3.intercept], new_x) 
print('\n새로운  값의 예측값  y : \n',fit_value2)








