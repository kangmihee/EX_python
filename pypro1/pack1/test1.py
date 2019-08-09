a = [1,2,3]
print(type(a))
print(id(a[0]),' ', id(a[1]))
a.append('kbs') # 추가
a += 'mbc'   # 한 글자씩 추가
a += ['sbs'] # 한 단어로 추가
print(a)
print(a[0:3])
a.remove(2) # 삭제
del a[5]    # 삭제
print(a) 
b = tuple(a)
print(b, '', type(b))
#b.remove(1) # 튜플은 remove사용 x, 튜플은 read only 이기 때문(검색이 빠른이유)
# 수정삭제는 list가 빠르다
a = list(b)
a += 'mbc'
print(a)
c = set(a)
a = list(c)
print(c)  # list아니기 때문에 중복되지 않음(lsit는 중복이 가능)

print('**' * 10)
mydic = dict(k1=1, k2='abc')
print(mydic, ' ', type(mydic)) # dict는 순서가 없음
dic = {'파이썬':'뱀', '자바':12, '오라클':'12'} # dic형태는 json형태와 같다
print(dic) # 숫자는 '' 유무 상관없음


# 제어문 (if)
grade = ''
# jum = int(input('점수는'))
jum = 77
print(type(jum))
if 90 <= jum <= 100:
    grade = 'a'
elif 70 <= jum < 90:
    grade = 'b'
else:
    grade = 'c'
    
print('grade : ' + grade)

print()

a = 'kbs'
b = 9 if a == 'kbs' else 11   # 한 줄로 길게 쓰기(파이썬만 가능함)
print(b)

a = 11
b = 'mbc' if a == 9 else 'kbs'
print(b)
    
a = 3
re = a * 2 if a > 5 else a + 2
print(re)
print(bool(True), bool(1), bool(-10), bool(3.5))
print(bool(False), bool(None), bool(0)) # 파이썬에서는 0은 False이다.  나머지 숫자는 True

print()

a = 0
while a <= 10:  # 0일경우 바로 else로 ... 0이 아니면 True
    a += 1
    if a == 5: continue
    if a == 7: break
    print(a, end = ' ')
else: 
    print('정상 종료') # 파이썬은 반복문에 else 를 줄 수 있다. (나머지언어는 반복문에 else 사용x)

print()


#for i in [1,2,3,4,5]:
#for i in (1,2,3,4,5):
for i in {1,2,3,4,5,5,1,3}:  # 중복제거로 5,1,3은 나오지 x   
    print(i, end = ' ')
else:
    print('정상 종료2')

soft = {'java':' 웹용언어', 'python':'만능언어', 'orecle':'db'}
for i in soft.items():
    #print(i) # print라서 자동 한 줄 띄움
    print(i[0] + ' ' + i[1])
    
    
print()


for k,v in soft.items():
    print(k, ' ', v)
    #print(v)

for v in soft.values():
    print(v)

    
print()


li = ['a', 'b', 'c']
for k, d in enumerate(li): # enumerate은 집합형 자료형태를 보여준다.
    print(k, d)

print()
    

datas = [1,2,'a',True,3]
li = [i * i for i in datas if type(i) == int] # return값은 list[]이다.
print(li)

datas = {1,2,2,3,3}
se = {i *i for i in datas}
print(se)

id_names = {1:'tom', 2:'james'}
name_id = {val:key for key, val in id_names.items()} # key와 value값을 바꿔 나타냄
print(name_id)

print()

print(list(range(1,6)))  # []형태   # 1 ~ 5까지 나타냄 (6은 안나옴)
print(tuple(range(1,6))) # ()형태
print(set(range(1,6)))   # {}형태   # return type 지정해준다 (list, tuple, range 등)

#for i in range(10):
#for i in range(1,11):
for i in range(1,11,2): # 2일경우 홀수만 출력 (1일 경우 전부 다)
    print(i, end = ' ')
    

# 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
for i in range(6):
    n1 = i + 1
    for j in range(6):
        n2 = j + 1
        su = n1 + n2
        if su % 4 == 0:
            print(n1, ' ', n2)
    

for _ in range(5): # _언더바 사용 가능(변수값 지정가능)
    print('good')



















