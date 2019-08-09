# file i/o : with 사용
try:
    with open('ftest3.txt', mode='w', encoding='utf-8') as f1:
        f1.write('문서 저장\n')
        f1.write('with 사용\n')
        f1.write('close 자동 처리\n') # close 필요 없음  
    print('저장 성공')
    
    
    with open('ftest3.txt', mode='r', encoding='utf-8') as f2:
        print(f2.read())
        
    
except Exception as e :
    print('err : ', e)
    
    
print('\n피클링(복합 객체 처리) - object를 파일로 저장')

import pickle
try:
    dicdata = {'tom':'111-1111', 'james':'222-2222'}
    listdata = ['마우스', '키보드']
    tupdata = (dicdata, listdata)
    
    with open('hello.dat', 'wb') as f3:
        pickle.dump(tupdata, f3)   #   pickle.dump(대상자료, 파일객체)
        pickle.dump(listdata, f3)
    print('객체를 파일로 저장')
    
    print('읽기')
    with open('hello.dat', mode='rb') as f4:
        a, b = pickle.load(f4)
        print(a) # pickle의 처음     dicdata를 가져옴
        print(b) # pickle의 두번 째  listdata를 가져옴
        c = pickle.load(f4)
        print(c)
    
except Exception as e :
    print('err : ', e)
    
















