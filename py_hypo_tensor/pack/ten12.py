# 경사하강법
import tensorflow as tf
import matplotlib.pyplot as plt

x_data = [1.,2.,3.]  # feature
y_data = [1.,2.,3.]  # label

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

tf.random.set_random_seed(12)

w = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.random_normal([1]))

hypothesis = tf.multiply(w, x) + b
cost = tf.reduce_mean(tf.square(hypothesis - y))

# 경사하강법(cost function 최소화 알고리즘 중 하나)
# learn_rate = 0.001 # 학습 이동거리
# decent = w - learn_rate * cost
# train = w.assign(decent)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
w_val = []
cost_val = []

for i in range(101):
    _, cur_cost, cur_w, cur_b = sess.run([train, cost, w, b], {x:x_data, y:y_data})
    w_val.append(cur_w)
    cost_val.append(cur_cost)
    if i % 10 == 0:
        print(str(i) + ' cost:' + str(cur_cost) + ' w:' + str(cur_w) + ' b:' + str(cur_b))

plt.plot(w_val, cost_val)
plt.xlabel('w')
plt.ylabel('cost')
plt.show()

print('예측값 얻기')
print(sess.run(hypothesis, feed_dict={x:[5]}))
print(sess.run(hypothesis, feed_dict={x:[2.5, 3.3]}))









        

