# 영어단어(4글자)를 한국어 단어(2글자)로 번역 - sequence to sequence 알고리즘
import tensorflow as tf
import numpy as np

#seq2seq 모델 사용시 특수 심벌이 필요
#S:디코딩 입력의 시작 심볼
#E:디코딩 출력의 끝 심볼
#P:현재 배치 데이터의 step 크기보다 작은 경우 빈 시퀀스를 채우는 심볼
# word -> ['w','o','r','d']     to -> ['t','o','P','P']
char_arr = [c for c in 'SEPabcdefghijklmnopqrstuvwxyz단어나무놀이도서화염자바']
print(char_arr)
num_dic = {n:i for i,n in enumerate(char_arr)}
print(num_dic)
dic_len = len(num_dic)

seq_data = [['word','단어'], ['wood','나무'],['game','놀이'],
            ['book','도서'],['fire','화염'],['java','자바']]
print(seq_data[1], ' ', seq_data[:1], ' ', seq_data[-1], seq_data[:-1])

def make_batch(seq_data):
    input_batch = []
    output_batch = []
    target_batch = []
    
    for seq in seq_data:
        # 인코더 셀의 입력값. 입력 단어의 글자들을 한 글자씩 분리해 배열 작성
        input = [num_dic[n] for n in seq[0]]
        #print(input)  # [25, 17, 20, 6]  word...
        # 디코더 셀의 입력값.  시작을 나타내는 S 심볼로 시작 
        output = [num_dic[n] for n in ('S' + seq[1])]
        #print(output)  # [0, 29, 30]  S단어 ...
        target = [num_dic[n] for n in (seq[1] + 'E')]
        #print(target)   # [29, 30, 1]  단어E ...
        
        input_batch.append(np.zeros((dic_len,dic_len))[input])    # one_hot
        output_batch.append(np.zeros((dic_len,dic_len))[output])  # one_hot
        target_batch.append(target)
        
    return input_batch, output_batch, target_batch
        
#make_batch(seq_data)

n_hidden = 128
total_epoch = 100
n_class = n_input = dic_len

# 모델 구축
enc_input = tf.placeholder(tf.float32, [None, None, n_input])
dec_input = tf.placeholder(tf.float32, [None, None, n_input])
targets = tf.placeholder(tf.int32, [None, None])  # [batch_size, time steps]

# 인코더 셀 구축
with tf.variable_scope('encode'):
    enc_cell = tf.nn.rnn_cell.LSTMCell(n_hidden)
    enc_cell = tf.nn.rnn_cell.DropoutWrapper(enc_cell, output_keep_prob=0.5)
    outputs, enc_states = tf.nn.dynamic_rnn(enc_cell, enc_input, dtype=tf.float32)

# 디코더 셀 구축
with tf.variable_scope('decode'):
    dec_cell = tf.nn.rnn_cell.LSTMCell(n_hidden)
    dec_cell = tf.nn.rnn_cell.DropoutWrapper(dec_cell, output_keep_prob=0.5)
    # seq2seq 모델은 인코더셀의 최종 상태값을 디코더셀의 초기 상태값으로 넣어줘야 한다.
    outputs, dec_states = tf.nn.dynamic_rnn(dec_cell, \
                    dec_input, initial_state=enc_states, dtype=tf.float32)

# 출력층을 만들고 손실함수와 최적화함수 구성
model = tf.layers.dense(outputs, n_class, activation=None)
cost = tf.reduce_mean(\
    tf.nn.sparse_softmax_cross_entropy_with_logits(logits=model, labels=targets))
optimizer = tf.train.AdamOptimizer(0.01).minimize(cost)

#----------------------
sess = tf.Session()
sess.run(tf.global_variables_initializer())
input_batch, output_batch, target_batch = make_batch(seq_data)

for epoch in range(total_epoch + 1):
    _, loss = sess.run([optimizer, cost], \
        feed_dict={enc_input:input_batch, dec_input:output_batch, targets:target_batch})
    if epoch % 10 == 0:
        print('epoch:{}, cost:{:.5f}'.format(epoch, loss))

# 번역 연습
def translate_test(myword):
    seq_data = [myword, 'P' * len(myword)]
    #print(seq_data)  # ['word', 'PPPP']
    input_batch, output_batch, target_batch = make_batch([seq_data])
    prediction = tf.argmax(model, 2)
    #print(prediction)
    result = sess.run(prediction, \
        feed_dict={enc_input:input_batch, dec_input:output_batch, targets:target_batch})
    
    decoded = [char_arr[i] for i in result[0]]
    #print(decoded)  # ['단', '어', 'E', 'E', 'E']
    end = decoded.index('E')
    translate = ''.join(decoded[:end])
    return translate

print()
print('word ->', translate_test('word'))
print('java ->', translate_test('java'))
print('fire ->', translate_test('fire'))
print('bava ->', translate_test('bava'))
print('cord ->', translate_test('cord'))
print('korea ->', translate_test('korea'))

