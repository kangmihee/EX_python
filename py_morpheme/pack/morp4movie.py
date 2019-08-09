# 영화 평점 관련 글 읽어 영화 간 유사도 출력

from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def movie_scrape(url):
    result = []
    for p in range(10):
        r = requests.get(url + "&page=" + str(p))
        soup = BeautifulSoup(r.content, 'lxml', from_encoding='ms949')
        #print(soup)
        title = soup.find_all("td", {"class":"title"})
        #print(title)
        sub_result = []
        for i in range(len(title)):
            sub_result.append(title[i].text
                              .replace("\r","")
                              .replace("\n","")
                              .replace("\t","")                              
                              .replace("ㅋㅋ","")
                              .replace("ㅎㅎ","")
                              .replace(".","")
                              .replace("..","")  
                              .replace(",,","")
                              .replace("알라딘","")       
                              .replace("토이 스토리 4 ","")       
                              .replace("라이온 킹","")       
                              .replace("마이펫의 이중생활2","")       
                              .replace("겨울왕국 2","")       
                                                                                      
                              .replace("신고","")    # 문자 자를 수 있음                                                         
                              )
        
        result = result + sub_result
    return("".join(result))

aladdin = movie_scrape("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=163788&target=after")
king = movie_scrape("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=169637&target=after")
toy = movie_scrape("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=101966&target=after")
mypet = movie_scrape("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=180374&target=before")
frozen = movie_scrape("https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=136873&target=before")
movies = [aladdin, king, toy, mypet, frozen]
movies = [m.replace("입니다", "") for m in movies] # 문자 자를 수 있음
movies = [m.replace("영화", "") for m in movies] 
movies = [m.replace("디즈니", "") for m in movies] 
movies = [m.replace("토이", "") for m in movies] 


#print(movies)


okt = Okt()

def word_seprate(movies):
    result = []
    for movie in movies:
        words = okt.pos(movie)
        one_result = []
        for word in words:
            if word[1] in ['Noun', 'Adjective'] and len(word[0]) >= 2:
                one_result.append(word[0])
        result.append(" ".join(one_result))
    
    return result

word_list = word_seprate(movies)
#print(word_list)


# 텍스트 문서를 토큰 카운트 행렬로 만듦 (CountVectorizer)

count = CountVectorizer(min_df=2)
#print(count)
tf_dtm = count.fit_transform(word_list).toarray()
#print(tf_dtm)

tf_dtm = pd.DataFrame(tf_dtm, columns = count.get_feature_names(), index = ['aladdin', 'king', 'toy', 'mypet', 'frozen'])
print(tf_dtm) # 영화별 단어별 빈도 수 확인


print('---------------------------------')

idf_maker = TfidfVectorizer(min_df=2)
tf_idf = idf_maker.fit_transform(word_list).toarray()
#print(tf_idf)

tf_idf_dtm = pd.DataFrame(tf_idf, columns = count.get_feature_names(), index = ['aladdin', 'king', 'toy', 'mypet', 'frozen'])
print(tf_idf_dtm)  # 가중치



# 각영화관 유사도를 측정하기위해 코사인 유사도 알고리즘 사용
def cosin_simi_fnc(doc1, doc2):
    bunja = sum(doc1*doc2)
    bunmo = (sum((doc1) ** 2) * sum((doc2) ** 2)) ** 0.5
    return bunja / bunmo

res = np.zeros((5, 5))

for i in range(5):
    for j in range(5):
        res[i, j] = cosin_simi_fnc(tf_idf_dtm.iloc[i], tf_idf_dtm.iloc[j].values)

df = pd.DataFrame(res, 
                  columns = ['aladdin', 'king', 'toy', 'mypet', 'frozen'],
                  index = ['aladdin', 'king', 'toy', 'mypet', 'frozen'])
print(df)

















