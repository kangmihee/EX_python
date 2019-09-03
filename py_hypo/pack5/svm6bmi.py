# BMI 식을 이용홰 자료를 무작위 작성 후 분류
# 몸무게(kg) / (키(cm) * 키(cm))

import random

def calc_bmi(h, w):
    bmi = w / (h/100) ** 2
    if bmi < 18.5: return 'thin'
    if bmi < 25: return 'normal'
    return 'fat'
'''
fp = open('bmi.csv', 'w', encoding='utf-8')
fp.write('height,weight,label\n')

# 무작위로 데이터 생성
cnt = {'thin':0, 'normal':0, 'fat':0} 
random.seed(12)
for i in range(50000):
    h = random.randint(150, 200)
    w = random.randint(35, 100)
    label = calc_bmi(h, w)
    cnt[label] += 1
    fp.write('{0},{1},{2}\n'.format(h, w, label))
    
fp.close()
print('ok', cnt)
'''

import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

tbl = pd.read_csv('bmi.csv')
print(tbl.head(5))

label = tbl['label']
h = tbl['height'] / 200 # 0 ~ 1 범위내로 정규화
w = tbl['weight'] / 100 # 0 ~ 1 범위내로 정규화
wh = pd.concat([w, h], axis=1)
print(label[:2])
print(wh[:2])








