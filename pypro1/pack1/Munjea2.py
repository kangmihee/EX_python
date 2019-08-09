from abc import *

class Employee(metaclass = ABCMeta) :

    def __init__(self, irum, nai) :
        self.irum = irum
        self.nai = nai
        
    @abstractmethod
    def pay(self) :
        pass
    
    @abstractmethod
    def data_print(self) :
        pass
        
    def irumnai_print(self) :
        print("이름 : ", self.irum, ", 나이 : ", self.nai, end = ", ")

class Temporary(Employee) :
    def __init__(self, irum, nai, ilsu, ildang):
        Employee.__init__(self, irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
    
    def pay(self):
        return self.ilsu * self.ildang
        
    def data_print(self) :
        self.irumnai_print()
        print("월급 : {}".format(self.pay()))
    
class Regular(Employee) :
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)  # == Employee.__init__(self, irum, nai)
        self.salary = salary
        
    def pay(self):
        return self.salary
        
    def data_print(self) :
        self.irumnai_print()
        print("급여 : {}".format(self.pay()))

class Salesman(Regular) :
    def __init__(self, irum, nai, salary, sales, commission):
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.commission = commission
    
    def pay(self):
        return self.salary + (self.sales * self.commission)
        
    def data_print(self) :
        self.irumnai_print()
        print("급여 : {}".format(self.pay()))

t = Temporary("aaa", 22, 20, 1000)
r = Regular("bbb", 35, 1000)
s = Salesman("ccc", 53, 5000, 2000, 0.25)

t.data_print()
r.data_print()
s.data_print()




