# 객체의 저장 및 읽기 : save/restore

import tensorflow as tf

v1 = tf.get_variable("v1", shape=[3], initializer = tf.zeros_initializer)
v2 = tf.get_variable("v2", shape=[5], initializer = tf.zeros_initializer)
inc_v1 = v1.assign(v1 + 10)
inc_v2 = v2.assign(v2 - 1)
x = tf.Variable(tf.random_normal([3]))

saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    inc_v1.op.run()
    inc_v2.op.run()
    print(sess.run(x))
    save_path = saver.save(sess, "./tmp/model.ckpt")
    print("Model saved in path : %s"%save_path)
