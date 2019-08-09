# One-sample t-test(단일표본 t검정) : 정규분포의 표본에 대해 기댓값을 조사하는 검정방법이다.

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#################################################

# 연습1) 어느 남성 집단의 평균키 검정
print('연습1 --------------------------------------')


one_sample = [177.0, 182.7, 169.6, 176.8, 180.0]
print('평균키 :', np.array(one_sample).mean())

# 귀무 : 집단의 평균키가 177cm이다.
# 대립 : 집단의 평균키가 177cm이 아니다.
result = stats.ttest_1samp(one_sample, popmean=177) # popmean 예상 평균값을 넣어준다
print('\npopmean=177 :',result) 
# t(검정통계량) = 0.10039070766877535
# pvalue = 0.9248646407498543
# 결론 p-value = 0.924 >= 0.05 이므로 귀무 채택

# 귀무 : 집단의 평균키가 167cm이다.
# 대립 : 집단의 평균키가 167cm이 아니다.
result = stats.ttest_1samp(one_sample, popmean=167) # popmean 예상 평균값을 넣어준다
print('popmean=167 :',result) 
# t(검정통계량) = 4.663604692613722
# pvalue=0.009563805798718098
# 결론 p-value = 0.009 < 0.05 이므로 귀무 기각, 대립 채택

#################################################

# 연습2) 어느 집단의 평균 검정
print('\n연습2 --------------------------------------')


np.random.randn(123)
mu = 0
n = 10

x = stats.norm(mu).rvs(n) # norm:정규분로 , rvs:랜덤 표본 생성
print('x:\n',x)
# sns.distplot(x)
# plt.show()

# 귀무 : 모수의 평균은 0이다.
# 대립 : 모수의 평균은 0이 아니다.
result = stats.ttest_1samp(x, popmean=0)
print('\npopmean=0 :',result)
# t(검정통계량) = 1.186535596408061
# pvalue=0.26578684473969755
# 결론 p-value = 0.265 >= 0.05 이므로 귀무 채택

# 귀무 : 모수의 평균은 0.9이다.
# 대립 : 모수의 평균은 0.9이 아니다.
result = stats.ttest_1samp(x, popmean=0.9)
print('popmean=0.9 :',result)
# t(검정통계량) = -3.536627059919446
# pvalue=0.006347597232969365
# 결론 p-value = 0.006 < 0.05 이므로 귀무 기각, 대립 채택

#################################################

# 실습 예제 1)
print('\n실습 예제 1 --------------------------------------')
# A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리 (국어 점수 평균검정) student.csv


data = pd.read_csv('../testdata/student.csv')
print('data:\n',data.head(3))
print('\ndescribe : \n',data.describe())

# 귀무 : 학생들의 국어점수의 평균은 80이다.
# 대립 : 학생들의 국어점수의 평균은 80이 아니다.
result = stats.ttest_1samp(data.국어, popmean=80)
print('\nt값 : %3f, p-value:%.3f'%result)
# t(검정통계량) = -1.332180
# pvalue = 0.199
# 결론 p-value = 0.199 >= 0.05 이므로 귀무  채택

# 귀무 : 학생들의 국어점수의 평균은 60이다.
# 대립 : 학생들의 국어점수의 평균은 60이 아니다.
result = stats.ttest_1samp(data.국어, popmean=60)
print('t값 : %3f, p-value:%.3f'%result)
# t(검정통계량) = 2.420440
# pvalue = 0.026
# 결론 p-value = 0.026 < 0.05 이므로 귀무 기각, 대립 채택

#################################################

# 실습 예제 2)
print('\n실습 예제 2 --------------------------------------')

# 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.

data = pd.read_csv('../testdata/babyboom.csv')
print('data:\n',data.head(3))
print('\ndescribe : \n',data.describe())

fdata = data[data.gender == 1]
print('\ngender=1(여아)만 출력 : \n',fdata.head(3))
print('\ngender=1(여아)갯수 출력 : \n',len(fdata))

# 정규성 확인
# sns.distplot(fdata.iloc[:, 2], fit=stats.norm) # 모든행의 2번째 행만
# plt.show()

# Q-Q plot : 잔차의 정규성 확인용
# stats.probplot(fdata.iloc[:, 2], plot=plt)
# plt.show()

print('\nshapiro : ',stats.shapiro(fdata.iloc[:, 2])) # 0.05보다 커야 정규성을 띤다.
# pvalue = 0.017984945327043533
# 결론 p-value = 0.0179 < 0.05 이므로 정규성을 띤다고 볼 수 없다.

result = stats.ttest_1samp(fdata.weight, popmean=2800)
#print('popmean=2800 :',result)
print('t값 : %3f, p-value:%.3f'%result)
# t(검정통계량) = 2.233188,
# pvalue = 0.039
# 결론 p-value = 0.039 < 0.05 이므로 귀무 기각
# 귀무 : 여아 신생아의 몸무게는 평균이 2800보다 작다.
# 대립 : 여아 신생아의 몸무게는 평균이 2800보다 작지 않다.(2800보다 크다)

