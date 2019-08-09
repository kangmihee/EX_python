# 스레드간 자원 공유

import threading, time

g_count = 0
lock = threading.Lock()

def threadCount(id, count):
    global g_count
    for i in range(count):
        lock.acquire()
        print('id %s ===> count:%s, g_count:%s' %(id, i, g_count))
        g_count = g_count + 1
        lock.release()
        
for i in range(1,6):
    threading.Thread(target=threadCount, args=(i,5)).start()

time.sleep(1)  # 1초 텀 갖기

print('마지막 g_count : ', g_count)
print('종료 3')    
