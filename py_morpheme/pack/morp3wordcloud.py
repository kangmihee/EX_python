# 웹에서 검색자료 읽은 후 워드 클라우드로 출력
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
from boto.dynamodb import item

#keyword = input('검색어:')
keyword = '장마'
print(keyword)
print(quote(keyword))

# 동아일보 검색 기능 사용
target_url = "http://www.donga.com/news/search?query=" + quote(keyword)
sou_code = urllib.request.urlopen(target_url)

soup = BeautifulSoup(sou_code, 'lxml', from_encoding='utf-8')
#print(soup)


########################

msg = ""
for title in soup.find_all('p', 'tit'):
    title_link = title.select('a')
    #print(title_link)
    article_url = title_link[0]['href']
    #print(article_url)
    
    sou_article = urllib.request.urlopen(article_url)
    soup = BeautifulSoup(sou_article,'lxml', from_encoding='utf-8')
    
    contents = soup.select('div.article_txt')
    for imsi in contents:
        item = str(imsi.find_all(text=True))
        #print(item)
        msg = msg + item
        
print(msg)

from konlpy.tag import Okt
from collections import Counter

okt = Okt()
nouns = okt.nouns(msg)
result = []
for imsi in nouns:
    if len(imsi) > 1:  # 2글자 이상만 참여
        result.append(imsi)
        
print(result)

count = Counter(result)
tag = count.most_common(50) # 상위 50개만 참여
print(tag)

##########################################

import pytagcloud
# (min)maxsize : 글꼴크기, 
taglist = pytagcloud.make_tags(tag, maxsize=100)
print(taglist)

pytagcloud.create_tag_image(taglist, "word.png", size=(1000,600), 
                            fontname="Korean", rectangular=False)


# 이미지 읽기
# import matplotlib.pylab as plt
# import matplotlib.image as mpimg
# #%matplotlib inline
# img = mpimg.imread("word.png")
# plt.imshow(img)
# plt.show()


# 이미지 브라우저로 읽기
import webbrowser
webbrowser.open("word.png")





