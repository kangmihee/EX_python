# 로지스틱 회귀
import tensorflow as tf
import numpy as np

# 자료1
# x_data = [[1,2],[2,3],[3,4],[4,3],[3,2],[2,1]]
# y_data = [[0],[0],[0],[1],[1],[1]]

# 자료2 : 키, 몸무게, 시력
from sklearn.preprocessing import normalize  # 정규화
x_data = [[155, 42, 0.8],[172, 42, 0.2],[188, 45, 0.5],
          [166, 53, 1.0],[175, 73, 1.5],[195, 82, 1.5]]
x_data = normalize(x_data)
y_data = [[0],[0],[0],[1],[1],[1]]

#x = tf.placeholder(tf.float32, shape=[None, 2])
x = tf.placeholder(tf.float32, shape=[None, 3])  # 자료2
y = tf.placeholder(tf.float32, shape=[None, 1])

#w = tf.Variable(tf.random_normal([2, 1]), name='weight')
w = tf.Variable(tf.random_normal([3, 1]), name='weight')  # 자료2
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.sigmoid(tf.matmul(x, w) + b)
cost = -tf.reduce_mean(y * tf.log(hypothesis) + (1 - y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

predict = tf.cast(hypothesis > 0.5, dtype=tf.float32)  # true:1, false:0
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(5001):
        sess.run(train, feed_dict={x:x_data, y:y_data})
        if step % 200 == 0:
            print(step, sess.run(cost, feed_dict={x:x_data, y:y_data}))
    # 정확도 출력
    h, c, a = sess.run([hypothesis, predict, accuracy], feed_dict={x:x_data, y:y_data})
    print('\nhypothesis:', h, '\ncorrect:',c, '\naccuracy:', a)
    # 새로운 값으로 예측 - 자료1
    '''
    x_newdata = [[1,1],[3,3],[8,4]]
    result = sess.run(predict, feed_dict={x:x_newdata})
    print('분류 결과 :\n', result)
    '''
    
    # 새로운 값으로 예측 - 자료
    x_newdata = normalize([[160, 50, 1.0],[136, 53, 1.5],[186, 53, 0.1]])
    result = sess.run(predict, feed_dict={x:x_newdata})
    print('분류 결과 :\n', result)














