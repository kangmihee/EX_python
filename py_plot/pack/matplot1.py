'''
Created on 2019. 7. 30.

@author: acorn
'''
# matplotlib : 플로팅 라이브러리
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib.inline

plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

# x = ['서울','인천','수원'] # list, tuple type까지 가능. set은 불가능(순서가 없기 때문에, dict도 안됨).
# x = ('서울','인천','수원')
# y = [5, 3, 7]
# plt.xlim([-1, 3])
# plt.ylim([0, 10]) # limit 값
# plt.plot(x, y)
# plt.yticks(list(range(0, 11, 3))) # y축 tick(숫자 범위)을 설정, 0 ~ 11 까지 step 3씩
# plt.show()

# data = np.arange(1, 11, 2) # y축 값을 주면 x축은 y축에 대한 구간값으로 자동 설정된다.
# print(data)
# plt.plot(data)
# plt.show()
# 
# plt.plot(data)
# plt.plot(data, data, 'r')
# plt.show()

# x = np.arange(10)
# y = np.sin(x)
# print(x, y)
# plt.plot(x, y)
# plt.plot(x, y, 'bo') # 'bo' 두꺼운 동그라미 그래프 생성
# plt.plot(x, y, 'r+') # 'r+' 빨간색 + 그래프 생성
# plt.plot(x, y, 'go--', linewidth=2, markersize=12) # 'go--' 초록색 동그라미 '--' 선 그래프 생성, 선 두께=2, makersize=12
# plt.plot(x, y, 'go--', lw=2, ms=12) # 위와 같다. linewidth = lw, markersize = ms 로 줄여서 사용 가능.
# plt.show()

x = np.arange(0, np.pi * 3, 0.1)
print(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

# plt.figure(figsize=(10, 5))
# plt.plot(x, y_sin, 'r')
# plt.scatter(x, y_cos) # 점선
# plt.xlabel('x축')
# plt.ylabel('y축')
# plt.title('제목')
# plt.legend(['sine','cosine']) # 범례
# plt.show()

# subplot
# plt.subplot(2, 1, 1) # 2개로 나눠서 나타내는데 (1,1)번째
# plt.plot(x, y_sin)
# plt.title('싸인')
# plt.subplot(2, 1, 2) # 2개로 나눠서 나타내는데 (1,2)번째
# plt.plot(x, y_cos)
# plt.title('코싸인')
# plt.show()

irum = ['a','b','c','d','e']
kor = [80,50,70,70,90]
eng = [60,70,80,70,60]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'gs-') # 초록색 네모점 '-'선
plt.ylim([0, 100])
plt.legend(['국어','영어'], loc=4) # 범례, loc : 범례 위치
plt.grid(True) # grid 선 노출
# plt.show()

fig = plt.gcf() # figure 객체에 접근가능.
plt.show()
fig.savefig('test.png') # 이미지로 저장

from matplotlib.pyplot import imread
img = imread('test.png')
plt.imshow(img)
plt.show()