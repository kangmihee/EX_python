# 연속형 -> 범주형으로 분류
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from keras.optimizers import SGD, Adam, RMSprop
from pack.ten32rnn_mnist import x_test

# train dataset
x_train = np.random.random((1000, 12))
y_train = np.random.randint(10, size=(1000, 1))
y_train = to_categorical(y_train, num_classes=10)  # one_hot encoding
print(x_train.shape)  # (1000, 12)
print(y_train.shape)  # (1000, 10)
#print(y_train[:2])  # [[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]...

# test dataset
x_test = np.random.random((100, 12))
y_test = np.random.randint(10, size=(100, 1))
y_test = to_categorical(y_test, num_classes=10)  # one_hot encoding

model = Sequential()
model.add(Dense(10, input_dim = 12, activation='softmax'))

model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

result = model.fit(x_train, y_train, epochs=1000, batch_size=64, verbose=1)
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

plt.plot(result.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()


# 예측
x_test_new = np.random.random([2, 12]) 
#pred = model.predict(x_test_new)
pred = model.predict_classes(x_test_new, batch_size=1)
print('예측 결과 : ', pred)
