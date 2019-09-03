# 변수 : Variable
import tensorflow as tf

var = tf.Variable([1,2,3,4,5], dtype=tf.float32)
v1 = tf.Variable([3])
v2 = tf.Variable([5])
v3 = v1 * v2 + 10
print(v3)

# sess = tf.Session()
# ...
# sess.close()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(var + 10))
    
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(v3))


