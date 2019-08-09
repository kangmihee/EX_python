'''
Created on 2019. 8. 5.

@author: acorn
'''
# ANOVA 검정방법
import numpy as np
import urllib
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
import statsmodels.api as sm
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3.txt"
data = np.genfromtxt(urllib.request.urlopen(url), delimiter=',')
# print(data, type(data))
print(data)
gr1 = data[data[:, 1] == 1, 0]
gr2 = data[data[:, 1] == 2, 0]
gr3 = data[data[:, 1] == 3, 0]
print(gr1)
print(gr2)
print(gr3)
print('gr1의 정규성 확인 :', stats.shapiro(gr1))
print('gr2의 정규성 확인 :', stats.shapiro(gr2))
print('gr3의 정규성 확인 :', stats.shapiro(gr3))

# 각 그룹간 밀집도를 시각화
plt_data = [gr1, gr2, gr3]
print(plt_data)
ax = plt.boxplot(plt_data)
print(ax)
plt.show()

# 세 그룹의 퍼짐정도와 평균값들은 약간의 차이를 보이고 있다.
# 일원분산분석으로 그 차이를 검정하기

# 일원분산분석(ANOVA) 방법1 - 한가지 성격(요인)의 복수집단 평균값 차이 분석
f_statistic, p_val = stats.f_oneway(gr1, gr2, gr3)
print('f_statistic : ', f_statistic)
print('p_val : ', p_val) # p_val :  0.0435 < 0.05이므로 귀무기각.

# 일원분산분석(ANOVA) 방법2 (linear model 이용)
df = pd.DataFrame(data, columns=['value','group'])
print(df[:3]) # 앞에꺼 3
print(df[-3:]) # 뒤에꺼 3

from statsmodels.stats.anova import anova_lm
model = ols('value ~ C(group)', df).fit() # C() : 독립 변수가 범주형 자료임을 명시적으로 선언
print(anova_lm(model, typ=1))
#             df        sum_sq      mean_sq         F    PR(>F)
# C(group)   2.0  15515.766414  7757.883207  3.711336  0.043589
# Residual  19.0  39716.097222  2090.320906       NaN       NaN

print('****' * 20)
# 이원분산분석 : 두 가지 성격(요인2)의 복수 집단 평균값 차이 검정
url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3_2.txt"
data = pd.read_csv(urllib.request.urlopen(url), delimiter=',')
print(data.head(3))

# 귀무 : 관측자와 태아수 그룹에 따라 태아의 머리둘레에 차이가 없다.
# 대립 : 관측자와 태아수 그룹에 따라 태아의 머리둘레에 차이가 있다.

# plt.rc('font', family='malgun gothic')
# data.boxplot(column='머리둘레', by='태아수', grid=False)
# plt.show()
# 시각화를 통해 태아 세 그룹의 머리둘레는 차이가 있어 보인다.
# 이것이 관측자와 상호작용이 있는지 검정 실시

formula = '머리둘레 ~ C(태아수) + C(관측자수) + C(태아수):C(관측자수)'
lm = ols(formula, data).fit()
print(anova_lm(lm))

#                   df      sum_sq     mean_sq            F        PR(>F)
# C(태아수)           2.0  324.008889  162.004444  2113.101449  1.051039e-27
# C(관측자수)          3.0    1.198611    0.399537     5.211353  6.497055e-03
# C(태아수):C(관측자수)   6.0    0.562222    0.093704     1.222222  3.295509e-01
# Residual        24.0    1.840000    0.076667          NaN           NaN

#   태아수 p값  1.051039e-27 < 0.05 이므로  태아머리둘레는 차이가 있다.
# 관측자수  p값  6.497055e-03 < 0.05 이므로  태아머리둘레는 차이가 있다.

# C(태아수):C(관측자수)는 p값 3.295509e-01 >= 0.05 상호작용에서는 태아머리둘레에 차이가 없다.
# 관측자와 태아의 머리둘레에는 관련이 없다. 측정자가 다르더라도 채아의 머리둘레에 영향을 주지 않는다.



















