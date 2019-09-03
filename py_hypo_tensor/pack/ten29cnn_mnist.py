# CNN으로 손글씨 분류
import tensorflow as tf
import random
from tensorflow.examples.tutorials.mnist import input_data
from nltk.chunk.util import accuracy
mnist = input_data.read_data_sets('./goMNIST_data/', one_hot=True)

tf.reset_default_graph()  # 커널 초기화

training_epochs = 3
batch_size = 128

x = tf.placeholder(tf.float32, [None, 784])
x_img = tf.reshape(x, [-1, 28, 28, 1])  # 입력자료를 4D 텐서로 재구성
y = tf.placeholder(tf.float32, [None, 10])

# 레이어 3개 사용
# filter  [3,3,1,32], [4,4,1,32], [3,3,1,28], ...
w1 = tf.Variable(tf.random_normal([3,3,1,32], stddev=0.01))
L1 = tf.nn.conv2d(x_img, w1, strides=[1,1,1,1], padding='SAME')
L1 = tf.nn.relu(L1)
L1 = tf.nn.max_pool(L1, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME') 

w2 = tf.Variable(tf.random_normal([3,3,32,64], stddev=0.01))
L2 = tf.nn.conv2d(L1, w2, strides=[1,1,1,1], padding='SAME')
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME') 

L2 = tf.reshape(L2, [-1, 7 * 7 * 64])  # 28 * 28 -> 14 * 14 -> 7 * 7
w3 = tf.get_variable('w3', shape=[7*7*64, 10],
                     initializer = tf.contrib.layers.xavier_initializer())
b = tf.Variable(tf.random_normal([10]))

hypo = tf.matmul(L2, w3) + b
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=hypo, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print('학습시작')
total_batch = int(mnist.train.num_examples / batch_size)

for epoch in range(training_epochs):
    avg_cost = 0
    for i in range(total_batch):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        feed_dict = {x:batch_x, y:batch_y}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch
        
    print('Epoch : ', '%04d'%(epoch + 1), ' cost:','{:.5f}'.format(avg_cost))
    
#accuracy
corr_pred = tf.equal(tf.argmax(hypo, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(corr_pred, tf.float32))
print('분류 정확도 : ', sess.run(accuracy, feed_dict={x:mnist.test.images, y:mnist.test.labels}))

print()
# 연습용 이미지 하나를 랜덤하게 뽑아 분류 확인
r = random.randint(0, mnist.test.num_examples - 1)
print('label : ', sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
print('예측 : ', sess.run(tf.argmax(hypo, 1), feed_dict={x:mnist.test.images[r:r + 1]}))





    






