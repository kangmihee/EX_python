# 상속 - 다형성 구사

class Animal:
    nai = 0
    
    def __init__(self):
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 생물')
        
class Dog(Animal):
    pass

dog1 = Dog()
dog1.move()

print()

class Horse(Animal):
    def my(self):
        print('난 말이야')

horse = Horse()
horse.move()
horse.my()


























