# cost 값을 최소화하는 수식을 이용해 최적의 모델을 작성하기 위한 W(기울기)값 찾기
import tensorflow as tf
import matplotlib.pyplot as plt

x = [1.,2.,3.]  # feature
y = [1.,2.,3.]  # label

w = tf.placeholder(tf.float32)
b = 0

# hypothesis = w * x + b
# cost = tf.reduce_sum(tf.pow(hypothesis - y, 2)) / len(x) # 비용함수 구하기
hypothesis = tf.multiply(w, x) + b
cost = tf.reduce_mean(tf.square(hypothesis - y))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
w_val = []
cost_val = []

for i in range(-30, 50):
    feed_w = i * 0.1  # learning rate(학습률)
    #print(feed_w)
    cur_cost, cur_w = sess.run([cost, w], feed_dict={w:feed_w})
    w_val.append(cur_w)  # 시각화에서 사용할 예정
    cost_val.append(cur_cost)
    print(str(i) + ' ' + 'cost:' + str(cur_cost) + ' w:' + str(cur_w))

#plt.scatter(w_val, cost_val)
plt.plot(w_val, cost_val)
plt.xlabel('w')
plt.ylabel('cost')
plt.show()






