import urllib.request as req
from bs4 import BeautifulSoup

url = "http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTime/1/5/"
plain_text = req.urlopen(url).read().decode()
#print(plain_text)

xmlObj = BeautifulSoup(plain_text,'html.parser')
lib_data = xmlObj.select('row')
#print(lib_data)

for t in lib_data:
    name = t.find('lbrry_name').text
    addr = t.find('adres').text
    
    print('도서관명 : ' + name)
    print('주소 : ' + addr, ' \n')
    