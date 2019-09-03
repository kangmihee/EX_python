# RNN  - sequence data로 자연어에 대해 이전문자를 참조하여 다음문자를 예측
import tensorflow as tf
import numpy as np

# test1  : 1,1,4
# data = np.array([[[1,0,0,0]]], dtype=np.float32)
# print(data.shape)

# test2  : one-hot encoding한 여러개 사용 - 1,2,3,4,5
one_hot = [[[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]]
data = np.array(one_hot,  dtype=np.float32)

hidden_size = 2 # 출력 수
#cell = tf.contrib.rnn.BasicRNNCell(num_units=hidden_size)
cell = tf.nn.rnn_cell.LSTMCell(num_units=hidden_size)  # cell 생성
outputs, states = tf.nn.dynamic_rnn(cell, data, dtype=tf.float32)
print(outputs.shape)  # (1:batch size, 1:sequence수, 2:출력수)

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
#print(sess.run(outputs))
print(outputs.eval())  # [[[ 0.04574287 -0.03133253]]]

