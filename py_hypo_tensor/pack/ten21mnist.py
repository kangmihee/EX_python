# MNIST 분류
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("./data/", one_hot = True)

training_epochs = 25
batch_size = 100  # 데이터 처리를 100개 묶음으로 처리

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# w = tf.Variable(tf.zeros([784, 10]))
# b = tf.Variable(tf.zeros([10]))
#logits = tf.matmul(x, w) + b
#hypothesis = tf.nn.softmax(logits)
#hypothesis = tf.nn.relu(logits)
#cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=y))

# 정확도 향상을 위해 layer 추가
w1 = tf.Variable(tf.random_normal([784, 256]))
w2 = tf.Variable(tf.random_normal([256, 256]))
w3 = tf.Variable(tf.random_normal([256, 10]))

b1 = tf.Variable(tf.random_normal([256]))
b2 = tf.Variable(tf.random_normal([256]))
b3 = tf.Variable(tf.random_normal([10]))

L1 = tf.nn.relu(tf.add(tf.matmul(x, w1), b1))  # Hidden layer
L2 = tf.nn.relu(tf.add(tf.matmul(L1, w2), b2))
hypothesis = tf.add(tf.matmul(L2, w3), b3)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=hypothesis, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for epoch in range(training_epochs):
    avg_cost = 0
    
    total_batch = int(mnist.train.num_examples / batch_size)  # 확룰적 학습
    for i in range(total_batch):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        _, c = sess.run([optimizer, cost], feed_dict={x:batch_x, y:batch_y})
        avg_cost += c / total_batch
    if (epoch + 1) % 5 == 0:
        print('epoch:', '%03d'%(epoch + 1), 'cost:','{:.5f}'.format(avg_cost))
        
# 모델 평가
cor_pred = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(cor_pred, tf.float32))
print('accuracy : ', sess.run(accuracy, feed_dict={x:mnist.test.images, y:mnist.test.labels}))

# 숫자 이미지 예측하기
import random
r = random.randrange(mnist.test.num_examples)
print(r)
#print(mnist.test.labels[0:1])
print('실제값 : ', sess.run(tf.argmax(mnist.test.labels[r:r+1], 1)))
print('예측 값: ', sess.run(tf.argmax(hypothesis, 1), feed_dict={x:mnist.test.images[r:r+1]}))










