# 3차에 걸친 시험으로 판정점수 예측 - matrix type
import tensorflow as tf
import numpy as np
import pandas as pd

# x1_data = [73,93,89,96,73,53,90]
# x2_data = [80,88,91,98,66,46,90]
# x3_data = [75,93,90,100,70,55,90]
# y_data = [150,180,190,200,130,100,190]

# csv 문서 읽기
datas = np.loadtxt('../testdata/exam.csv', delimiter=',', skiprows=1, dtype=np.float32)
print(datas)
df = pd.DataFrame(datas)
print(df.head(3))
print(df.corr(method='pearson'))

x_data = datas[:,0:-1]
y_data = datas[:, [-1]]
print(x_data, x_data.shape, len(x_data))
print(y_data)

tf.random.set_random_seed(12)
x = tf.placeholder(tf.float32, shape=[None, 3])
y = tf.placeholder(tf.float32, shape=[None, 1])
w = tf.Variable(tf.random_normal([3, 1]))
b = tf.Variable(tf.random_normal([1]))

hypothesis = tf.matmul(x, w) + b
cost = tf.reduce_mean(tf.square(hypothesis - y))

#optimizer = tf.train.GradientDescentOptimizer(0.00001)
optimizer = tf.train.GradientDescentOptimizer(1.0e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
                feed_dict={x:x_data,y:y_data})
    if step % 500 == 0:
        print(step, ' cost:', cost_val, ' pred:', hy_val)

print()
# 값 예측
print(sess.run(hypothesis, feed_dict={x:[[73,80,75]]}))
print(sess.run(hypothesis, feed_dict={x:[[11,22,33],[99,90,85]]}))
                                         






