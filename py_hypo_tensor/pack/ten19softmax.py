import tensorflow as tf
import numpy as np

x_data = [[1,2,3,4],[2,4,6,8],[3,6,9,12],
        [1,1,1,1],[2,2,2,2],[3,3,3,3],
        [1,2,1,2],[1,3,1,3],[1,4,1,4]]
# 0,0,0, 1,1,1, 2,2,2
y_data = [[1,0,0],[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,1,0],[0,0,1],[0,0,1],[0,0,1]]

output = 3
x = tf.placeholder(tf.float32, [None, 4])
y = tf.placeholder(tf.float32, [None, output])
w = tf.Variable(tf.random_normal([4,output]))
b = tf.Variable(tf.random_normal([output]))

# 방법1
# hypothesis = tf.nn.softmax(tf.matmul(x, w) + b)
# cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(hypothesis)))

# 방법2
logits = tf.matmul(x, w) + b
hypothesis = tf.nn.softmax(logits)
cost = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=y_data))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(5001):
        sess.run(optimizer, feed_dict={x:x_data, y:y_data})
        if step % 500 == 0:
            print(step, ' ', sess.run(cost, feed_dict={x:x_data, y:y_data}))
    
    print(sess.run(hypothesis, feed_dict={x:x_data}))
    #print(sum([9.9491441e-01, 1.9048452e-03, 3.1806531e-03]))
    print('예측값 : ', sess.run(tf.argmax(hypothesis, 1), feed_dict={x:x_data}))
    
    print('새값으로 분류 작업')
    new_data = sess.run(hypothesis, feed_dict={x:[[1,2,3,9],[9,9,8,8]]})
    print(new_data)
    print(sess.run(tf.argmax(new_data, 1)))
    















