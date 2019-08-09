# 비율 검정 : 집단의 비율이 어떤특정한 값과 같은지를 검색

import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# one sample : 
# a회사에는 100명 중 45명이 스타벅스 커피만 마신다. 
# 국가 통계를 보니 국민 전체의 스타벅스 커피 마시는 비율이 35% 한다면 비율이 같은가 검정하시오.
# 귀무 : 비율이 같다.
# 대립 : 비율이 다르다.

count = np.array([45])
nobs = np.array([100])  # 대상으로 한 수
val = 0.35
z, p = proportions_ztest(count=count, nobs=nobs, value=val)
print('z:',z)
print('p:',p) # p-value(0.044) < 0.05  => 귀무기각 : 비율이 다르다

##################################################################

# two sample : 
# a회사 직원 300명 중 100명이 햄버거를 먹었고,
# b회사 직원 400명 중 170명이 햄버거를 먹었다고 할 때 두 집단의 햄버거를 먹는 비율이 동일한가를 검정하시오.
# 귀무 : 비율이 같다.
# 대립 : 비율이 다르다.

count = np.array([100, 170])
nobs = np.array([300, 400])
z, p = proportions_ztest(count=count, nobs=nobs, value=0) # 비율제시 없을경우에는 0
print('z:',z)
print('p:',p) # p-value(0.013) < 0.05  => 귀무기각 : 비율이 다르다








