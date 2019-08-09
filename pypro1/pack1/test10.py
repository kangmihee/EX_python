# 다중 상속
class Animal:
    def move(self):
        pass

class Dog(Animal):
    name = "개"
    def move(self):
        print('개는 낮에 돌아다님')

class Cat(Animal):
    name = "고양이"
    def move(self):
        print('고양이는 사뿐히 걸어다님')
        print('눈빛이 빛남')

dog = Dog()
print(dog.name)
dog.move()

print()

cat = Cat()
print(cat.name)
cat.move()

print('--------------------')

class Wolf(Dog, Cat):  # 다중상속
    pass

wolf = Wolf()
print(wolf.name) # 먼저상속한 Dog이 출력
wolf.move()      # 먼저상속한 Dog이 출력


class Fox(Cat, Dog):  # 다중상속
    def foxMethod(self):
        print('여우 고유 메소드')

fox = Fox()
print(fox.name)
fox.move()
fox.foxMethod()













































































