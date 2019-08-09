# 모듈 호출하기
import other.mymod1 # 호출방법1
from mymod3 import Gop

print('하하핳하하ㅏ')

print('tot : ', other.mymod1.tot)
other.mymod1.kbs()

print(dir())

if __name__ == '__main__':
        print('여기는 최상위 모듈')    
        
from other import mymod1  # 호출방법2
mymod1.Mbc()

from other.mymod2 import Cha # 호출방법3
print(Cha(3, 4))

from other.mymod2 import * # 호출방법3
print(Hap(3, 4))

print(Gop(3, 4))






