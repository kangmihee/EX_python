# process : 실행중인 하나의 단위 프로그램 / thread : process 내의 단위 프로그램
from subprocess import *

#call('c:/windows/system32/notepad.exe')  # 메모장   ... call은 창을 닫으면 그 다음 창을 오픈해준다.
#Popen('c:/windows/system32/calc.exe')    # 계산기


import threading, time

def run(id):
    for i in range(1, 11):
        print('id:{} ---> {}'.format(id, i))
        
        
# thread를 사용하지 않았을 때        
#run(1)
#run(2)


# thread 사용 (결과는 random값으로 나온다.) 
th1 = threading.Thread(target=run, args=('일',))
th2 = threading.Thread(target=run, args=('둘',))
th1.start()
th2.start()

print('종료')

print('------------')

class MyThread(threading.Thread):
    def run(self):
        for i in range(1,11):
            print('id:{} ---> {}'.format(self.getName(), i))
            time.sleep(0.1)
           
for i in range(2):
    th = MyThread()
    th.start()           

print('종료2')

print('~~~~~~~~~~')













