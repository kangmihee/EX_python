# 단순선형회귀 : 학습시간에 따른 성적결과 예측
import tensorflow as tf
import matplotlib.pyplot as plt

xdata = [1,2,3,4,5]
ydata = [20,30,38,45,66]

plt.scatter(xdata, ydata)
plt.xlabel('study per hour')
plt.ylabel('score')
plt.ylim([0, 100])
plt.xlim([0, 10])
plt.show()

w = tf.Variable(tf.random_uniform([1], -100, 100))
b = tf.Variable(tf.random_uniform([1], -100, 100))
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

h = w * x + b
cost = tf.reduce_mean(tf.square(h - y))  # loss, cross entropy
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1001):
    sess.run(train, feed_dict = {x:xdata, y:ydata})
    if i % 100 == 0:
        print(i, sess.run(cost, feed_dict = {x:xdata, y:ydata}), ' ',
                          sess.run(w), ' ', sess.run(b))

print(sess.run(h, feed_dict = {x:[6]}))
print(sess.run(h, feed_dict = {x:[7, 8]}))




