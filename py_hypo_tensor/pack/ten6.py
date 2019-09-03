# 연산자, 내장함수
import tensorflow as tf

x = tf.constant(7)
y = tf.constant(3)

# 삼항연산
result1 = tf.cond(x > y, lambda : tf.add(x, y), lambda:tf.subtract(x, y))
print(result1)

f1 = lambda:tf.constant(1)
f2 = lambda:tf.constant(2)
result2 = tf.case([(tf.less(x, y), f1)], default=f2)  # if a < b return 1 else return 2

sess= tf.Session()
print(sess.run(result1))
print(sess.run(result2))

print('관계연산----------')
print(sess.run(tf.equal(1, 2)))
print(sess.run(tf.not_equal(1, 2)))
print(sess.run(tf.less(1, 2)))
print(sess.run(tf.greater(1, 2)))
print(sess.run(tf.greater_equal(1, 2)))

print('논리연산----------')
print(sess.run(tf.logical_and(True, False)))
print(sess.run(tf.logical_or(True, False)))
print(sess.run(tf.logical_xor(True, False)))
print(sess.run(tf.logical_not(True)))

print('합집합----------')
kbs = tf.constant([1,2,2,2,3])
val, idx = tf.unique(kbs)
print(sess.run(val))
print(sess.run(idx))

# tf.reduce~  : 연산 후 차원축소가 이루어짐
ar = [[1.,2.],[3.,4.]]
print(tf.reduce_sum(ar).eval(session=tf.Session()))
print(tf.reduce_mean(ar, axis=0).eval(session=tf.Session())) # 열방향
print(tf.reduce_mean(ar, axis=1).eval(session=tf.Session())) # 행방향

print()
#차원변경
import numpy as np
t = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
print(t.shape)  # (2, 2, 3)

sess = tf.Session()
print(tf.reshape(t, shape=[2, 6]).eval(session=sess))
print(tf.reshape(t, shape=[-1, 3]).eval(session=sess))
print(tf.reshape(t, shape=[-1, 6]).eval(session=sess))
print(tf.reshape(t, shape=[-1, -1, 3]).eval(session=sess))

print('--차원축소------------------')
print(tf.squeeze(t).eval(session=sess))  # 차원축소 함수 : 열 요소가 1인 배열만 가능
aa = np.array([[1],[2],[3],[4]])
print(aa.shape)
bb = tf.squeeze(aa).eval(session=sess)
print(bb, ' ', bb.shape)

print('--차원추가------------------')
tarr = tf.constant([[1,2,3],[4,5,6]])
print(sess.run(tf.shape(tarr)))  # [2 3]
sbs = tf.expand_dims(tarr, axis=0)  # 첫번째 차원을 추가해 확장
print(sess.run([sbs, tf.shape(sbs)]))  # [1, 2, 3]
print()
sbs = tf.expand_dims(tarr, axis=1)  # 두번째 차원을 추가해 확장
print(sess.run([sbs, tf.shape(sbs)]))  # [1, 2, 3]
print()
sbs = tf.expand_dims(tarr, axis=2)  # 세번째 차원을 추가해 확장
print(sess.run([sbs, tf.shape(sbs)]))  # [1, 2, 3]

print('--One hot encoding------------------')
print(tf.one_hot([0,1,2,0], depth=3).eval(session=sess))
print(tf.argmax(tf.one_hot([0,1,2,0], depth=3)).eval(session=sess))














