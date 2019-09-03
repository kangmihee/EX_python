# MNIST Clustering

import numpy as np
import tensorflow as tf
from tensorflow.contrib.factorization import KMeans
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('./tmp/data/', one_hot = True)

full_data_x = mnist.train.images
print(full_data_x.shape)  # (55000, 784)

num_steps = 200
batch_size= 1000
k=50
num_classes = 10   # 출력 레이블 수
num_features = 784 # 입력 feature 수

x = tf.placeholder(tf.float32, shape=[None, num_features])
y = tf.placeholder(tf.float32, shape=[None, num_classes])

kmodel = KMeans(inputs=x, num_clusters=k, distance_metric='cosine', use_mini_batch=True)
training_graph = kmodel.training_graph()

(all_scores, cluster_idx, scores, 
    cluster_centers_initialized, init_op, train_op)=training_graph
print('cluster_idx : ',cluster_idx)
print('cluster_idx[0] : ',cluster_idx[0])
cluster_idx = cluster_idx[0]
print('cluster_idx : ',cluster_idx)
avg_distance = tf.reduce_mean(scores)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
sess.run(init_op, feed_dict={x:full_data_x})

# training
for i in range(1, num_steps + 1):
    _,d,idx = sess.run([train_op, avg_distance, cluster_idx], feed_dict={x:full_data_x})
    if i % 10 == 0:
        print('step %i, avg distance:%f'%(i, d))

counts = np.zeros(shape=(k, num_classes))
for i in range(len(idx)):
    counts[idx[i]] += mnist.train.labels[i]

print(counts)  # [[9.900e+02 0.000e+00 9.000e+00 ...

# centroid에 가장 빈번한 레이블 지정
labels_map = [np.argmax(c) for c in counts]
labels_map = tf.convert_to_tensor(labels_map)

cluster_label = tf.nn.embedding_lookup(labels_map, cluster_idx)
#print(cluster_label)  # 모델에 의해 예측된 값

# 정확도
corr_pred = tf.equal(cluster_label, tf.cast(tf.argmax(y, 1), tf.int32))
accuracy = tf.reduce_mean(tf.cast(corr_pred, tf.float32))

test_x, test_y = mnist.test.images, mnist.test.labels
print('분류정확도 : ', sess.run(accuracy, feed_dict={x:test_x, y:test_y}))






    











