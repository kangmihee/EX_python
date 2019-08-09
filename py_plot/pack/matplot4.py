'''
Created on 2019. 7. 30.

@author: acorn
'''
# matplotlib의 기능 추가 패키지 중 seaborn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def sinplot():
    x = np.linspace(1, 15, 100)
    plt.plot(x, np.sin(x))
    plt.show()
    
# sinplot()
sns.set_style("whitegrid")
sinplot()

titanic = sns.load_dataset("titanic")
print(titanic.info()) # titanic에 대한 정보를 확인할 수 있다.
titanic_size = titanic.pivot_table(index='class', columns='sex', aggfunc='size')
print(titanic_size)

sns.heatmap(titanic_size, cmap=sns.light_palette("gray", as_cmap=True), annot=True) # annot=True : 데이터값 노출
plt.show()



