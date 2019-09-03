# MultiRnnCell - 긴 문장을 처리
# 4글자로 구성된 단어에서 입력으로 3글자를 제공하면 마지막 글자 추천받기
import tensorflow as tf
import numpy as np
from tensorflow.python.framework.test_ops import n_in_polymorphic_twice

#char_arr = ['a','b' ...]
char_arr = [c for c in 'abcdefghijklmnopqrstuvwxyz']
print(char_arr)

num_dic = {n:i for i, n in enumerate(char_arr)}
print(num_dic)
dic_len = len(num_dic)  # 26

# wor <= x,  d <= y
seq_data = ['word','wood','deep','dive','cold','cool','load','love','kind','king']
print(seq_data[1], ' ', seq_data[:1], ' ', seq_data[-1], ' ', seq_data[:-1])

# one_hot encode 예
# imsi = []
# kbs = [0, 3, 6]
# imsi.append(np.eye(10)[kbs])
# print('imsi : ', imsi)

def make_batch(seq_data):
    input_batch = []
    target_batch = []
    
    for seq in seq_data:     # wor|d
        input = [num_dic[n] for n in seq[:-1]]
        #print('input : ', input)  # input :  [22 w, 14 o, 17 r] ...
        target = num_dic[seq[-1]]
        #print('target : ', target)  # target :  3 d ...
        input_batch.append(np.eye(dic_len)[input])
        target_batch.append(target)
    
    return input_batch, target_batch
    
# a, b = make_batch(seq_data)
# print('-------------')
# print(a)
# print()
# print(b)

#n_hidden = 26
n_hidden = 128
total_epoch = 100
n_step = 3
n_input = n_class = dic_len

#-------------
x = tf.placeholder(tf.float32, [None, n_step, n_input])
y = tf.placeholder(tf.int32)
w = tf.Variable(tf.random_normal([n_hidden, n_class]))
b = tf.Variable(tf.random_normal([n_class]))

cell1 = tf.nn.rnn_cell.LSTMCell(n_hidden)
cell1 = tf.nn.rnn_cell.DropoutWrapper(cell1, output_keep_prob=0.5) # 과적합 방지
cell2 = tf.nn.rnn_cell.LSTMCell(n_hidden)
multi_cell = tf.nn.rnn_cell.MultiRNNCell([cell1, cell2])
outputs, states = tf.nn.dynamic_rnn(multi_cell, x, dtype=tf.float32)
print(outputs)
outputs = tf.transpose(outputs, [1, 0, 2])
print(outputs)
outputs = outputs[-1]
print(outputs)

model = tf.matmul(outputs, w) + b
cost = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=model, labels=y))
optimizer = tf.train.AdamOptimizer(0.01).minimize(cost)


# --------------
sess = tf.Session()
sess.run(tf.global_variables_initializer())

input_batch, target_batch = make_batch(seq_data)
# print('input_batch : ', input_batch)
# print('target_batch : ', target_batch)
for epoch in range(total_epoch):
    _, loss = sess.run([optimizer, cost], feed_dict={x:input_batch, y:target_batch})
    print('epoch:', epoch, ' cost:{:.5f}'.format(loss))

# 예측값 및 정확도
prediction = tf.cast(tf.argmax(model, 1), tf.int32)
pred_chk = tf.equal(prediction, y)
accuracy = tf.reduce_mean(tf.cast(pred_chk, tf.float32))

predict, accuracy_val = sess.run([prediction, accuracy], feed_dict={x:input_batch, y:target_batch})
print('predict : ', predict)
for i in range(10):
    print('char : ', char_arr[predict[i]])

print('accuracy_val : ', accuracy_val)

print()
predict_words = []
for idx, val in enumerate(seq_data):
    last_char = char_arr[predict[idx]]
    predict_words.append(val[:3] + last_char)
    
print('예측 입력 값 : ', [w[:3] + '' for w in seq_data])
print('예측값  : ', predict_words)



















