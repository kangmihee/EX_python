# BMI 자료 분류
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

bmid = pd.read_csv('../testdata/bmi.csv')
print(bmid.head(2))
print('전체 행수 : ', len(bmid))  # 20000

bmid['height'] = bmid['height'] / 200  # 정규화
bmid['weight'] = bmid['weight'] / 100  # 정규화
print(bmid.head(2))

bclass = {'thin':[1,0,0],'normal':[0,1,0],'fat':[0,0,1]}
bmid['label_onehot'] = bmid['label'].apply(lambda x:np.array(bclass[x]))
print(bmid.head(2))

# train / test
train_data, test_data = train_test_split(bmid, test_size = 0.3)
print(train_data.shape)  # (14000, 4)
print(test_data.shape)   # (6000, 4)

train_fea = np.array(train_data[['height', 'weight']])
train_ans = list(train_data['label_onehot'])
print(train_fea[0])  # [0.945 0.67 ]
print(train_ans[0])  # [0 1 0]
test_fea = np.array(test_data[['height', 'weight']])
test_ans = list(test_data['label_onehot'])

# softmax
x = tf.placeholder(tf.float32,[None, 2])
y = tf.placeholder(tf.float32,[None, 3])
w = tf.Variable(tf.zeros([2, 3]))
b = tf.Variable(tf.zeros([3]))

logits = tf.matmul(x, w) + b
hypo = tf.nn.relu(logits)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=0.1).minimize(cost)

predict = tf.equal(tf.argmax(hypo, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(3001):
        sess.run(optimizer, feed_dict={x:train_fea, y:train_ans})
        if step % 500 == 0:
            print(step, sess.run(cost, feed_dict={x:train_fea, y:train_ans}))

    acc_train = sess.run(accuracy, feed_dict={x:train_fea, y:train_ans})
    print('학습 자료로 정확도 : ', acc_train)
    
    acc_test = sess.run(accuracy, feed_dict={x:test_fea, y:test_ans})
    print('검정 자료로 정확도 : ', acc_test)

    # 새로운 데이터로 분류
    new_data = pd.DataFrame({'height':[140,170, 190], 'weight':[60, 60, 60]})
    print(new_data)
    new_data['height'] = new_data['height'] / 200
    new_data['weight'] = new_data['weight'] / 100
    result = sess.run(hypo, feed_dict={x:new_data})

    print(sess.run(tf.argmax(result, 1)))











