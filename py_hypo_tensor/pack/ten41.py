# bmi 분류
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np

bmi = pd.read_csv('../testdata/bmi.csv')
print(bmi.head(3), bmi.shape)

bmi['weight'] /= 100
bmi['height'] /= 200

x = bmi[['weight', 'height']].as_matrix()
bclass = {'thin':[1,0,0],'normal':[0,1,0],'fat':[0,0,1]}
y = np.empty((20000, 3))

for i, v in enumerate(bmi['label']):
    y[i] = bclass[v]
print(y)

# train / test ( 3:1 )
x_train, y_train = x[0:15000], y[0:15000]
x_test, y_test = x[15000:], y[15000:]
print(len(x_train), len(x_test))

# 모델
model = Sequential()

#1
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.3))
#2
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.3))
#3
model.add(Dense(3))
model.add(Activation('softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=32, epochs=20,
          callbacks = [EarlyStopping(monitor='val_loss', patience=5)])

score = model.evaluate(x_test, y_test)
print('loss : ', score[0])
print('accuracy : ', score[1])

print(model.summary())











