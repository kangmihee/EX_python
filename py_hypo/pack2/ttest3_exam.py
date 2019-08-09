import scipy.stats as stats
from numpy import average
import MySQLdb
import ast
import pandas as pd

# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
# 귀무 : 영업부 직원의 연봉의 평균에 차이가 존재하지 않는다.
# 대립 : 영업부 직원의 연봉의 평균에 차이가 존재한다.

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
    
    buser1 = df[df['부서'] == '총무부']['연봉']
    buser2 = df[df['부서'] == '영업부']['연봉']
    
    #print('문제3:',stats.ttest_ind(buser1, buser2))
    # t(검정통계량) = 0.4683, pvalue = 0.6455
    # p-value = 0.6455 >= 0.05 이므로 귀무 채택
    # 결론 : 영업부 직원의 연봉의 평균에 차이가 존재하지 않는다.
    
except Exception as e:
    print('err : ', e)
    
finally:
    cursor.close()
    conn.close()   


# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
# 중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
# 기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?
# 귀무 : 중간고사 성적과 기말고사 성적을 비교한 결과 학급의 학업능력이 변화하지 않았다.
# 대립 : 중간고사 성적과 기말고사 성적을 비교한 결과 학급의 학업능력이 변화하였다.

score1 = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
score2 = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

print('문제4:',stats.ttest_rel(score1, score2))
# t(검정통계량) = -2.6281, pvalue = 0.0234
# p-value = 0.0234 < 0.05 이므로 귀무 기각, 대립 채택
# 결론 : 중간고사 성적과 기말고사 성적을 비교한 결과 학급의 학업능력이 변화하였다.

