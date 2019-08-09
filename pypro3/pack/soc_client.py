# client source
from socket import *

clientSoc = socket(AF_INET, SOCK_STREAM)
clientSoc.connect(('192.168.0.96', 7878))
clientSoc.sendall('안녕 반가워(mh)'.encode('utf_8'))

re_msg = clientSoc.recv(1024).decode()

print('수신자료 : ' + re_msg)
clientSoc.close()