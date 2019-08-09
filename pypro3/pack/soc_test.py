# tcp/ip 기반의 Socet 클래스를이용한 통신

import socket

print(socket.getservbyname('http', 'tcp'))   # 80 
print(socket.getservbyname('telnet', 'tcp')) # 23
print(socket.getservbyname('ftp', 'tcp'))    # 21

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
