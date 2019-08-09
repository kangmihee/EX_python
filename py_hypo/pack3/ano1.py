'''
Created on 2019. 8. 5.

@author: acorn
'''
# 세 개 이상의 모집단에 대한 가설검정 – 분산분석
# ‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고 요인
# 에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.
# 세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제1종 오류가 증가하게 되어 문제가 발생한다.
# 이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.

# * 서로 독립인 세 집단의 평균 차이 검정
# 실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시. three_sample.csv'
# 귀무 : 교육방법(세가지 방법)에 따른 시험점수(평균)에 차이가 없다.
# 대립 : 교육방법(세가지 방법)에 따른 시험점수(평균)에 차이가 있다.

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols

data = pd.read_csv('../testdata/three_sample.csv')
# data = pd.read_csv('../testdata/three_sample.csv', na_values = ' ')
# data = data.dropna()

print(data.head(3))
print(len(data))
print(data.describe())

# 시각화
import matplotlib.pyplot as plt
plt.hist(data.score)
# plt.show()

data = data.query('score <= 100')
print(len(data))
print(data.describe())

print('정규성 검사 확인 : \n', stats.shapiro(data.score)) # (0.9810646176338196, 0.2986918091773987)
# 0.2986 >= 0.05 이므로 정규성을 띈다.

print()
# 교차표 : 교육방법별 건수
data2 = pd.crosstab(index = data['method'], columns='count')
data2.index = ['방법1','방법2','방법3']
print('교육방법별 건수 : \n', data2)

# 교차표 : 교육방법별 만족여부 건수
data3 = pd.crosstab(data['method'], data.survey)
data3.index = ['방법1','방법2','방법3']
data3.columns = ['만족','불만족']
print('교육방법별 만족여부 건수 : \n', data3)

print('====' * 20)
import statsmodels.api as sm
# F검정통계량을 얻기
# reg = ols('data["score"] ~ data["method"]', data).fit() # R에서의 formula와 같다.
reg = ols('data["score"] ~ C(data["method"])', data).fit()
print(reg)
table = sm.stats.anova_lm(reg, typ=1)
print(table) # PR(>F) 0.727597 >= 0.05
# 교육방법(세가지 방법)에 따른 시험점수(평균)에 차이가 없다.를 인정
#                  df(자유도) sum_sq(SSR) mean_sq(MSR)    F    PR(>F)
# data["method"]   1.0     27.980888   27.980888  0.122228  0.727597 # 
# Residual        76.0 17398.134497(SSE) 228.922822(MSE) NaN    NaN # 잔차(오차)값

# ols('data["score"] ~ C(data["method"])', data).fit() # ****C(data["method"])를 사용하는 것이 좋다.
                                                    # ols에게 독립변수가 범주형 데이터라는 것을 명시적으로 알려주기 위해
                                                    # C() : 안에 데이터가 범주형 데이터라고
#                      df        sum_sq     mean_sq         F    PR(>F)
# C(data["method"])   2.0     28.907967   14.453984  0.062312  0.939639
# Residual           75.0  17397.207418  231.962766       NaN       NaN

# 참고 : 다중회귀식을 사용
#===============================================================================
# reg2 = ols('data.score ~ C(data.method) + C(data.survey)', data).fit()
# print(reg2)
# print(reg2.pvalues)
# table2 = sm.stats.anova_lm(reg2, typ=1)
# print(table2)
#===============================================================================

print()
# 사후검정 : 전체 그룹들 간의 평균값 차이 확인
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# tukeyhsd, scheffe, duncan ... 등의 방법들이 있다.
result = pairwise_tukeyhsd(data.score, data.method)
print(result)

result.plot_simultaneous()
plt.show()