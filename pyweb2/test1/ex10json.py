import urllib.request as req
from bs4 import BeautifulSoup
import json

url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTime/1/5/"
plain_text = req.urlopen(url).read().decode()
print(plain_text)


# str -> dict
json_data = json.loads(plain_text)
print(json_data['SeoulLibraryTime']['row'][0]['LBRRY_NAME'])

lib_data = json_data.get("SeoulLibraryTime").get("row")
print(lib_data)


print()
for ele in lib_data:
    name = ele.get('LBRRY_NAME')
    addr = ele.get("ADRES")
    print('도서관명 : ' + name)
    print('주소 : ' + addr, ' \n')
