# 클래스의 포함
from pack1.poham import PohamHandle

class PohamCar:
    turnShow = "정지"
    
    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle()  # 생성자 ... 클래스의 포함
        
    def TurnHandle(self, q):
        if q > 0 :
            self.turnShow = self.handle.RightTurn(q) #포함관계의 함수
        elif q < 0 :
            self.turnShow = self.handle.LeftTurn(q)
        elif q == 0 :
            self.turnShow = "직진"
            
            
if __name__ == "__main__" :
    tom = PohamCar('톰')
    tom.TurnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow + str(tom.handle.quantity))
    
    print('-------------------')
    james = PohamCar('제임스')
    james.TurnHandle(-5)
    print(james.ownerName + '의 회전량은 ' + james.turnShow + str(james.handle.quantity))
    
    

    
    
