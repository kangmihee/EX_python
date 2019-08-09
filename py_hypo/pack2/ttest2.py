from scipy import stats
import pandas as pd
from dask.array.ma import average

# * 서로 독립인 두 집단의 평균 차이 검정 (독립표본 t검정 = independent samples t-test)

############################################################
############################################################

print('문제 1 --------------------------------------') 

# 남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을 독립표본(two sample)이라고 한다.
# 실습) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정

# 귀무 : 남녀 두 집단 간 파이썬 시험의 평균은 차이가 없다.
# 대립 : 남녀 두 집단 간 파이썬 시험의 평균은 차이가 있다.

Male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]

two_sample = stats.ttest_ind(Male, female)
print(two_sample)
# t(검정통계량) = 1.233193127514512
# pvalue = 0.2525076844853278
# p-value = 0.252 >= 0.05 이므로 귀무 채택
# 결론 : 남녀 두 집단 간 파이썬 시험의 평균은 차이가 없다.

print('female : ',average(female))
print('male : ',average(Male))

############################################################
############################################################

print('\n문제 2 --------------------------------------') 

#실습) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_sample.csv'

# 귀무 : 두 가지 교육방법에 따른 평균시험 점수에 차이가 없다.
# 대립 : 두 가지 교육방법에 따른 평균시험 점수에 차이가 있다.

data = pd.read_csv('../testdata/two_sample.csv')
print('data:\n',data.head(3))
result = data[['method', 'score']]
print('\nresult:\n',result)

# NaN 확인
print('\nNaN 확인 :\n',result.isnull().sum())
print('\nNaN 확인 :\n',result['score'].isnull().sum())
print('\nNaN 확인 :\n',result.isnull().any())

m1 = result[result['method'] == 1] 
m2 = result[result['method'] == 2]

score1 = m1['score']
score2 = m2['score']

#sco1 = score1.fillna(0) # 비어있는 값 0으로 채우기
sco1 = score1.fillna(score1.mean()) # 평균값으로 빈값 채우기
sco2 = score2.fillna(score2.mean())

# 정규성 확인
import seaborn as sns
import matplotlib.pyplot as plt

# sns.distplot(sco1, kde =False, fit = stats.norm)
# sns.distplot(sco2, kde =False, fit = stats.norm)
# plt.show()

print('\nsco1: ',stats.shapiro(sco1)) #p(0.367) >= 0.05
print('sco2: ',stats.shapiro(sco2))   #p(0.671) >= 0.05

# stats.kruskal()  # 정규성 없다고 생각할 때 사용...?
# stats.wilcoxon()
# stats.mannwhitneyu()

result = stats.ttest_ind(sco1, sco2) # 등분산성o ... 있다고 가정함
#result = stats.ttest_ind(sco1, sco2, equal_var = True) # equal_var = True : 등분산성o 사용
#result = stats.ttest_ind(sco1, sco2, equal_var = False) # equal_var = False : 등분산성x 사용

print('\n검정통계량 : %.5f, pvalue : %.5f'%result) #p(0.84505) >= 0.05
# t(검정통계량) = -0.19649
# pvalue = 0.84505
# p-value = 0.84505 >= 0.05 이므로 귀무 채택
# 결론 : 두 가지 교육방법에 따른 평균시험 점수에 차이가 없다.

