# CNN
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

sess = tf.InteractiveSession()
image = np.array([[[[1],[2],[3]], [[4],[5],[6]], [[7],[8],[9]]]], dtype=np.float32)
print(image.shape)  # (1, 3, 3, 1)

plt.imshow(image.reshape(3,3), cmap='Greys')
plt.show()

# filter
weight = tf.constant([[[[1.]],[[1.]]],[[[1.]],[[1.]]]])
print(weight.shape)  # (2, 2, 1, 1)   (너비,높이,입력채널수,필터수)

# padding을 VALID를 설정 : 0으로 채우기 X
conv2d = tf.nn.conv2d(image, weight, strides=[1,1,1,1], padding='VALID')
conv2_img = conv2d.eval()
print('conv2_img VALID : ', conv2_img.shape)
print(conv2_img)

# sub sampling
for i, one_img in enumerate(conv2_img):
    #print(conv2_img.reshape(2,2))
    plt.subplot(1, 2, i + 1)
    plt.imshow(one_img.reshape(2,2), cmap='Greys')
    plt.show()

# padding을 SAME를 설정 : 0으로 채우기 O
conv2d = tf.nn.conv2d(image, weight, strides=[1,1,1,1], padding='SAME')
conv2_img = conv2d.eval()
print('conv2_img VALID : ', conv2_img.shape)
print(conv2_img)

conv2_img = np.swapaxes(conv2_img, 0, 3)
# sub sampling
for i, one_img in enumerate(conv2_img):
    #print(conv2_img.reshape(3,3))
    plt.subplot(1, 2, i + 1)
    plt.imshow(one_img.reshape(3,3), cmap='Greys')
    plt.show()













