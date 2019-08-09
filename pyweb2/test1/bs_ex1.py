# BeautifulSoup : html, xml 문서를 파싱

from bs4 import BeautifulSoup


######################################


html_data = """
<html><body>
<h1>제목 태그</h1>
<p>웹 페이지 읽기</p>
<p>자료 추출</p>
</body></html>
"""
print(type(html_data))
soup = BeautifulSoup(html_data, 'html.parser') # 파싱방법 1 ... BeautifulSoup으료 파싱해주면 객체 변함
print(type(soup))

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling # 다음단계 데이터 가져오는 법 (아주좋은 방법은 아님)
print('h1 : ',h1)
print('p1 : ',p1) # 첫번쨰 p태그만 가져온다
print('p2 : ',p2)


######################################


print('\nfind() 사용')
html_data2 = """
<html><body>
<h1 id='title'>제목 태그</h1>
<p>웹 페이지 읽기</p>
<p id='my'>자료 추출</p>  # id 혹은 class를 줌  ... id좀 더  unique함
</body></html>
"""
soup2 = BeautifulSoup(html_data2, 'lxml') # 파싱방법 2
print("#title : " + soup2.find(id = "title").string)
print("#my : " + soup2.find(id = "my").string)
print("p : " + soup2.find("p").string) # 맨처름 p 태그 가져옴


######################################


print('\nfind() 사용 ----------------------')
html_data3 = """
<html><body>
<h1 id='title'>제목 태그</h1>
<p>웹 페이지 읽기</p>
<p id='my'>자료 추출</p>  # id 혹은 class를 줌  ... id좀 더  unique함
<div>
    <a href='http://www.naver.com'>naver</a>
    <a href='http://www.daum.net'>daum</a>
    
</div>
</body></html>
"""

soup3 = BeautifulSoup(html_data3, 'lxml') # 파싱
#print(soup3.prettify())
links = soup3.find_all("a") # 해당 태그의 모든 값 가져옴
print(links)

for i in links:
    href = i.attrs['href']
    text = i.string
    print(href ,' ', text)
    
print(soup3.find_all('p')) # 해당 태그의 모든 값 가져옴
print(soup3.find_all(['h1', 'p']))

aa = soup3.find_all(string=['제목 태그', '웹 페이지 읽기'])
print(aa[0])
print(aa[1])


######################################


print('\n 정규표현식')

import re

links2 = soup3.find_all(href = re.compile(r'^http://')) # 시작:^, 끝:$
print(links2)

for i in links2:
    print(i.attrs['href'])


######################################


print('\n CSS selector() 사용 ----------------------')
html_data4 = """
<html><body>
<div id='hello'>
    <a href='http://www.naver.com'>naver</a>
    <ul class='world'>
        <li>안녕</li>
        <li>비가 오네</li>        
    </ul> # 순서가 없는 태그
</div>
</body></html>
"""

soup4 = BeautifulSoup(html_data4, 'lxml') # 파싱
aa = soup4.select_one("div#hello > a ").string # div 태그의 'hello' id 갖는 a태그 
print(aa)

bb = soup4.select("div#hello > ul.world > li") # id:# , class:. 을 사용한다
print(bb)

for i in bb:
    print(i.string)


