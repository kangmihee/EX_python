# pandas 문제 5)
# 
#  MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.
#      - 사번 이름 부서명 연봉 직급을 읽어 DataFrame을 작성
#      - 부서명별 연봉의 합, 평균을 출력
#      - 부서명, 직급으로 교차테이블을 작성(crosstab : 명목형 숫자 데이터 칼럼을 추가해서 작업함)
#      - 직원별 담당 고객자료를 출력
#      - DataFrame의 자료를 파일로 저장

import MySQLdb
import pandas as pd
import numpy as np
import ast
import csv

try:  # db 읽는 방법
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
        select jikwon_no, jikwon_name, buser_name, jikwon_pay, jikwon_jik 
        from jikwon inner join buser
        on buser.buser_no = jikwon.buser_num
    """
    sql2 = """
        select gogek_no, gogek_name, gogek_tel, gogek_jumin, jikwon_name
        from gogek inner join jikwon
        on gogek.gogek_damsano = jikwon.jikwon_no order by jikwon_name
    """
        
    cursor.execute(sql)
    cursor1.execute(sql2)
    
    # 사번 이름 부서명 연봉 직급을 읽어 DataFrame을 작성  
    df = pd.read_sql(sql, conn)
    df.columns = ('번호','이름','부서','연봉','직급') # 튜플타입    
    print(df.head(3))
    
    df2 = pd.read_sql(sql2, conn)
    df2.columns = ('고객번호','고객이름','고객핸드폰','고객주민번호', '담당사원이름') # 튜플타입    
    print(df2.head(3))
    
    
    # 부서명별 연봉의 합, 평균을 출력
    buser_pay_sum = df.groupby(['부서'])['연봉'].sum()
    buser_pay_mean = df.groupby(['부서'])['연봉'].mean()
    print('\n 부서명별 연봉의 합 : \n',buser_pay_sum)  
    print('\n 부서명별 연봉의  평균 : \n',buser_pay_mean)  
    
    
    # 부서명, 직급으로 교차테이블을 작성(crosstab : 명목형 숫자 데이터 칼럼을 추가해서 작업함)
    ctab = pd.crosstab(df['부서'], df['직급'], margins=True)
    print('\n 교차테이블 : \n',ctab)
    
    
    # 직원별 담당 고객자료를 출력
    print('\n 직원별 담당 고객자료 : \n',df2)
    
    
    # DataFrame의 자료를 파일로 저장
    with open("jik_gogek_datas.csv", "w", encoding="utf-8") as fw:
        writer = csv.writer(fw)
        for row in cursor:
            writer.writerow(row)
        print('저장 성공')
        
    with open("jik_gogek_datas1.csv", "w", encoding="utf-8") as fw:
        writer = csv.writer(fw)
        for row in cursor1:
            writer.writerow(row)
        print('저장 성공1')
        
    # DataFrame의 자료를 파일저장 (다른방법)   
    df.to_csv("jikwon_data.csv",index=None)
    df2.to_csv("customer_data.csv",index=None)
    
        
except Exception as e:
    print('err : ', e)
    
finally:
    cursor.close()
    conn.close()
     


