# 추상
from abc import *

class AbstractClass(metaclass = ABCMeta):   
    @abstractmethod # 장식자
    def abcMethod(self): # 추상메소드
        pass
        
    def normalMethod(self):
        print('추상클래스 내의 일반 메소드')
        
#parent = AbstractClass() # 인터페이스를 사용하면 자바에서도 다중상속 가능

class Child1(AbstractClass):
    name = '난 child1'    
    def abcMethod(self):
        AbstractClass.abcMethod(self)
        print('추상메소드 오버라이딩') 
              
ch1 = Child1()

class Child2(AbstractClass):
    def abcMethod(self):
        AbstractClass.abcMethod(self)
        print('추상메소드 오버라이딩2')
    def normalMethod(self):
        print('추상클래스 내의 일반 메소드를 재정의')
        
ch2 = Child2()

print()
aaa = ch1
aaa.abcMethod()
aaa.normalMethod()

print()
aaa = ch2
aaa.abcMethod()
aaa.normalMethod()









































    

