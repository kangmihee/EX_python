# Char-RNN 예제
# https://github.com/solaris33/char-rnn-tensorflow
# Reference : https://github.com/sherjilozair/char-rnn-tensorflow

import tensorflow as tf
import numpy as np
from pack.utils import TextLoader

# 학습에 필요한 설정값들을 지정.
data_dir = 'data'        # 셰익스피어 희곡 <리처드 3세> 데이터로 학습
#data_dir = 'data/linux' # <Linux 소스코드> 데이터로 학습
batch_size = 50          # Training : 50, Sampling : 1
seq_length = 50          # Training : 50, Sampling : 1
hidden_size = 128        # 히든 레이어의 노드 개수
learning_rate = 0.002
num_epochs = 2
num_hidden_layers = 2
grad_clip = 5   # Gradient Clipping에 사용할 임계값

# TextLoader를 이용해서 데이터를 호출.
data_loader = TextLoader(data_dir, batch_size, seq_length)
# 학습데이터에 포함된 모든 단어들을 나타내는 변수인 chars와 chars에 id를 부여해 dict 형태로 만든 vocab을 선언.
chars = data_loader.chars 
vocab = data_loader.vocab
vocab_size = data_loader.vocab_size # 전체 단어수

# 배치 사이즈를 입력받기 위한 플레이스홀더를 설정.
input_data = tf.placeholder(tf.int32, shape=[None, None])  # input_data : [batch_size, seq_length])
target_data = tf.placeholder(tf.int32, shape=[None, None]) # target_data : [batch_size, seq_length])
state_batch_size = tf.placeholder(tf.int32, shape=[])      # Training : 50, Sampling : 1

# RNN의 마지막 히든레이어의 출력을 소프트맥스 출력값으로 변환해주기 위한 변수들을 선언.
# hidden_size -> vocab_size
softmax_w = tf.Variable(tf.random_normal(shape=[hidden_size, vocab_size]), dtype=tf.float32)
softmax_b = tf.Variable(tf.random_normal(shape=[vocab_size]), dtype=tf.float32)

# num_hidden_layers만큼 LSTM cell(히든레이어)를 선언.
cells = []
for _ in range(0, num_hidden_layers):
    cell = tf.nn.rnn_cell.BasicLSTMCell(hidden_size)
    cells.append(cell)

# cell을 종합해서 RNN을 정의.
cell = tf.contrib.rnn.MultiRNNCell(cells, state_is_tuple=True)

# 인풋데이터를 변환하기 위한 Embedding Matrix를 선언.
# vocab_size -> hidden_size
embedding = tf.Variable(tf.random_normal(shape=[vocab_size, hidden_size]), dtype=tf.float32)
inputs = tf.nn.embedding_lookup(embedding, input_data)

# 초기 state 값을 0으로 초기화.
initial_state = cell.zero_state(state_batch_size, tf.float32)

# 학습을 위한 tf.nn.dynamic_rnn을 선언.
# outputs : [batch_size, seq_length, hidden_size]
outputs, final_state = tf.nn.dynamic_rnn(cell, inputs, initial_state=initial_state, dtype=tf.float32)
# ouputs을 [batch_size * seq_length, hidden_size]] 형태로 변경.
output = tf.reshape(outputs, [-1, hidden_size])

# 최종 출력값을 설정.
# logits : [batch_size * seq_length, vocab_size]
logits = tf.matmul(output, softmax_w) + softmax_b
probs = tf.nn.softmax(logits)

# Cross Entropy 손실 함수를 정의. 
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=target_data))

