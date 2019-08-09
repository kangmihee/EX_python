# Thread를 이용한 멀티 채팅

import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('192.168.0.111', 5555))
ss.listen(5) 
print('채팅 서비스 시작..')
users = []

def ChatUser(conn):
    name = conn.recv(1024)
    data = '^ㅅ^' + name.decode('utf_8') + '님 입장 !'
    print(data)
    
    try:
        for p in users:
            p.send(data.encode('utf_8'))
                       
        while True:
            msg = conn.recv(1024)
            data = name.decode('utf_8') + '님 메세지:' + msg.decode('utf_8')
            print('수신 : ', data)
        
            for p in users:
                p.send(data.encode('utf_8'))

    except:
        users.remove(conn)
        data = '~~ ' + name.decode('utf_8') + '님 퇴장 !'
        print(data)

        if users:
            for p in users:
                p.send(data.encode('utf_8'))
        else:
            print('종료')
            
while True:
    conn, addr = ss.accept()
    users.append(conn)
    th = threading.Thread(target=ChatUser, agrs=(conn,))
    th.start()
    
