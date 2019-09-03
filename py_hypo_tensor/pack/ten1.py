# Tensorflow
import tensorflow as tf

a = 1            # 0 tensor - scala
print(type(a))
a = [1, 2]       # 1 tensor - vector
print(type(a))
a = [[1,2],[3,4]]  # 2 tensor - matrix
print(type(a))

hello = tf.constant('Hello') # 상수 선언
print(hello)
print(type(hello)) # lass 'tensorflow.python.framework.ops.Tensor' 다차원배열
world = tf.constant('여름은 가고') # 상수 선언

a = tf.constant(1)
b = tf.constant([1])
c = tf.constant([5, 10], dtype=tf.int32)
d = a + b + c
print(d)

print('---------------')
sess = tf.Session()
result1 = sess.run(hello)
print(result1)
result2 = sess.run(world)
print(result2.decode(encoding='utf-8'))
result3 = sess.run(d)
print(result3)
sess.close()

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
