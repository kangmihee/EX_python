# placeholder()

import tensorflow as tf
import numpy as np

#ph = tf.placeholder(dtype=tf.float32, shape=[3,3])
ph = tf.placeholder(dtype=tf.float32)
print(ph)

y = tf.add(ph , 10)

data = range(1, 11)
a = tf.placeholder(tf.int32, shape=[])
tot = tf.Variable(0)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    #print(sess.run(y))
    imsi = np.random.randn(3,3)
    print(sess.run(y, feed_dict={ph:imsi}))
    print()
    for i in range(10):
        sess.run(tf.assign(tot, tf.add(tot, a)),
                 feed_dict={a:data[i]})
    print('tot : ', sess.run(tot))
    