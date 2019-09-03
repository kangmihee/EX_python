# w값을 변화시켜가며 최적의 회귀식 작성 시각화
import numpy as np
import matplotlib.pyplot as plt

w=0.1
b=0.3
vec_set = []

for i in range(1000):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * w + b + np.random.normal(0.0, 0.03)
    vec_set.append([x1, y1])
    
x_data = [v[0] for v in vec_set]
y_data = [v[1] for v in vec_set]

print(x_data[:3])
print(x_data[:3])
plt.plot(x_data, y_data, 'ro')
plt.legend()
plt.show()

# 텐서플로로 최적의 회귀선 긋기
import tensorflow as tf

w = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
model = w * x_data + b
loss = tf.reduce_mean(tf.square(model - y_data))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10):  # epoch
    sess.run(train)
    print(step, ' ', sess.run(w), ' ', sess.run(b), ' ', sess.run(loss))
    
    # 시각화
    plt.plot(x_data, y_data, 'ro')
    plt.plot(x_data, sess.run(w) * x_data + sess.run(b))
    plt.xlabel('x')
    plt.xlabel('y')
    plt.legend()
    plt.show()

