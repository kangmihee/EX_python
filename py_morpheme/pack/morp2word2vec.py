# 형태소 분석 후 다어 간 거리 계산
import pandas as pd
from konlpy.tag import Okt

okt = Okt()

f = open('aaa.txt', 'r', encoding='utf-8')
#print(f.read())

word_dic = {}
lines = f.read().split('\n')
f.close()
print(len(lines))  # 줄 행수

for line in lines:
    datas = okt.pos(line)  # 품사
    #print(datas)
    for word in datas:
        if word[1] == 'Noun':
            #print(word[0])
            if not(word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1
            
print(word_dic)

keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)  # reverse=True : descening
print(keys)

wlist = []
coulist = []

for word, count in keys[:20]:
    wlist.append(word)
    coulist.append(count)

# 데이터 전처리 후 model에 추가 (DataFrame)
#######################    
df = pd.DataFrame()
df['word'] = wlist
df['count'] = coulist
print(df)
#######################
print('---------word2vec-----------')

results = []

with open('aaa.txt', 'r', encoding='utf-8') as fr:
    lines = fr.read().split("\n")

for line in lines:
    datas = okt.pos(line, stem=True)  # 품사
    #print(datas)
    imsi = []
    for word in datas:
        if not word[1] in ['Verb', 'Josa', 'Modifier', 'Suffix', 'Punctuation', 'Number']:
            imsi.append(word[0])
        imsi2 = ("".join(imsi)).strip()
        results.append(imsi2)
        
print(results)


# file로 저장
fileName = 'news.txt'
with open(fileName, 'w', encoding='utf-8') as fw:
    fw.write('\n'.join(results))
    print('저장성공')
    
from gensim.models import word2vec
genObj = word2vec.LineSentence(fileName)
print(genObj)

model = word2vec.Word2Vec(genObj, 
                          size=100, window=10, # size : 차원을 뜻함, window : 주변단어갯수
                          min_count=2, sg=1)  # min_count : 참여횟수, sg = 0은 CBOW, 1은 Skip-gram
print(model)
#model.init_sims(replace = True) # 필요없는 메모리 정리


# 모델 생성 후 저장
# try:
#     model.save('news.model')
#     print('ok')
# except Exception as e:
#     print('fail')

# 모델을 이용해 단어 간의 친밀도 확인
model = word2vec.Word2Vec.load('news.model')
#print(model.similarity('국장', '국가'))
print(model.similarity('대통령', '트럼프'))

print()
print(model.wv.most_similar(positive=['트럼프']))
print()
print(model.wv.most_similar(positive=['트럼프'], tops=3))
print()
print(model.wv.most_similar(positive=['트럼프','대통령'], negative=['중단']))









            
