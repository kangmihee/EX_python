# Keras로 OR gate 분류모델 생성
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD, Adam, RMSprop
import keras

# 데이터 수집 및 가공
x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[1]])

# 모델 설정
# model = Sequential()
# model.add(Dense(1, input_dim = 2))
# model.add(Activation('sigmoid'))

model = Sequential([
    Dense(input_dim = 2, units=1),
    Activation('sigmoid')
])

#print(model)

#모델 학습 설정
#model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
#model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
#model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#model.compile(optimizer=SGD(lr=0.1), loss='binary_crossentropy', metrics=['accuracy'])
#model.compile(optimizer=SGD(lr=0.1, momentum=0.9), loss='binary_crossentropy', metrics=['accuracy'])
#model.compile(optimizer=RMSprop(lr=0.1), loss='binary_crossentropy', metrics=['accuracy'])
model.compile(optimizer=Adam(lr=0.1), loss='binary_crossentropy', metrics=['acc'])

#모델 학습
model.fit(x, y, epochs=1000, batch_size=1, verbose=2)

# 모델 평가
loss_metrics = model.evaluate(x, y)
print(loss_metrics)

model.save('test.hdf5')  # hdf5 다중객체파일 형식으로 대용량의 데이터 저장이 가능
del model
from keras.models import load_model
model2 = load_model('test.hdf5')

# 예측
pred = model2.predict(x, batch_size=1)
print('예측결과 : ', pred)

pred = model2.predict_classes(x, batch_size=1)
print('예측결과 : ', pred)

#모델 저장


















