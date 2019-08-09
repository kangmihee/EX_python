
msg = "파이썬 만세"
print(msg) # client창 에서는 보이지 않음 (영향없음)

print('Content-Type:text/html;charset=utf-8\n')
print('<html><body>')
print('<b>안녕하세요</b>파이썬 모듈로 작성했네요')
print("<br>")
print("변수 값은 %s"%(msg,)) # msg 사용가능
print('</body></html>')
