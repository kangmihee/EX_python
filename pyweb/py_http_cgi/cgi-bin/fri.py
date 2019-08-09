import cgi

form = cgi.FieldStorage() # form에서 넘어온 값 받기
name = form["name"].value  # java에서의 request.getParmeter("name") 와 같은 뜻
phone = form["phone"].value
gen = form["gen"].value

print('Content-Type:text/html;charset=utf-8\n')
print("""
<html><body>
이름은 (), 전화{}, 성별{}
</body></html>
""".format(name, phone, gen))
