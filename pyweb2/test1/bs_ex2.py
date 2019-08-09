# 위키백과 사이트 자료 읽기

import urllib.request as req
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki = req.urlopen(url)
print(wiki)
soup = BeautifulSoup(wiki, 'html.parser')
print(soup)
print(soup.select("#mx-content-text > div > p "))