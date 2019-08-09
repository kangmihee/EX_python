# 자동차의 부품 클래스 중 하나로 핸들
class PohamHandle:
    quantity = 0 # 회전량
    
    def LeftTurn(self, quantity):
        self.quantity = quantity
        return "좌회전"
    
    def RightTurn(self, quantity):
        self.quantity = quantity
        return "우회전"
    
    