# 옵티마이저를 선언하고 옵티마이저에 Gradient Clipping을 적용.
# grad_clip(=5)보다 큰 Gradient를 5로 Clippin.
tvars = tf.trainable_variables()
grads, _ = tf.clip_by_global_norm(tf.gradients(loss, tvars), grad_clip)
optimizer = tf.train.AdamOptimizer(learning_rate)
train_step = optimizer.apply_gradients(zip(grads, tvars))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for e in range(num_epochs):
        data_loader.reset_batch_pointer()
        # 초기 상태값을 지정.
        state = sess.run(initial_state, feed_dict={state_batch_size : batch_size})

        print("총 학습 수 : ", num_epochs * data_loader.num_batches)
        
        for b in range(data_loader.num_batches):
            # x, y 데이터를 호출.
            x, y = data_loader.next_batch()
            # y에 one_hot 인코딩을 적용. 
            y = tf.one_hot(y, vocab_size)            # y : [batch_size, seq_length, vocab_size]
            y = tf.reshape(y, [-1, vocab_size])       # y : [batch_size * seq_length, vocab_size]
            y = y.eval()

            # feed-dict에 사용할 값들과 LSTM 초기 cell state(feed_dict[c])값과 hidden layer 출력값(feed_dict[h])을 지정.
            feed_dict = {input_data : x, target_data: y, state_batch_size : batch_size}
            for i, (c, h) in enumerate(initial_state):
                feed_dict[c] = state[i].c
                feed_dict[h] = state[i].h

            # 한 스텝 학습을 진행.
            _, loss_print, state = sess.run([train_step, loss, final_state], feed_dict=feed_dict)
            print("학습 횟수:{}, loss:{:.3f}".format(e * data_loader.num_batches + b, loss_print))

    print("트레이닝 끝~~~")   
    
    # 샘플링 시작
    print("샘플링을 시작! ----------------------")
    num_sampling = 4000  # 생성할 글자(Character)의 개수를 지정. 
    prime = u' '         # 시작 글자를 ' '(공백)으로 지정.
    sampling_type = 1    # 샘플링 타입을 설정.
    state = sess.run(cell.zero_state(1, tf.float32)) # RNN의 최초 state값을 0으로 초기화.

    # Random Sampling을 위한 weighted_pick 함수를 정의.
    def weighted_pick(weights):
        t = np.cumsum(weights)
        s = np.sum(weights)
        return(int(np.searchsorted(t, np.random.rand(1)*s)))

    ret = prime       # 샘플링 결과를 리턴받을 ret 변수에 첫번째 글자를 할당.
    char = prime[-1]   # Char-RNN의 첫번쨰 인풋을 지정.  
    for n in range(num_sampling):
        x = np.zeros((1, 1))
        x[0, 0] = vocab[char]

        # RNN을 한스텝 실행하고 Softmax 행렬을 리턴으로 받음.
        feed_dict = {input_data: x, state_batch_size : 1, initial_state: state}
        [probs_result, state] = sess.run([probs, final_state], feed_dict=feed_dict)         

        # 불필요한 차원을 제거.
        # probs_result : (1, 65) -> p : (65)
        p = np.squeeze(probs_result)

        # 샘플링 타입에 따라 3가지 종류로 샘플링.
        # sampling_type : 0 -> 다음 글자를 예측할 때 항상 argmax를 사용
        # sampling_type : 1(defualt) -> 다음 글자를 예측할 때 항상 random sampling을 사용
        # sampling_type : 2 -> 다음 글자를 예측할 때 이전 글자가 ' '(공백)이면 random sampling, 그렇지 않을 경우 argmax를 사용
        if sampling_type == 0:
            sample = np.argmax(p)
        elif sampling_type == 2:
            if char == ' ':
                sample = weighted_pick(p)
            else:
                sample = np.argmax(p)
        else:
            sample = weighted_pick(p)

        pred = chars[sample]
        ret += pred     # 샘플링 결과에 현재 스텝에서 예측한 글자를 추가. (예를 들어 pred=L일 경우, ret = HEL -> HELL)
        char = pred     # 예측한 글자를 다음 RNN의 인풋으로 사용.

    print("샘플링 결과:")
    print(ret)
