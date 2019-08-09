# 회귀분석으로 추정치(독립:마력, 종속:연비) 구하기 예제 : ols()사용
import statsmodels.api
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family='malgun gothic')
mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.head())
#print('\n구조:\n',mtcars.describe())
#print('\n상관계수:\n',np.corrcoef(mtcars.hp, mtcars.mpg)) # 마력, 연비 ... 음의 상관관계를 이룸
#print('\n상관관계:\n',mtcars.corr()) # 음의상관관계

# 시각화
# plt.scatter(mtcars.hp, mtcars.mpg)
# plt.xlabel('마력수')
# plt.ylabel('연비')
# slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1)
# plt.plot(mtcars.hp, mtcars.hp * slope + intercept,'b')
# plt.show()

#-----------------------------------
# 단일 회귀분석 모델
print('\n단일 회귀분석 모델 : ')
result = smf.ols(formula='mpg ~ hp', data=mtcars).fit()
#print(result.summary()) # Intercept(절편):30.0989, hp(기울기:slope):-0.0682
print(result.summary().tables[1])
print('임의의 마력수예 대한 연비 예측값 출력 :', -0.0682 * 110 + 30.0989)  # slope(기울기) * hp(아무값) + Intercept(절편)
print('임의의 마력수예 대한 연비 예측값 출력 :', -0.0682 * 210 + 30.0989)  # 15.7
print('임의의 마력수예 대한 연비 예측값 출력 :', -0.0682 * 50 + 30.0989)   # 26.6 (마력과 연비는 반비례관계)마력수가 작아지면  연비가 커짐

#-----------------------------------
# 다중 회귀분석 모델
print('\n다중 회귀분석 모델 : ')
result2 = smf.ols(formula='mpg ~ hp + wt', data=mtcars).fit()
#print(result2.summary()) # Intercept(절편):37.2273, hp(기울기:slope):-0.0318, wt(기울기:slope):-3.8778
print(result2.summary().tables[1])
print('임의의 마력수예 대한 연비 예측값 출력 :', (-0.0318 * 110) + (-3.8778 * 2.620) + 37.2273)
print('임의의 마력수예 대한 연비 예측값 출력 :', (-0.0318 * 210) + (-3.8778 * 5.0) + 37.2273)
print('임의의 마력수예 대한 연비 예측값 출력 :', (-0.0318 * 50) + (-3.8778 * 0.5) + 37.2273)

#-----------------------------------
# 추정치 구하기  wt(차체무게)로 인해 mpg(연비)가 영향을 받으므로 이를 통해 임의의 wt 값에  mpg를 추정하기
result3 = smf.ols(formula='mpg ~ wt', data=mtcars).fit()
print(result3.summary())

print('임의의 차체무게에 대한 연비 출력: ', -5.3445 * 1.5 +  37.2851)
pred = result3.predict()

print(mtcars.mpg[0])
print(pred)
 
data = {
    'mpg_real':mtcars.mpg,
    'mpg_pred':pred
    }
 
df = pd.DataFrame(data)
print('\n',df)

mtcars.wt = 10
pred_new = result3.predict(pd.DataFrame(mtcars.wt))
print('\n',str(mtcars.wt) + '일 때 예상연비는 ', pred_new[0])
print('\n차체무게가 ' + str(mtcars.wt[0]) + '일 때 예상연비는 ', pred_new[0])

wt_new = pd.DataFrame({'wt':[5, 2, 0.5, 8]})
pred_new2 = result3.predict(wt_new)
print('\n예상연비 : \n',pred_new2)
                       























