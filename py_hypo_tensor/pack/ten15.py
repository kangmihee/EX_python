# 다중선형회귀
import tensorflow as tf
import matplotlib.pyplot as plt
x1 = [1,0,3,0,5]
x2 = [0,2,4,4,0]
y = [1,2,3,4,5]

tf.random.set_random_seed(12)
w1 = tf.Variable(tf.random_uniform([1], -100, 100))
w2 = tf.Variable(tf.random_uniform([1], -100, 100))
b = tf.Variable(tf.random_uniform([1], -100, 100))

h = w1 * x1 + w2 * x2 + b
cost = tf.reduce_mean(tf.square(h - y))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

print('step\t','cost\t','w1\t','w2\t','b')
for step in range(1001):
    sess.run(train)
    if step % 100 == 0:
        print(step, sess.run(cost), sess.run(w1),sess.run(w2),sess.run(b))

sess.close()






