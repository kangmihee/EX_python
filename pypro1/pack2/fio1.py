# try except
from docutils.parsers.rst.directives import encoding
try:
    # 1
    print('파일 읽기')
    #f1 = open(r'C:\work\workspace\pypro1\pack2\ftest.txt', mode = 'r', encoding = 'utf-8')
    # 소문자 r을 앞에 넣어주면 \를 escape으로 구별하지 x
    f1 = open('ftest.txt', 'r', encoding = 'utf-8') # 간단히 요약 가능
    print(f1.read()) 
    f1.close()
        
    # 2
    print('파일 저장')
    f2 = open('ftest2.txt', mode='w', encoding='utf-8')
    f2.write('저장 연습\n')
    f2.write('홍길동, 신기해')
    f2.close()
    print('저장 성공')
        
    # 3
    print('파일 추가')
    f3 = open('ftest2.txt', mode='a', encoding='utf-8') # a는 append
    f3.write('\n추가')
    f3.write('\n내용이 추가됨')
    f3.close()
    print('추가 성공')
        
    # 4
    print('파일 읽기2')
    f4 = open('ftest2.txt', mode='r', encoding='utf-8')
    #print(f4.readlines()) # 밑의 방법으로 표현 가능하다.
    lines = f4.readlines()
    print(lines) # file에 있는 모든 내용 가져옴
    print(lines[2:])
    print(lines[1:4:2])
    
    f4.close()
    

except Exception as e:
    print('err : ' + str(e))
    
    

    