from pack1.coinIn import coinIn

class machine:
    cupCount = 1
    def __init__(self):
        #self.cupCount = cupCount
        self.coinin = coinIn() # 생성자
        self.cal = self.coinin.culc() # change
    def showData(self):
        if self.cal == 0:
            print('요금부족')
        elif self.cal == 1:
            print('커피 ',self.coinin.cupCount,' 잔과 잔돈 0원')       
        else:
            print('커피 ',self.coinin.cupCount,' 잔과 잔돈 ',self.cal)
            
coffee = machine()
coffee.showData()