# 회귀분석 문제 1) scipy.stats.linregress() 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청시간과 운동량 대한 데이터는 아래와 같다.
#  - 지상파 시청시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균값을 사용하기로 한다. 이상치는 제거.

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import polyval

data = pd.read_csv('reg3_exam.txt', delimiter=' ')
print(data)
data = data.fillna(data['지상파'].mean())

# 이상치 제거
plt.boxplot(data['운동'])
plt.show()
data= data[data['운동']!=35.0]

x = data.지상파
y = data.운동
z = data.종편
print('\n상관계수:\n',np.corrcoef(x, y))
print('\n상관관계:\n',data.corr())

# 단순 선형회귀
model = stats.linregress(x, y)
model2 = stats.linregress(x, z)

print('\nmodel :',model)
print('기울기 :',model.slope)   
print('절편 :',model.intercept)

print('\nmodel2 :',model2)
print('기울기 :',model2.slope)   
print('절편 :',model2.intercept)

# 지상파 시청시간을 입력 후 모집단 모델과 비교 
input_time = float(input('\ntime : '))

# y = wx + b 방법
result = model.slope * input_time + model.intercept
result2 = model2.slope * input_time + model2.intercept

# polyval 방법 
res = polyval([model.slope, model.intercept], input_time)
res2 = polyval([model2.slope, model2.intercept], input_time)

print(result)
print(result2)
print(res)
print(res2)






