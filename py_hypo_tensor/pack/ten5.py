# Variable, constant, placeholder
import tensorflow as tf

def func1():
    imsi = tf.Variable(1)
    const = tf.constant(1)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for _ in range(3):
            print(sess.run(imsi))
            imsi = tf.add(imsi, const)  # imsi = imsi + const
           
func1()

def func2():
    imsi = tf.Variable(0)
    const = tf.constant(1)
    value = tf.add(imsi, const)
    update = tf.assign(imsi, value)  # tf.assign(value,imsi) X
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for _ in range(3):
            print(sess.run(update))

func2()

print('구구단 --------')
def gugu1(arg):
    level = tf.constant(arg)
    state = tf.Variable(1)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for _ in range(1, 10):
            dan, su = sess.run(level), sess.run(state)
            print('{}*{}={:2}'.format(dan, su, dan * su))
            state = tf.add(state, 1)
            
gugu1(3)

print()
def gugu2(arg):
    level = tf.constant(arg)
    state = tf.Variable(1)
    add = tf.add(state, 1)
    value = tf.assign(state, add)
    update = tf.multiply(level, value)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for _ in range(9):
            #dan, su, result = sess.run([level, state, update])
            result = sess.run(update)
            dan, su = level.eval(), state.eval()
            print('{}*{}={:2}'.format(dan, su, result))

gugu2(5)

print()
def gugu3(arg):
    dan = tf.placeholder(tf.int32)
    su = tf.placeholder(tf.int32)
    update = tf.multiply(dan, su)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(1, 10):
            result = sess.run(update, feed_dict={dan:arg, su:i})
            print('{}*{}={:2}'.format(arg, i, result))

gugu3(7)





