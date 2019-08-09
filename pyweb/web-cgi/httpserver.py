# CGI 서비스 가능
from http.server import CGIHTTPRequestHandler, HTTPServer

PORT = 8888

class Handler(CGIHTTPRequestHandler):
    cgi_diretories = ['/cgi-bin']
    
serv = HTTPServer(('127.0.0.1', PORT), Handler)

print('웹 서비스 시작...')
serv.serve_forever()  # 서비스 시작
