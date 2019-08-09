# 간단한 서버 구축
# favicon : 200이 제일 이상적임

from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 7777

handler = SimpleHTTPRequestHandler
serv = HTTPServer(('127.0.0.1', PORT), handler)
print('웹 서비스 시작...')
serv.serve_forever()  # 서비스 시작

