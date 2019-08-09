# 개인용 DB : sqlite

import sqlite3

#conn = sqlite3.connect("exam.db") # 파일저장
conn = sqlite3.connect(":memory:") # 휘발성

try:
    c = conn.cursor()
    c.execute("create table if not exists friends(name text, phone text, addr text)")
    c.execute("insert into friends(name, phone, addr) values('홍길동', '111-1111', '다동')")
    c.execute("insert into friends values('고길동', '222-1111', '필동')")
    c.execute("insert into friends values(?,?,?)", ('나길동', '333-3333', '역삼동'))
    inputdata = ('신길동', '444-3333', '서초동')
    c.execute("insert into friends values(?,?,?)", inputdata)
    conn.commit()
    
    # select
    c.execute("select * from friends")
    #print(c.fetchone()) # 두  개 이상 참조방법은 없다. 포인터를 하나씩 옮기면서 읽어나가야 함
    #print(c.fetchone())
    print(c.fetchall()) # 각각의 데이터를 튜플로 읽어들임
    
    print()
    
    c.execute("select name, phone, addr from friends") 
    for row in c :
        #print(row)
        print(row[0] + ' ' + row[1] + ' ' + row[2])
        
except Exception as e:
    conn.rollback()
    print('er :', e)
    
finally:
    conn.close()






































