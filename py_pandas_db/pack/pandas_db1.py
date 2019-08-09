# sqlite3
import sqlite3

sql = "create table if not exists test(product varchar(10), maker varchar(10), weight real, price integer)"
conn = sqlite3.connect(":memory:")
conn.execute(sql)
conn.commit()

data = [('mouse','sm',12.5,5000),('keyboard','lg',52.5,25000)]
stmt = "insert into test values(?,?,?,?)"
conn.executemany(stmt, data)
conn.commit()

#############################################
# select 방법 1
cursor = conn.execute("select * from test")
rows = cursor.fetchall()

print(rows[0], ' ', rows[1])
print(rows[0][0])

import pandas as pd
df1 = pd.DataFrame(rows, columns=['상품명','제조사','무게','가격'])
print('\n columns 추가 : \n',df1)

#############################################
# select 방법 2
df2 = pd.read_sql("select * from test", conn) 
print('\n',df2)

#############################################

cursor.close()
conn.close()

#############################################




























