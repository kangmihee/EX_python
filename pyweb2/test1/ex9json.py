# JSON
import json

dict = {'name':'tom', "age":33, 'score':['90','80','100']}
print('dict:%s'%dict)
print('dict:%s'%type(dict))

print('\n인코딩 -----------------') # dump : dict -> str(JSON모양의 문자열 )
str_val = json.dumps(dict)
#str_val = json.dumps(dict, indent = 4)
print('str_val : %s'%str_val)
print('str_val type : %s'%type(str_val))
print(str_val[0:10])
#print(str_val['name']) # type err ... dict 명령 x


print('\n디코딩 -----------------') # str -> dict
json_val = json.loads(str_val)
print('json_val : %s'%json_val)
print('json_val type : %s'%type(json_val))
#print(json_val[0:10]) # type err ... str 명령 x
print(json_val['name']) # 출력가능
print(json_val['score']) 


print('\n--------------------------\n')
for k in json_val.keys():
    print(k)

print()    
for v in json_val.values():
    print(v)


print()
# get
name_data = json_val.get("name")
print(name_data)
score_data = json_val.get("score")
print(score_data)
print(sorted(json_val.keys())) # 정렬가능

print('\n--------------------------\n')
import pandas as pd
objStr = """
{
    "name":"james",
    "lan":["java","python","js"],
    "exam":[
        {"first":77, "second":88},
        {"first":90, "second":100}  
    ]
}
"""

print(objStr, ' ', type(objStr)) # type : str혀


result = json.loads(objStr)
print(result, ' ', type(result)) 
 
seri = pd.Series(result["lan"])
print(seri)
print()
df = pd.DataFrame(result['exam'])
df.columns = ['중간','기말']
print(df)








