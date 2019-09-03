# RNN으로 MNIST 처리 ----------------

import tensorflow as tf
from tqdm import tqdm

tf.reset_default_graph()

# RNN 은 순서가 있는 자료를 다루므로, 한 번에 입력받는 갯수와, 총 몇 단계로 이루어져있는 데이터를 받을지를 설정.
# 이를 위해 가로 픽셀수를 n_input 으로, 세로 픽셀수를 입력 단계인 n_step 으로 설정하였다.

n_steps = 28
n_inputs = 28
n_neurons = 128
n_outputs = 10

# 신경망 모델 구성

x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])

y = tf.placeholder(tf.int32, [None])



# RNN 에 학습에 사용할 셀을 생성한다. 아래 함수들을 사용하면 다른 구조의 셀로 간단하게 변경할 수 있다
# BasicRNNCell,BasicLSTMCell,GRUCell
basic_cell = tf.contrib.rnn.BasicRNNCell(num_units=n_neurons)  

# # 원래는 다음과 같은 과정을 거쳐야 하지만
# states = tf.zeros(batch_size)
# for i in range(n_step):
#     outputs, states = cell(X[[:, i]], states)
# ...

# 아래처럼 tf.nn.dynamic_rnn 함수를 사용하면 CNN 의 tf.nn.conv2d 함수처럼 간단하게 RNN 신경망 생성.
outputs, states = tf.nn.dynamic_rnn(basic_cell, x, dtype=tf.float32)
logits = tf.layers.dense(states, n_outputs)
xentropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y)

loss = tf.reduce_mean(xentropy)
optimizer = tf.train.AdamOptimizer(learning_rate=0.001)
training_op = optimizer.minimize(loss)
correct = tf.nn.in_top_k(logits, y, 1)
accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('./tmp2/data')
x_test = mnist.test.images.reshape((-1, n_steps, n_inputs))
y_test = mnist.test.labels

n_epochs = 10  #100
batch_size = 100

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in tqdm(range(n_epochs)):
        for iteration in range(mnist.train.num_examples // batch_size):
            x_batch, y_batch = mnist.train.next_batch(batch_size)
            # X 데이터를 RNN 입력 데이터에 맞게 [batch_size, n_step, n_input] 형태로 변환.
            x_batch = x_batch.reshape((-1, n_steps, n_inputs))
            sess.run(training_op, feed_dict = {x:x_batch, y:y_batch})

    acc_train = sess.run(accuracy, feed_dict = {x:x_batch, y:y_batch})
    acc_test = sess.run(accuracy, feed_dict = {x:x_test, y:y_test})

    print(epoch, '훈련 정확도:', acc_train, '테스트 정확도:', acc_test)