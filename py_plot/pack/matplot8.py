'''
Created on 2019. 7. 30.

@author: acorn
'''
import pandas as pd

tips = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tips.csv")
print(tips.head())
print()

tips['gender'] = tips['sex'] # sex -> gender로 변경
del tips['sex'] # sex 삭제
print(tips.head(3))
print()

tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips.head(3))
print()

tip_pct_group = tips['tip_pct'].groupby([tips['gender'], tips['smoker']]) # 성별에 따른 흡연자
print(tip_pct_group, '\n')
print('성별에 따른 흡연자의 합계 : \n', tip_pct_group.sum(), '\n')
print('성별에 따른 흡연자의 최댓값 : \n', tip_pct_group.max(), '\n')
print('성별에 따른 흡연자의 최솟값 : \n', tip_pct_group.min())
print()
result = tip_pct_group.describe() # describe() : 요약 통계
print(result)

print()
print(tip_pct_group.agg('sum'))
print(tip_pct_group.agg('mean'))
print(tip_pct_group.agg('var'))

def diff_func(group):
    diff = group.max() - group.min()
    return diff

result2 = tip_pct_group.agg(['var','mean','max',diff_func]) # diff_func 은 사용자 지정 함수이기 때문에 ''없이 사용.
print(result2)

import matplotlib.pyplot as plt

# result2.plot(kind='barh', title='agg func')
result2.plot(kind='barh', title='agg func', stacked=True) # stacked=True : 누적 막대 그래프
plt.show()

print('-----' * 10)
print(tip_pct_group.agg('sum'))
print(tip_pct_group.apply(sum)) # 명령어 표현만 다를 뿐 같은 동작 실행.