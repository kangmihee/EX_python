# sangdata table을 출력 (서버로)

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

print('Content-Type:text/html;charset=utf-8\n')
print('<html><body><b>상품 자료</b><br>')
print('<table border="1"><tr><th>코드</th><th>품명</th><th>수량</th><th>단가</th></tr>')

try:
    conn = MySQLdb.connect(**config) # config는 dict type이기때문에 ** 붙여준다.
    cursor = conn.cursor()
    
    cursor.execute("select * from sangdata order by code desc")
    datas = cursor.fetchall()
    for d in datas:
        print("""
        <tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
        </tr>    
        """.format(d[0],d[1],d[2],d[3]))
        
except Exception as e:
    print('err : ' +  str(e)) 

finally:
    cursor.close()
    conn.close()
print('</table></body></html>')





