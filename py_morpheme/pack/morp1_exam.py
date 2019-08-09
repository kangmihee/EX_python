
from konlpy.tag import Okt
from docutils.parsers.rst.directives import encoding
import operator
okt = Okt()

import urllib
from bs4 import BeautifulSoup
from urllib import parse
import pandas as pd


url = "http://www.seelotus.com/gojeon/gojeon/so-seol/hong-kil-dong-wan-pan-bon.htm" 
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')

wordlist = [] 
 
#location > province + city + data > tmn
 
for item in soup.select('p'):
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

sorted_x = sorted(word_dict.items(),
    key = operator.itemgetter(1), reverse=True)
     
 
#print('\n\n word_dict 출력')
#print(word_dict)
 
#print('중복 단어 제거')
#setdata = set(wordlist)
#print(setdata) 
#print('발견된 단어 수 (중복x) : ' + str(len(setdata)))    
     
     
###################################################
     
# csv 파일로 저장
import csv
import pandas as pd
 
try:
    f = csv.writer(open('ws2.csv', 'w', encoding='utf-8'))
    f.writerow(word_dict)
except Exception as e:
    print('err : ', e)
     
     
with open('ws2.csv', 'r', encoding='utf-8')as f:
    print(f.read())
     
print()
from pandas import Series, DataFrame
li_data = Series(wordlist)
#print(li_data)  
print(li_data.value_counts()[:5])  
print()
 
print('-----------------')
df = DataFrame(wordlist, columns = ['단어'])
print(df.head())
     
 
 
 
     
     
    
    
    
    
    
    