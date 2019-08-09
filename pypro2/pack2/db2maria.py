# 원격 DB 연동
# java는 autocommit이지만 python은 수동으로 commit을 걸어줘야 한다.
# sql은 변수명으로 values로 값을 주면 해킹위험이 있기 떄문에 secure coding(? 또는 %s)으로 사용해야한다.

import MySQLdb
import code
#conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
#print(conn)
#conn.close

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
    conn = MySQLdb.connect(**config) # config는 dict type이기때문에 ** 붙여준다.
    cursor = conn.cursor()


#--------------------------------------      
    # 자료 추가(insert)
    
    """
    # 추가 방법1
    #sql = "insert into sangdata(code, sang, su, dan) values(10, '신상1', 500, 12000)"
    #cursor.execute(sql) # 실제로 데이터가 들어간것은 아님.서버에 값 안들어감 (겉보기로만 보이기), commit하면 들어감
    
    # 추가 방법2
    sql = "insert into sangdata values(%s, %s, %s, %s)" # s = string (sql문은 무조건 문자열취급)
    #sql_data = ('11','신상2',10,2000) # tuple형태
    sql_data = '11','신상2',10,2000    # tuple형태
    cursor.execute(sql, sql_data)
    
    conn.commit()
    """
    
#--------------------------------------  
    # 자료 수정(update)
    
    """
    sql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"   # pk는 수정불가
    sql_data = ('파이썬', 7, 7700, 11)
    cursor.execute(sql, sql_data)
    
    conn.commit()
    """
    
#--------------------------------------  
    # 자료 삭제(delete)
    
    """
    code = '11'
    # 방법1
    sql = "delete from sangdata where code=" + code  # secure coding에 위배
     cursor.execute(sql)
     
    # 방법2
    code = '11'
    sql = "delete from sangdata where code={0}".format(code)
    cursor.execute(sql)
    
    # 방법3
    code = '10'
    sql = "delete from sangdata where code=%s"
    cursor.execute(sql, (code,)) # ,줘서 tuple로 준다
       
    conn.commit()

    """    
    
#--------------------------------------   
    # 자료 읽기(select)
    sql = "select code, sang, su, dan from sangdata" # 출력 순서 바껴도 괜춘

    # 출력 방법 1
    cursor.execute(sql)
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s' %data)    
    print() 
    
    # 출력 방법 2   
    cursor.execute(sql)
    for r in cursor:
        #print(r)
        print(r[0], r[1], r[2], r[3])    
    print()  
    
    # 출력 방법 3  
    cursor.execute(sql)
    for(a, b, c, d) in cursor:
        print(a, b, c, d)        
    print()    
 #--------------------------------------  
        
except Exception as e:
    print('err : ' +  str(e)) 
    conn.rollback() 

finally:
    cursor.close()
    conn.close()


























































