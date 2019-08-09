# 카이제고 ㅂ검정
import pandas as pd

data = pd.read_csv("../testdata/pass_cross.csv", encoding='euc-kr')
print(data.head(5), '\n')

# 귀무 : 공부하는 것과 합격 여부는 관련이 없다.
# 대립 : 공부하는 것과 합격 여부는 관련이 있다.

print('공부함 &합격 :', data[(data['공부함'] == 1) & (data['합격'] == 1)].shape[0])
print('공부함 &불합격 :', data[(data['공부함'] == 1) & (data['불합격'] == 1)].shape[0])

print('\n빈도표----------------\n')
data2 = pd.crosstab(index=data['공부안함'], columns=data['불합격'], margins=True)
data2.columns = ['합격','불합격','행의합']
data2.index = ['공부 o','공부 x','열의합']

print('공부안함 &불합격 :\n',data2)

##################################################

# 기대도수 = (각행의 주변값) * (각열의 주변값) / 총합
#chi2 = (18 - 15) ** 2 + ... 
chi2 = 3
df = 2 - 1

# 방법1 : 유의수준(0.05), df(1)을 이용해 카이제곱표의 입계값(3.84)
# 결론 : 카이제곱 검정 통계량 3 < 3.84 이므로 귀무가설을 채택
# 공부하는것과 합격 여부는 관련이 없다. 결론을 얻는다.


# 방법2 : p값을 이용
import scipy.stats as stats

chi2, p, ddof, expected = stats.chi2_contingency(data2)
print('\n카이제곱값:',chi2)
print('p값:',p)
# 결론 : p값(유의확률:0.5578) > 유의수준(0.05)이므로 귀무가설을 채택


