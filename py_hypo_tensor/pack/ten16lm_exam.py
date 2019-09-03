# 3차에 걸친 시험으로 판정점수 예측 - vector type
import tensorflow as tf

x1_data = [73,93,89,96,73,53,90]
x2_data = [80,88,91,98,66,46,90]
x3_data = [75,93,90,100,70,55,90]
y_data = [150,180,190,200,130,100,190]

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

tf.random.set_random_seed(12)
w1 = tf.Variable(tf.random_normal([1]))
w2 = tf.Variable(tf.random_normal([1]))
w3 = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.random_normal([1]))

hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + b
cost = tf.reduce_mean(tf.square(hypothesis - y))

#optimizer = tf.train.GradientDescentOptimizer(0.00001)
optimizer = tf.train.GradientDescentOptimizer(1.0e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
                feed_dict={x1:x1_data,x2:x2_data,x3:x3_data,y:y_data})
    if step % 500 == 0:
        print(step, ' cost:', cost_val, ' pred:', hy_val)



