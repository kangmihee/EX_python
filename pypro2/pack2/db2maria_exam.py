# 부서명 : 총무부
#
# 사번    이름  부서  직급
#   1 홍길동  10  과장


import MySQLdb

config = {
    'host':'127.0.0.1',   # dict type
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config) 
    cursor = conn.cursor()
    
    input = input('부서명:')
    
    # 자료 읽기(select)
    sql = "select jikwon_no, jikwon_name, buser_num, jikwon_jik from jikwon inner join buser on buser.buser_no = jikwon.buser_num where buser.buser_name=%s and jikwon_no=1"   
    #sql = "select jikwon_no, jikwon_name, buser_num, jikwon_jik from buser inner join jikwon on buser.buser_no = jikwon.jikwon_no where buser_name=%s"       
    #"select jikwon_no, jikwon_name, buser_num ,jikwon_jik from jikwon where jikwon_no=1"    
    cursor.execute(sql, (input,))
    for data in cursor.fetchall():
        print('%s %s %s %s' %data)    
    print() 
    
    """
    # 자료 수정(update)   
    sql = "update jikwon set jikwon_jik=%s where jikwon_no=%s"   
    sql_data = ('이사', 1)
    cursor.execute(sql, sql_data)
    
    conn.commit()
    """
      
except Exception as e:
    print('err : ' +  str(e)) 

finally:
    cursor.close()
    conn.close()
    
    
    
    
    
    
    
    