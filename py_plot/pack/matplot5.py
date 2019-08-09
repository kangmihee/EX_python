'''
Created on 2019. 7. 30.

@author: acorn
'''
import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/iris.csv")
print(iris_data.info(), '\n')
print('iris_data : \n', iris_data.head(3), '\n')

# plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
# plt.xlabel('Sepal.Length')
# plt.ylabel('Petal.Length')
# plt.show()

iris_col = iris_data.loc[:, 'Sepal.Length':'Petal.Width']
print('Sepal.Length ~ Petal.Width까지의 데이터 : \n', iris_col.head(3))

from pandas.plotting import scatter_matrix
# scatter_matrix(iris_col, diagonal='kde')
# scatter_matrix(iris_col)
# plt.show()
print()

print(iris_data['Species'].unique())

cols = []
for s in iris_data['Species']: # iris_data의 꽃의 종류
    choice = 0
    if s == 'setosa': choice = 1
    elif s == 'versicolor': choice = 2
    elif s == 'virginica': choice = 3
    cols.append(choice)
    
# plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'], c=cols)
# plt.xlabel('Sepal.Length')
# plt.ylabel('Petal.Length')
# plt.show()

import seaborn as sns

plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

# sns.pairplot(iris_col)
# plt.title("seaborn 사용")
# plt.show()

x = iris_data['Sepal.Length'].values
sns.rugplot(x)
plt.show()

sns.kdeplot(x) # 데이터 분포 상태를 보여준다. seaborn이 제공한다.
plt.show()