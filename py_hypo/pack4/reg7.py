# Linear Regression

import statsmodels.api
from sklearn.linear_model import LinearRegression

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars[:3])

# 마력수(mp)가 mpg(연비)에 영행을 주는 영향값 예측
x = mtcars[['hp']].values
y = mtcars[['mpg']].values

print(x[:3])
print(y[:3])

# 시각화
import matplotlib.pyplot as plt
#plt.scatter(x, y)
#plt.show()

fit_model = LinearRegression().fit(x,y)
print(fit_model) # 분산처리시 n_jobs 사용
print('\n기울기:', fit_model.coef_[0][0]) # -0.06822827807156365
print('절편:', fit_model.intercept_[0])  # 30.09886054
# y = mx + b
# y = fit_model.coef_[0][0] * x + fit_model.intercept_[0]
# predict = fit_model.predict(x)
pred = fit_model.predict(x) 
print('\npred:\n', pred[:3])    # 2차원으로 보기
print('\npred:\n', pred[:3, 0]) # 1차원으로 보기

# 샤로운 마력수로 연비추정
#new_hp = [[110]]
new_hp = [[60]]
pred_new = fit_model.predict(new_hp)
print('\n연비추정:\n', pred_new[0][0])




