
class coinIn:
    coin = 0
    change = 0
    def culc(self):
        self.coin =int(input('동전을 입력하시오: '))
        self.cupCount = int(input('몇잔을 원하세요: '))
        self.change = self.coin - (self.cupCount*200)
        if self.change < 0:
            return 0
        elif self.change == 0:
            return 1
        else:
            return self.change
            
        
        