# server
import socket
import sys


#HOST = '192.168.0.96'
HOST = ''
PORT = 7878

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket(소켓종류, 소켓유형)

try:
    serverSock.bind((HOST, PORT)) # tuple 타입으로 준다.
    print('server start...')
    serverSock.listen(5)  # 동시 최대 5명 접속 가능
    
    while True:
        conn, addr = serverSock.accept() # client의 접속 시 승인
        print('client info : ', addr[0], addr[1])
        print(conn.recv(1024).decode()) # 이진(binary)처리해야 접속가능 ... decode로 암호 해제
        
        # 메세지 송신
        conn.send(('from server : ' + str(addr[1]) + '하이 잘 지내').encode('utf_8'))
        
        
except Exception as e:
    print('socket err : ', e)
    sys.exit()
    
finally:
    serverSock.close()
    conn.close()
    