# clustering
import tensorflow as tf
from tensorflow.contrib.factorization import KMeans

k = 3
# num_feature = 1
# arr = [[1],[2],[2],[4],[2]]

num_feature = 2
arr = [[1,2],[2,3],[3,4],[5,5],[5,10],[15,5]]

x = tf.placeholder(tf.float32, shape=[None, num_feature])
kmodel = KMeans(inputs=x, num_clusters=k, \
                distance_metric='squared_euclidean', use_mini_batch=True)
#print(kmodel)
(all_scores, cluster_idx, scores, cluster_centers_initialized, init_op, train_op)=\
    kmodel.training_graph()
cluster_idx = cluster_idx[0]
avg_distance = tf.reduce_mean(scores)  # 요소값 거리의 평균

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(init_op, feed_dict = {x:arr}))
print(sess.run(train_op, feed_dict = {x:arr}))
print(sess.run(all_scores, feed_dict = {x:arr}))
print(sess.run(cluster_idx, feed_dict = {x:arr}))
print(sess.run(scores, feed_dict = {x:arr}))
print(sess.run(cluster_centers_initialized, feed_dict = {x:arr}))

# 학습
for i in range(1, 100):
    _,d,idx = sess.run([train_op, avg_distance, cluster_idx], feed_dict = {x:arr})
    #print(i, idx)
    if i % 10 == 0:
        print(i, ' ', 'distance :', d)

print(d, idx)

print()
for i in range(0, k):
    result = []
    for j in range(0, idx.size, 1):
        if idx[j] == i:
            result.append(arr[j])
    print(i, '에 속한 데이터:', result)



