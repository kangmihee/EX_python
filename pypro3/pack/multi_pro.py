# Thread는 파이썬으 ㅣ구조에서 제대로 구현되지 않는다. 그래서 multiprocessing을 이용해 multi tasking을 구현한다.


from multiprocessing import Pool
import time
import os

# 입력값을 process들을 건너건너 분배 후 실행


def func(x):
    print('값', x, '에 대한 작업 pid=', os.getpid())
    time.sleep(1)
    return x * x
    
if __name__ == '__main__':
    p = Pool(4) # 프로세스 참여 수 ... 많으면 안좋을 수 있음
    
    startTime= int(time.time())
    
    """
    for i in range(0, 10):
        print(func(i))
    """
    print(p.map(func, range(0, 10))) # 함수와 인자값을 같이 준다. 작업시간이 짧아진다.
    
    
    endTime = int(time.time()) 
    print('총 작업 시간: ', (endTime - startTime))
    
    
    