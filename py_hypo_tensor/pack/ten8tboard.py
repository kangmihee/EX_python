# 텐서보드 : 텐서플로우의 수행과정을 시각화. 알고리즘 동작 확인

import tensorflow as tf

with tf.name_scope("scope_a"):
    a = tf.add(1, 2, name='a_add')
    b = tf.multiply(a, 3, name='a_mul')

with tf.name_scope("scope_b"):
    c = tf.add(4, 5, name='b_add')
    d = tf.multiply(a, 6, name='b_mul')

e = tf.add(b, d, name="output")

with tf.Session() as sess:
    tf.summary.merge_all
    writer = tf.summary.FileWriter("./board", sess.graph)
    
    sess.run(tf.global_variables_initializer())
    print(sess.run(c))
    print(sess.run(e))
    
    writer.close()
