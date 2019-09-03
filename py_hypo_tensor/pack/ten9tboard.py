import tensorflow as tf

import numpy as np
from tqdm import tqdm     # 상태바 출력

x_data = np.array([[0, 0],[0, 1],[1, 0],[1, 1]], dtype=np.float32)
y_data = np.array([[0],[0],[0],[1]], dtype=np.float32)

X = tf.placeholder(tf.float32, [None, 2], name='x-input')
Y = tf.placeholder(tf.float32, [None, 1], name='y-input')

with tf.name_scope("layer") as scope:    
    W = tf.Variable(tf.random_normal([2, 1]), name='weight')
    b = tf.Variable(tf.random_normal([1]), name='bias')

    hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

    #histogram으로 보고 싶은 변수는 tf.summary.histogram으로 변수를 잡아 준다.
    w_hist = tf.summary.histogram("weight", W)
    b_hist = tf.summary.histogram("bias", b)
    hypothesis_hist = tf.summary.histogram("hypothesis", hypothesis)


with tf.name_scope("cost") as scope:
    cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
    #scalar로 cost를 보고 싶다면 tf.summary.scalar로 잡으면 된다. 
    cost_summ = tf.summary.scalar("cost", cost)

with tf.name_scope("train") as scope:
    train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

    
# Accuracy computation
# True if hypothesis > 0.5 else False
# predicted와 accuracy를 얻고, accuracy만 scalar로 보고 싶어 tf.summary.scalar로 잡아 주었다.

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)

accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))
accuracy_summ = tf.summary.scalar("accuracy", accuracy)

with tf.Session() as sess:
    merged_summary = tf.summary.merge_all()
    writer = tf.summary.FileWriter("./goodjob")   # tensorboard --logdir=./logs
    writer.add_graph(sess.graph)  # Save the graph

    tf.global_variables_initializer().run()

    for step in tqdm(range(10001)):
        summary, _ = sess.run([merged_summary, train], feed_dict={X: x_data, Y: y_data})
        writer.add_summary(summary, global_step=step)

    # Accuracy report
    h, p, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\np\Predict: ", p, "\nAccuracy: ", a)

# 그래프를 실행하는 부분에서는 tf.summary.merge_all()명령으로 변수를 잡아서 sess.run으로 train을 돌릴 때 같이 돌려준다. 

# tf.summary.FileWriter를 이용해서 log를 기록할 폴더를 지정해 주면 된다. 
