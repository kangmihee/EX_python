# singleton : 객체가 계속 만들어지는것이 아닌 한번만 만들어 지는것

class Singleton:
    inst = None   
    def __new__(cls):
        if cls.inst is None :
            cls.inst = object.__new__(cls)
            return cls.inst
        
    def aa(self):
        print('일반 메소드')
        
class Sub(Singleton):
    pass

s1 = Sub()
s2 = Sub()

print(id(s1), ' ', id(s2)) # 주소값 서로 다르게 나옴 

s1.aa()
#s2.aa()


print('**'* 20) # 사용가능한 멤버 고정


class Animal:
    __slots__ = ['name', 'age']
    
    def printData(self):
        print(self.name, self.age)
        
        
m = Animal()
m.name = 'tiger'
m.age = 5
#m.eat = '고기' # slots을 걸었기 때문에 'name', 'age'에만 제한을 걸어둠
print(m.name + ' ' + str(m.age))
m.printData()






















