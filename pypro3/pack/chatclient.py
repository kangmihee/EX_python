import socket
import threading
import sys


def Handle(socket):
    while True:
        data = socket.recv(1024)
        if not data: continue
        print(data.decode('utf-8'))
        
sys.stdout.flush() # 버퍼를 클리어 함 (버퍼안의 내용을 출력창에 보내고 비워주는 것)

name = input('채팅 아이디 입력 : ')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('192.168.0.111', 5555))
cs.send(name.encode('utf-8'))

th = threading.Thread(target=Handle, args=(cs,))
th.start()

while True:
    msg = input()
    sys.stdout.flush()
    if not msg: continue
    cs.send(msg.encode('utf-8'))
    
cs.close()

    
    
