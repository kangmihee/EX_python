# bs4d으로 XML 자료 처리
from bs4 import BeautifulSoup

with open('../testdata/my.xml', mode='r', encoding='utf-8') as fr:
    xmlFile = fr.read()
    print(xmlFile)
    
soup = BeautifulSoup(xmlFile, 'lxml')
print(soup)


print('-----------------------')
itemTag = soup.find_all('item')
print(itemTag[0])

print()
nameTag = soup.find_all('name')
print(nameTag)
print(nameTag[0]['id'])
print()
for i in nameTag:
    print(i['id'])
    
print()
for i in itemTag:
    nameTag = i.findAll('name')
    for j in nameTag:
        print('id : ' + j['id'] + ' name : ' + j.string)
        
    for j in i.findAll('tel'):
        print('tel : ' + j.string)
        
    for j in i.findAll('exam'):
        print('kor : ' + j['kor'])
        
        
        