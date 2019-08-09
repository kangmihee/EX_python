# 방법 1
import urllib.request
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
data = urllib.request.urlopen(url)
soup = BeautifulSoup(data, 'lxml')

#print(soup.select('div.tit3'))
#print(soup.select('div[class = tit3]')) # 위와 같은 표현
for tag in soup.select('div[class = tit3]'):
    print(tag.text.strip())



print('~~~~~~~' * 10)


# 방법 2
import requests

data = requests.get(url)
print(data.status_code, ' ', data.encoding)
datas = data.text
#print(datas)

datas = requests.get(url).text
soup = BeautifulSoup(datas, 'lxml')
#m_list = soup.findAll("div", "tit3") # 순서 : 'tag명', '속성'
m_list = soup.findAll("div", {'class':"tit3"})
#print(m_list)
for i in m_list:
    title = i.findAll('a')
    #print(title)

title = 'abcdefg'
print(title[title.find('b'):title.find('f')])   # slicing
print(type(title))



for i in m_list:
    title = i.findAll('a')
    # print(title)
    # print(type(title)) # BeautifulSoup 객체로 str() 사용 가능
    #print(type(str(title)))
    # print(str(title)[1:20])
    print(str(title)[str(title).find('title="') + 7:str(title).find('">')])
    
    
print('순위 -----------------------------')
count = 1
for i in m_list:
    title = i.find('a')
    print(str(count) + '위: ' + title.string)
    count += 1


















   
