# csv 문서 읽기
import tensorflow as tf
import pandas as pd
import numpy as np

# python 고유 방법
data = []

df = pd.DataFrame(columns=("이름","국어","영어","수학"))

with open('../testdata/student.csv', encoding='utf-8') as fr:
    next(fr)  # skip header
    for line in fr:
        irum,kor,eng,mat = line.strip().split(",")
        #print(irum,kor,eng,mat)
        values = [irum,kor,eng,mat]
        data.append(values)
        df.loc[len(df)] = values
        
print(df[:3])
data_arr = np.array(data)
print(data_arr.shape)  # (20, 4)

data_tf = tf.convert_to_tensor(data_arr[:, 1:4], dtype=tf.float32)
print(data_tf)
tfdata = tf.constant(data_arr[:, 1:4], dtype=tf.float32)
print(tfdata)
sess = tf.Session()
print(sess.run(data_tf), type(data_tf))
print()
print(sess.run(tfdata), type(tfdata))
sess.close()

print('tensorflow로 csv 읽기 ---------')
fn = tf.io.read_file('../testdata/student.csv')
print(fn)
data2 = []

with tf.Session() as sess:
    #print(sess.run(fn))
    line = sess.run(fn)
    sl = str(line.decode(encoding='utf-8')).strip().split(chr(10))
    print(sl)
    for ss in sl:
        irum,kor,eng,mat = ss.strip().split(",")
        values = [irum,kor,eng,mat]
        #print(values)
        data2.append(values)

data_arr2 = np.array(data2)
tfdata2 = tf.constant(data_arr2[1:, 1:4], dtype=tf.float32)
print(tfdata2)

with tf.Session() as sess:
    print(sess.run(tfdata2))
    print(tfdata2.eval().shape)  # (20, 3)
    


 



