# MNIST 손글씨로 분류
import tensorflow as tf

(x_train,y_train),(x_test,y_test) = tf.keras.datasets.mnist.load_data()
print(len(x_train), len(y_train),len(x_test), len(y_test))

new_x = x_test

print(x_train.shape)
x_train = x_train.reshape(60000, 784).astype('float32')
x_test = x_test.reshape(10000, 784).astype('float32')
#print(x_train[0])  # 0.   0.  55. 172. 226.
x_train /= 255
x_test /= 255
#print(x_train[0])  # 0.         0.         0.11764706 0

# label은 one_hot
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)
#print(y_train[0])  # [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]

# 모델 적용
model = tf.keras.Sequential()

# layer 1
model.add(tf.keras.layers.Dense(512, input_shape=(784,)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.5))

# layer 2
model.add(tf.keras.layers.Dense(512, kernel_regularizer=tf.keras.regularizers.l2(0.001)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dropout(0.5))

# layer 3 : 마지막
model.add(tf.keras.layers.Dense(10))
model.add(tf.keras.layers.Activation('softmax'))

model.compile(optimizer=tf.keras.optimizers.Adam(), 
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=128)

score = model.evaluate(x_test, y_test)
print('loss : ', score[0])
print('accuracy : ', score[1])

pred = model.predict(x_test)
print('pred : ', pred)
import numpy as np
print(np.argmax(pred, 1))







