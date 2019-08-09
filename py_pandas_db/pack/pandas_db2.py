# remote DB 연동

import MySQLdb
import pandas as pd
import numpy as np
import ast
import csv

"""
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
} 
"""
try:  # db 읽는 방법
    with open("mariadb_connect.txt", "r") as fr:
        config = fr.read() # String 형태
    
except Exception as e:
    print('read err : ' + str(e))

print(config)
config = ast.literal_eval(config)
print(type(config))  # dict type으로 들어옴


#############################################
# sql 명령
try:
    conn = MySQLdb.connect(**config) # 연결을 dict type으로  (String type은  err)
    cursor = conn.cursor()
    sql = """
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay
        from jikwon inner join buser
        on buser.buser_no = jikwon.buser_num
    """    
    cursor.execute(sql)
    
#     for (a,b,c,d,e,f) in cursor:
#         print(a,b,c,d,e,f)

    with open("jikwon_datas.csv", "w", encoding="utf-8") as fw:
        writer = csv.writer(fw)
        for row in cursor:
            writer.writerow(row)
        print('저장 성공')
        
        
    # 읽기 1 : csv
    df = pd.read_csv("jikwon_datas.csv", header=None, names=('번호','이름','부서','직급','성별','연봉'))
    print(df[:3])
    
    # 읽기 2 : sql
    df2 = pd.read_sql(sql, conn)
    #df2.columns = '번호','이름','부서','직급','성별','연봉' # 튜플타입
    df2.columns = ('번호','이름','부서','직급','성별','연봉') # 튜플타입    
    print(df2.head(3))
    
    print(len(df2))
    print('\n *직급  : \n',df2['직급'].value_counts())
    print('\n *부서  : \n',df2['부서'].value_counts())
    
    print('\n *연봉 합계  : \n',df2.loc[:,'연봉'].sum() / len(df2))
    print('\n *연봉 평균  : \n',df2.loc[:,'연봉'].mean())
    print('\n *연봉 상세  : \n',df2.loc[:,['연봉']].describe())
    print('\n *연봉  5000 이상  : \n',df2.loc[df2.loc[:,'연봉']>=5000])
    print('\n *연봉  5000 이상 , 부서는  영업부: \n',df2.loc[(df2.loc[:,'연봉']>=5000) & (df2['부서']=='영업부')])
    
    print('\n 교차표----------- \n')
    ctab = pd.crosstab(df2['성별'], df2['직급'], margins=True)
    print('\n 교차표 : \n',ctab)
    
    import matplotlib.pyplot as plt
    plt.rc('font', family='malgun gothic')
    
    # 직급별 연봉 평균
    jik_ypay = df2.groupby(['직급'])['연봉'].mean()
    print('\n 직급별 연봉 평균 : \n',jik_ypay)  
    print('\n 직급별 연봉 평균 : \n',jik_ypay.index)  
    print('\n 직급별 연봉 평균 : \n',jik_ypay.values)  
    
    plt.pie(jik_ypay, 
            labels=jik_ypay.index, 
            labeldistance=0.5,
            counterclock=False, # 시계반대방향
            shadow=True,
            explode=(0.2,0,0,0.2,0))
    plt.show()
    

#############################################

except Exception as e:
    print('err : ', e)
    
finally:
    cursor.close()
    conn.close()
     
#############################################