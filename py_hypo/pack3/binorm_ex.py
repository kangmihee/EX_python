# 이항분포 개념
# 1. 정규분포(正規分布)와 마찬가지로 모집단이 가지는 이상적인 분포형
# 2. 정규분포가 연속변량인 데 대하여 이항분포는 이산변량
# 3. 그래프는 좌우대칭인 종 모양 곡선
# stats.binom_test() 함수 : 명목척도(y/n) 대상 이항분포검정 

import pandas as pd
import scipy.stats as stats

data = pd.read_csv('../testdata/one_sample.csv')
print(data[:3])

ctab = pd.crosstab(index=data['survey'], columns='count')
ctab.index=['불만족','만족']
print('\n',ctab)

##################################################################

# 양측검정 : 고객안내 서비스에 대해 기존 80% 만족률 가진 검사 실시 - 방향성이 없다.
x = stats.binom_test([136, 14], p=0.8, alternative="two-sided") # alternative : 양측검정
print('\n양측검정-만족률:',x) # p값(0.0006) 출력 < 0.05 보다 작다
# 해설 : 고객안내 서비스에 대해 기존 80% 만족률에 차이가 있다.

# 불만족률
x = stats.binom_test([14, 136], p=0.2, alternative="two-sided") 
print('양측검정-불만족률:',x) # p값(0.0006) 출력 < 0.05 보다 작다 ... # 결과는 같다.

##################################################################

# 단측검정 - 방향성이 있다.
x = stats.binom_test([136, 14], p=0.8, alternative="greater")
print('\n단측검정-만족률:',x) # p값(0.0003) 출력 < 0.05 보다 작다
# 해설 : 고객안내 서비스에 대해 기존 80% 만족률 보다 크다.

x = stats.binom_test([14, 136], p=0.2, alternative="less")
print('단측검정-불만족률:',x) # p값(0.0003) 출력 < 0.05 보다 작다 ... # 결과는 같다.



