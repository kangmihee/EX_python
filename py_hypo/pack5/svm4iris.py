import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import  seaborn as sns
from sklearn.datasets import load_iris
from sklearn import svm
from sklearn.model_selection import train_test_split


iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['target_names'] = iris.target_names[iris.target]
print(iris_df.head(3))

from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
print(pysqldf)

iris_df['is_setosa'] = pysqldf("""
    select *, case when target_names='setosa' then 1 else 0 end is_setosa
    from iris_df
""")['is_setosa']

print(print(iris_df.head(2)))
print(print(iris_df.tail(2)))

# train, test
train_set, test_set = train_test_split(iris_df, test_size=0.3)
print(train_set.shape)
#sns.pairplot(data=train_set, hue='target_names', height=5, \
#             x_vars=['sepal length (cm)'], y_vars=['petal length (cm)'])
#plt.show()

# print(print(iris_df.head(2)))

# print(print(iris_df.head(2)))

# SVM
model = svm.LinearSVC(C=10)
model.fit(X = train_set[['sepal length (cm)', 'petal length (cm)']], \
          y = train_set[['is_setosa']])
# 예측값
pred = model.predict(X = test_set[['sepal length (cm)', 'petal length (cm)']])
print(pred)

# 정확도
#print(model.score(X = train_set[['sepal length (cm)', 'petal length (cm)']], \
#                  y = train_set[['is_setosa']]))
#print(model.score(X = test_set[['sepal length (cm)', 'petal length (cm)']], \
#                  y = test_set[['is_setosa']]))

# 시각화
fig = plt.figure()
plt.scatter(iris_df[iris_df.is_setosa == 0]['sepal length (cm)'], \
            iris_df[iris_df.is_setosa == 0]['petal length (cm)'], marker = '+')

plt.scatter(iris_df[iris_df.is_setosa == 1]['sepal length (cm)'], \
            iris_df[iris_df.is_setosa == 1]['petal length (cm)'], marker = 'o', c='red')           

aa = np.linspace(4,8)
bb = -(model.coef_[:,0] * aa + model.intercept_) / model.coef_[:, 1]

plt.plot(aa,bb, color='b', label='decision line')
plt.legend()
plt.show()

































