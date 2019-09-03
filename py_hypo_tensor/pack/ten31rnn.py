#RNN : 문자열에서 마지막 다음 글자를 예측 - 각 문자의의 다음 문자 예측

import tensorflow as tf
import numpy as np

# hihello로 연습
char_set = ['h','i','e','l','o']
# x_data = [[0,1,1,2,3,3]]  #hihell
x_one_hot = [[[1,0,0,0,0],[0,1,0,0,0],[1,0,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,1,0]]]
y_data = [[1,0,2,3,3,4]]   #ihello

hidden_size = 6
sequence_length = 6
input_dim = 5
batch_size = 1

#with tf.device('/cpu:0'):
    #...

x = tf.placeholder(tf.float32, [None,sequence_length,input_dim])
y = tf.placeholder(tf.int32, [None, sequence_length])

cell = tf.nn.rnn_cell.LSTMCell(num_units=hidden_size)
output, states = tf.nn.dynamic_rnn(cell, x, dtype=tf.float32)
print(output)  # shape=(?, 6, 6)

# 비용 최소화 작업
weights = tf.ones([batch_size, sequence_length]) # 1 * 6 텐서 작성 후 0으로 채움
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=output, targets=y, weights=weights)
loss = tf.reduce_mean(sequence_loss)
optimizer = tf.train.AdamOptimizer(0.01).minimize(loss)

pred = tf.argmax(output, axis=2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        los, _ = sess.run([loss, optimizer], feed_dict={x:x_one_hot, y:y_data})
        result = sess.run(pred, feed_dict={x:x_one_hot})
        if i % 100 == 0:
            print(i, ' loss:', los, ' predict:', result, ' y_data:', y_data)

    print('--------')
    print(result.shape, np.squeeze(result.shape))
    
    result_str = [char_set[c] for c in np.squeeze(result)]
    print('최종 결과 :', ''.join(result_str))
















