'''
Created on 2019. 7. 30.

@author: acorn
'''
# 세 과목 시험점수의 표준 점수 출력 후 시각화
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/member.csv", encoding='ms949')
# print(data)
data = data.drop('이름', axis=1)
print(data)

kormean, korsd = data['국어'].mean(), data['국어'].std() # kormean(평균값), korsd(표준편차)
engmean, engsd = data['영어'].mean(), data['영어'].std()
matmean, matsd = data['수학'].mean(), data['수학'].std()

data['국어z값'] = (data['국어'] - kormean) / korsd
data['영어z값'] = (data['영어'] - engmean) / engsd
data['수학z값'] = (data['수학'] - matmean) / matsd

# print(data)

data['국어표준값'] = data['국어z값'] * 20 + 100
data['영어표준값'] = data['영어z값'] * 20 + 100
data['수학표준값'] = data['수학z값'] * 20 + 100

print(data)

# 원점수 시각화
plt.figure(figsize=(10, 5))
plt.plot(data['국어'], color='r', label='kor')
plt.plot(data['영어'], color='g', label='eng')
plt.plot(data['수학'], color='b', label='mat')
plt.legend()
plt.show()

# 표준점수 시각화
plt.figure(figsize=(10, 5))
plt.plot(data['국어표준값'], color='r', label='kor')
plt.plot(data['영어표준값'], color='g', label='eng')
plt.plot(data['수학표준값'], color='b', label='mat')
plt.grid()
plt.legend()
plt.show()