# 웹문서 읽어 파일로 저장

from bs4 import BeautifulSoup
import urllib.request as req
import datetime

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'lxml')

#print(soup)

price = soup.select_one("div.head_info > span.value").string
print(price)

# 파일로 저장
#t = datetime.date.today()
#fname = t.strftime('%Y-%m-%d') + ".txt"

#t = datetime.datetime.now()  # 시분초 얻기
#print(t)
#fname = t.strftime('%Y-%m-%d-%H-%M-%S') + ".txt"
#with open(fname, 'w', encoding='utf-8') as fw:
#    fw.write(price)

