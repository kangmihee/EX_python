a = 1

def doFunc():
    print('a') # a

b = 2

doFunc() # a

res = doFunc()
print(res) # None을 return

kbs = doFunc()
print(kbs) # a와 None return
mbc = doFunc()
print(id(mbc))

def isOdd(arg):
    return arg % 2 == 1  # 홀수 리턴

mydict = {x:x*x for x in range(11) if isOdd(x)}
print(mydict)

print('~~' * 10)

# 지역, 전역 L > E > G
a = 10; b = 20; c = 30
print('함수 수행 전 a:{},b{},c{}'.format(a,b,c)) # 수행 전

def foo():
    a = 40 # 지역변수
    b = 50 # 지역변수
    def bar():
        #c = 60 # 지역변수
        global c   # c = 30
        nonlocal b
        print('함수 수행 중 a:{},b{},c{}'.format(a,b,c)) # 지역변수 a,b,c 
        c = 60 # local variable 'c' 에러 ... global 변수 취해준다.
        b = 70 
    bar() # 수행 중
    
foo()
print('함수 수행 후 a:{},b{},c{}'.format(a,b,c)) # 수행 후 ... c = 60 으로 return

print()

def func1(a,*b, **c): # 가변인수에 * 붙일수 있음 ... **은 dict만 출력
    print(a)
    print(b) # 집합형 자료(tuple) ... 처음의 데이터 뺴고 나머지 출력
    print(c) # irum='tom' 출력

func1('aa', 'bb', 'cc', irum='tom')

# 일급함수 : 함수 안 함수, 인자로 함수, 반환값이 람수
def fun1(a, b):
    return a + b

fun2 = fun1
print(fun2(3,4))


# 함수안에 또 다른 함수가 선언되어 반환되는 것을 클로저 함수라고 한다.
def fun3(func):
    def fun4():
        print('내부함수 출력ㅇㅅㅇ')
        fun4()
        return func
    
sbs = fun3(fun2)
#print(sbs(10, 20))
        
def Hap(x,y):
    return x * y
print(Hap(3, 4))

print((lambda x, y: x * y)(3,4))
ytn = lambda x, y: x * y
print(ytn(3,4))

# 장식자 : Meta 기능 
def make2(fn):
    return lambda:"ㅇㅅㅇ" + fn()  # 주소를 return

def make1(fn):
    return lambda:"ㅎㅅㅎ" + fn()

def hello():
    return "ㅊㅅㅊ"

hi = make2(make1(hello))
print(hi())

@make2  # 장식자
@make1
def hello2():
    return "신기해"
print(hello2())









 
        




















