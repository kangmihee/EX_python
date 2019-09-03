# 저장된 모델 읽어 활용
import tensorflow as tf

v1 = tf.get_variable("v1", shape=[3], initializer = tf.zeros_initializer)
v2 = tf.get_variable("v2", shape=[5], initializer = tf.zeros_initializer)

x = tf.Variable(tf.random_normal([3])) 

saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, "./tmp/model.ckpt")
    print('v1 : %s'%v1.eval())
    print('v2 : %s'%v2.eval())
    print('x : %s'%sess.run(x))
