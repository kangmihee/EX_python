# 교차분석 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 : NA가 있는 행은 제외한다.
# 
# 교차분석 문제2) jikwon_jik과 jikwon_pay 간의 관련성 분석. 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (사장:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#   조건 : NA가 있는 행은 제외한다.

import pandas as pd
import scipy.stats as stats
import MySQLdb
import numpy as np
import ast

################################################################

# 문제1 : 
# 귀무 : 부모학력 수준이 자녀의 진학여부와 관련이 없다.
# 대립 : 부모학력 수준이 자녀의 진학여부와 관련이 있다.

data = pd.read_csv("../testdata/cleanDescriptive.csv")
data = data.dropna()
print(data.head(5))

ctab = pd.crosstab(index=data['level2'], columns=data['pass2'])
print(ctab)

chi2, p, ddof, expected = stats.chi2_contingency(ctab)
msg = "chi2 : {}, p-value : {} "
print('\n',msg.format(chi2, p))

# p-value : 0.020 < 0.05 이기 때문에 귀무가설 기각, 대립가설 채택
# 결과 : 부모학력 수준이 자녀의 진학여부와 관련이 있다.

################################################################

# 문제2 : 
# 귀무 : jikwon_jik과 jikwon_pay 간의 관련이 없다.
# 대립 : jikwon_jik과 jikwon_pay 간의 관련이 있다.

try:  # db 읽기
    with open("mariadb_connect.txt", "r") as fr:
        config = fr.read() # String 형태    
except Exception as e:
    print('read err : ' + str(e))
config = ast.literal_eval(config)

try:
    conn = MySQLdb.connect(**config) # 연결을 dict type으로  (String type은  err)
    cursor = conn.cursor()
    cursor1 = conn.cursor()
    sql = """
        select jikwon_pay, jikwon_jik from jikwon
    """    
    cursor.execute(sql)
    df = pd.read_sql(sql, conn)    
    df = df.dropna()
    
    df.loc[df.jikwon_jik=='이사', 'jikwon_jik'] = '1'
    df.loc[df.jikwon_jik=='부장', 'jikwon_jik'] = '2'
    df.loc[df.jikwon_jik=='과장', 'jikwon_jik'] = '3'
    df.loc[df.jikwon_jik=='대리', 'jikwon_jik'] = '4'
    df.loc[df.jikwon_jik=='사원', 'jikwon_jik'] = '5'
    
    df.loc[(df.jikwon_pay <= 2999) & (df.jikwon_pay >= 1000), 'jikwon_pay']= 1
    df.loc[(df.jikwon_pay <= 4999) & (df.jikwon_pay >= 3000), 'jikwon_pay'] = 2,
    df.loc[(df.jikwon_pay <= 6999) & (df.jikwon_pay >= 5000), 'jikwon_pay'] = 3,
    df.loc[(df.jikwon_pay >= 7000), 'jikwon_pay'] = 4
    df.columns = ('연봉','직급')
    print(df)
    
    ctab2 = pd.crosstab(index=df['직급'], columns=df['연봉'])   
    print(ctab2.head(5))
       
    chi2, p, ddof, expected = stats.chi2_contingency(ctab2)
    msg = "chi2 : {}, p-value : {} "
    print('\n',msg.format(chi2, p))
    
    # p-value : 0.0001 < 0.05 이기 때문에 귀무가설 기각, 대립가설 채택
    # 결과 : jikwon_jik과 jikwon_pay 간의 관련이 있다.
    
except Exception as e:
    print('err : ', e)
    
finally:
    cursor.close()
    conn.close()    