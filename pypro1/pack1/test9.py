# method overriding

class Parent:
    def printData(self):
        pass
    
class Child1(Parent):
    def printData(self): # 부모의 함수 사용 = 메소드 오버라이딩
        print('Child1에서 오버라이드')
    
class Child2(Parent):
    def printData(self): 
        print('Child2에서 재정의')
        print('부모 메소드와 이름은 동일하나 다른 기능을 코딩')
        
    def aaa(self):
        print('Child2 고유메소드')
                
c1 = Child1()
c1.printData()

c2 = Child2()
c2.printData()

print('다형성----------------------')
#par = Parent() # 주석처리해도 가능
par = c1     # 부모객체변수로 자식주소를 줌
par.printData()

print()

par = c2     # 부모객체변수로 자식주소를 줌
par.printData()
par.aaa() # 파이썬은 자바와 달리 메소드 오버라이딩 기능이 미약함

print()
plist = [c1, c2]
for i in plist:
    i.printData()













































































