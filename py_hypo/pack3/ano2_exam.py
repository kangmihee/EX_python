# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
import MySQLdb
import ast
import statsmodels.api as sm

data = pd.read_csv('ano_Exam1.txt', delimiter=' ')
print(data)

data = data.fillna(data['quantity'].mean())
print(data)

# 일원분산분석(ANOVA) 방법2 (linear model 이용)
df = pd.DataFrame(data, columns=['kind','quantity'])

from statsmodels.stats.anova import anova_lm
model = ols('quantity ~ C(kind)', df).fit() 
print(anova_lm(model, typ=1))

# 귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하지 않는다.
# 대립 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재한다.

# kind(종류) p값  0.848244 >= 0.05 이므로 귀무채택
# 결론 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하지 않는다.


###################################################################
###################################################################


# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
# 만약 연봉이 없는 직원은 작업에서 제외한다.

try:  
    with open("mariadb_connect.txt", "r") as fr:
        config = fr.read() # String 형태    
except Exception as e:
    print('read err : ' + str(e))
config = ast.literal_eval(config)

try:
    conn = MySQLdb.connect(**config) # 연결을 dict type으로  (String type은  err)
    cursor = conn.cursor()
    sql = """
        select buser_name, jikwon_pay from jikwon inner join buser
        on buser.buser_no = jikwon.buser_num
    """    
    cursor.execute(sql)
    df = pd.read_sql(sql, conn)    

    df.columns = ('부서','연봉')
    
    print(df)
    
    reg2 = ols('df.연봉 ~ C(df.부서)', df).fit()
    table = sm.stats.anova_lm(reg2, typ = 1)
    print(table)

    # 귀무 : 각 부서에 따라 직원의 연봉에 차이가 없다.
    # 대립 : 각 부서에 따라 직원의 연봉에 차이가 있다.
    
    # kind(종류) p값  0.740797 >= 0.05 이므로 귀무채택
    # 결론 : 각 부서에 따라 직원의 연봉에 차이가 없다
  
except Exception as e:
    print('err : ', e)
    
finally:
    cursor.close()
    conn.close()   

