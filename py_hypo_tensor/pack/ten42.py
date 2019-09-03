# MNIST (패션잡화) 자료로 분류
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels),(test_images, test_labels) = fashion_mnist.load_data()

# print(train_images[0], ' ', train_images.shape) # (60000, 28, 28)
# print(train_labels[0], ' ', train_labels.shape) # 9   (60000,)

class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
train_images = train_images / 255.0
test_images = test_images / 255.0
#print(train_images[0])

# plt.imshow(train_images[0])
# plt.colorbar()
# plt.show()

# plt.figure(figsize=(10, 10))
# for i in range(25):
#     plt.subplot(5, 5, i + 1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.imshow(train_images[i])
#     plt.xlabel(class_names[train_labels[i]])
#     
# plt.show()

# 모델 작성 후 작업
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, verbose=1)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('loss : ', test_loss)
print('정확도 : ', test_acc)

pred = model.predict(test_images)
print(pred[0])
print('예측값 : ', np.argmax(pred[0]))
print('실제값 : ', test_labels[0])

# 각 이미지 시각화
def plot_image(i, pred_arr, true_label, img):
    pred_arr, true_label, img = pred_arr[i], true_label[i], img[i]
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img)
    pred_label = np.argmax(pred_arr)
    if pred_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[pred_label],
                                         100 * np.max(pred_arr),
                                         class_names[true_label]), color=color)

def plot_value_arr(i, pred_arr, true_label):
    pred_arr, true_label = pred_arr[i], true_label[i]
    thisplot = plt.bar(range(10), pred_arr)
    pred_label = np.argmax(pred_arr)
    thisplot[pred_label].set_color('red')
    thisplot[true_label].set_color('blue')

i = 0
plt.figure(figsize=(6, 3))
plt.subplot(1,2,1)
plot_image(i, pred, test_labels, test_images)

plt.subplot(1,2,2)
plot_value_arr(i, pred, test_labels)

plt.show()

 

















