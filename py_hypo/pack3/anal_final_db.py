# 가설검정 정리

import MySQLdb
import pandas as pd
import numpy as np
import ast
import scipy.stats as stats

with open('mariadb_connect.txt','r') as fr:
    config = fr.read()
    
config = ast.literal_eval(config)
conn = MySQLdb.connect(**config)
cursor = conn.cursor()


###################################################################


print("--------교차분석(이원카이제곱) 검정  연습 --------")
df = pd.read_sql("select * from jikwon", conn)
print(df[:3])

print('\n각부서와 직원 평가점수 간의 관련성(독립성) 분석')
# 귀무 : 관련이 없다.
# 대립 : 관련이 있다.

buser = df['buser_num'] # 범주형
rating = df['jikwon_rating'] # 범주형
ctab = pd.crosstab(buser,rating) # 교차표 작성
print('ctab:\n',ctab)

chi, p, df, exp = stats.chi2_contingency(ctab)
print("chi:{}, p:{}, df:{}".format(chi, p, df))
# 해설 : p값(0.290) >= 0.05 => 귀무채택 : 관련이 없다.

###################################################################

print('\n각부서와 직급 간의 관련성(독립성) 분석')
# 귀무 : 관련이 없다.
# 대립 : 관련이 있다.

df = pd.read_sql("select * from jikwon where jikwon_no <= 20", conn)
buser = df['buser_num'] # 범주형
jik = df['jikwon_jik'] # 범주형
ctab = pd.crosstab(buser,jik) # 교차표 작성
print('ctab:\n',ctab)

chi, p, df, exp = stats.chi2_contingency(ctab)
print("chi:{}, p:{}, df:{}".format(chi, p, df))
# 해설 : p값(0.2464) >= 0.05 => 귀무채택 : 관련이 없다.


###################################################################


print("\n\n\n--------차이분석(T검정) 검정  연습 : 독립변수(범주), 종속변수(연속) --------")
print('10, 20번 부서 간 평균 연봉값의 차이 여부 검정')
# 귀무 : 두 부서간 연봉평균에 차이가 없다.
# 대립 : 두 부서간 연봉평균에 차이가 있다.

df_10 = pd.read_sql("select buser_num, jikwon_pay from jikwon where buser_num=10", conn)
df_20 = pd.read_sql("select buser_num, jikwon_pay from jikwon where buser_num=20", conn)

buser10 = df_10['jikwon_pay']
buser20 = df_20['jikwon_pay']

t_result = stats.ttest_ind(buser10, buser20)
print(t_result) # p값(0.6455) >= 0.05 => 귀무채택 : 두 부서간 연봉평균에 차이가 없다.  
print(np.mean(buser10),' ',np.mean(buser20)) # 평균값 : 5414, 4895 차이남(?)


###################################################################


print('\n\n-------------------분산분석(ANOA)-------------------')
from statsmodels.formula.api import ols
import statsmodels.api as sm
import matplotlib.pyplot as plt

print('각 부서의 평균 연봉값의 차이 여부 검정')
# 귀무 : 각 부서의 평균 연봉값의 차이가 없다.
# 대립 : 각 부서의 평균 연봉값의 차이가 있다.

df = pd.read_sql("select *from jikwon", conn)
buser = df['buser_num']
pay = df['jikwon_pay'] # 연속형

gr1 = df[df['buser_num'] == 10]['jikwon_pay']
gr2 = df[df['buser_num'] == 20]['jikwon_pay']
gr3 = df[df['buser_num'] == 30]['jikwon_pay']
gr4 = df[df['buser_num'] == 40]['jikwon_pay']

# 시각화
# plot_data =[gr1,gr2,gr3,gr4]
# plt.boxplot(plot_data)
# plt.show()

# ANOA 방법 1
f_sta, pval = stats.f_oneway(gr1,gr2,gr3,gr4)
print("f_sta:{}, pval:{}".format(f_sta, pval))
# 해설 : p값(0.7407) >= 0.05 => 귀무채택 : 차이가 없다.


# ANOA 방법 2 
reg = ols('pay ~ C(buser)', data=df).fit()
table = sm.stats.anova_lm(reg, type=1)
print('\ntable:\n',table)
# 해설 : p값(0.7407) >= 0.05 => 귀무채택 : 차이가 없다.


# 사후검정  (차이점 여부만 확인하고 어떤 차이인지 모르기때문에 사후검정을 해준다.)
from statsmodels.stats.multicomp import pairwise_tukeyhsd
res = pairwise_tukeyhsd(df.jikwon_pay, df.buser_num)
print('\nres:\n',res)
res.plot_simultaneous()
plt.show()

