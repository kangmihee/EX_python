# zoo dataset으로 동물 분류 (7가지)
import tensorflow as tf
import numpy as np

datas = np.loadtxt('../testdata/zoo.csv', delimiter=',', dtype=np.float32)
print(datas, ' ', datas.shape)  # (101, 17)

x_data = datas[:, 0:-1]
y_data = datas[:, [-1]]
print(x_data[:3]) # [[1. 0. 0. 1. 0. 0. 1. 1. 1. 1. 0. 0. 4. 0. 0. 1.]...
print(y_data[:3]) # [[0]...
print(set(y_data[:, 0]))  # {0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0}


outputs = 7
y_one_hot = tf.one_hot(y_data, outputs)
print(y_one_hot)  # shape=(101, 1, 7)
y_one_hot = tf.reshape(y_one_hot, [-1, outputs])
print(y_one_hot)  # shape=(101, 7)

x = tf.placeholder(tf.float32, [None, 16])
y = tf.placeholder(tf.int32, [None, 1])
w = tf.Variable(tf.random_normal([16, outputs]))
b = tf.Variable(tf.random_normal([outputs]))

logits = tf.matmul(x, w) + b
hypothesis = tf.nn.softmax(logits)
cost = tf.reduce_mean(\
    tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=y_one_hot))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

pred = tf.argmax(hypothesis, 1)
correct_pred = tf.equal(pred, tf.argmax(y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(1001):
        sess.run(optimizer, feed_dict={x:x_data, y:y_data})
        if step % 100 == 0:
            loss, acc = sess.run([cost, accuracy], feed_dict={x:x_data, y:y_data})
            print('step:{:5}\tcost:{:.3f}\tacc:{:.2%}'.format(step, loss, acc))
    
    print('새 값으로 분류')
    new_data = [[0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0., 8., 0., 0., 1.]]
    print(sess.run(pred, feed_dict={x:new_data}))













