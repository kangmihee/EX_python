# 형태소 분석

from konlpy.tag import Okt
from docutils.parsers.rst.directives import encoding
okt = Okt()
#result = okt.pos('고추 등 매운음식을 오랫동안 너무 많이 먹었을 경우 인지능력과 기억력을 저하시킬 위험이 높다는 연구결과가 나왔다.')
#result = okt.morphs('고추 등 매운음식을 오랫동안 너무 많이 먹었을 경우 인지능력과 기억력을 저하시킬 위험이 높다는 연구결과가 나왔다.')
#result = okt.nouns('고추 등 매운음식을 오랫동안 너무 많이 먹었을 경우 인지능력과 기억력을 저하시킬 위험이 높다는 연구결과가 나왔다.')
#print(result)

import urllib
from bs4 import BeautifulSoup
from urllib import parse

para = parse.quote("이순신")
print(para)
url = "https://ko.wikipedia.org/wiki/" + para
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')
print(soup)

wordlist = []

for item in soup.select("#mw-content-text > div > p"):
    if item.string != None:
        #print(item.string)
        ss = item.string
        wordlist += okt.nouns(ss)
        
print('wordlist 출력')
print(wordlist)
print('단어 수 : ' + str(len(wordlist)))

word_dict = {}
for i in wordlist:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
    

print('\n\n word_dict 출력')
print(word_dict)

print('중복 단어 제거')
setdata = set(wordlist)
print(setdata) 
print('발견된 단어 수 (중복x) : ' + str(len(setdata)))    
    
    
    
# csv 파일로 저장
import csv
import pandas as pd

try:
    f = csv.writer(open('ws1.csv', 'w', encoding='utf-8'))
    f.writerow(word_dict)
except Exception as e:
    print('err : ', e)
    
# df1 = pd.read_csv('ws1.csv', encoding='utf-8')
# print(df1)

with open('ws1.csv', 'r', encoding='utf-8')as f:
    print(f.read())
    
print()
from pandas import Series, DataFrame
li_data = Series(wordlist)
#print(li_data)  
print(li_data.value_counts()[:5])  
print()
li_data = Series(word_dict)  
print(li_data.value_counts()[:5])  

print('-----------------')
df = DataFrame(wordlist, columns = ['단어'])
print(df.head())
    

###############################################################


    
    
    
    
    
    
    
    