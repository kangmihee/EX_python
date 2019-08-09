a = 1

def func():
    pass

aa = 100

def abc():
    print('이건 함수')

class TestClass:
    aa = 10 # 멤버변수(클래스내에서 전역)
    
    def __init__(self):
        print('생성자')
        
    def __del__(self):
        print('소멸자')
        
    def abc(self):
        print('메소드')
    
    def printMsg(self):
        print('메소드')
        aa = 50
        name = '한국인' # 지역변수
        print(name)
        print(self.aa)  
        print(aa)
        self.abc() # class내의 함수호출이라서 위의 '이건 함수'를 출력할 수 없다.
        
print(TestClass.aa)
# print(TestClass.printMsg()) # 에러뜸 ... 사용불가
print()

test = TestClass() # 생성자 호출 
print(test.aa) # 10 출력

test.printMsg() # 메소드, 한국인, 10, 출력 ... Bound method call
print()
#TestClass.printMsg(test) # 메소드, 한국인, 10, 출력 ... 소멸자는 자동 출력 ... UnBound method call

print('************')
test2 = TestClass() # 생성자 호출 
test2.aa = 77
print(test2.aa) 

test2.printMsg() 





















































