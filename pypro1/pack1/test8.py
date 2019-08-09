# 상속 

class Person:
    say = '난 사람이야'
    nai = '20'
    __kbs = 'good' # private형식 (현재 class에서만 유효)
    
    def __init__(self, nai):
        print('person 생성자')
        self.nai = nai
        
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))
        
    def hello(self):
        print('안녕')
        print('hello : ', self.say, ' ', self.__kbs)
    
    @staticmethod
    def sbs(tel):
        print('sbs -static method : ', tel)
    
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자'
    
    def __init__(self):
        print('Employee 생성자')
   
    def printInfo(self):
        print('Employee 메소드')
     
    def EprintInfo(self):
        self.printInfo()
        super().printInfo() 
        print(self.say)
        print(super().say)
        self.hello() 
         
e = Employee() # 생성자 호출
print(e.say, ' ', e.nai, ' ', e.subject)
e.EprintInfo()


print('^^^'*10)


class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai) # 부모의 생성자를 호출
       
    def printInfo(self):
        print('Worker : printInfo')
         
    def WprintInfo(self):
        #printInfo() # 모듈 (global)
        self.printInfo() # 현재class에서 함수 찾음
        super().printInfo() # 처음부터 부모를 찾아감
            
w = Worker('30')

print(w.say, ' ', w.nai) # Worker에 nai가 없어서 부모 class의 nai값을 return
w.printInfo()
w.WprintInfo()


print('~~;;;'*10)

class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        #super().__init__(nai)     # Bound method call
        Worker.__init__(self, nai) # UnBound method call
        
    def WprintInfo(self):
        print('Programmer에서 override 가능')
        #self.__kbs # 변수를 선언한 class가 아니기 때문에 에러
        
pr = Programmer(24)
print(pr.say, ' ', pr.nai)
pr.WprintInfo()
pr.hello() 
pr.sbs('111-1111')     # Person class의 함수 사용  (static)
Person.sbs('222-2222') # Person class의 함수 사용  (static)
        
print('--------------------')
a = 10
print(type(a))            
print(type(pr))             # <class '__main__.Programmer'>
print(Programmer.__bases__) # (<class '__main__.Worker'>,)
print(Worker.__bases__)     # (<class '__main__.Person'>,)
print(Person.__bases__)     # (<class 'object'>,)














