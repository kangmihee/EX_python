# 케라스(Keras) 기본 개념 
#   - 케라스의 가장 핵심적인 데이터 구조는 “모델＂이다.
#   - 케라스에서 제공하는 시퀀스 모델로 원하는 레이어를 쉽게 순차적으로 쌓을 수 있다. 

#예) iris dataset으로 종류별로 분류
import tensorflow as tf
import keras
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
Y_1hot = enc.fit_transform(Y.reshape(-1, 1)).toarray()

print(Y[0], " -- one hot enocding --> ", Y_1hot[0])
print(Y[50], " -- one hot enocding --> ", Y_1hot[50])
print(Y[100], " -- one hot enocding --> ", Y_1hot[100])

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(4, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y_1hot, epochs=300, batch_size=10)
#print(model.eval‎uate(X, Y_1hot))

Y_pred = model.predict_classes(X)

print('예측값 :', Y_pred)
print('실제값 :', Y)
print('분류 실패 수:', (Y != Y_pred).sum())

new_x = np.array([[1.1, 1.1, 1.1, 1.1],[5.5, 5.5,  5.5, 5.5]])
new_pred = model.predict_classes(new_x)
print(new_pred)
