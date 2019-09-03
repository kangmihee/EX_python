# DNNClassifier : layer 추가가 편리
import tensorflow as tf
import numpy as np

def start():
    training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
            filename='iris_training.csv',
            target_dtype=np.int,
            features_dtype=np.float32)
    
    #print(training_set.data, ' ', training_set.data.shape) # [[6.4 2.8 5.6 2.2]... # (120, 4)
    #print(training_set.target)  # [2 1 2 0 ...
    
    test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
            filename='iris_test.csv',
            target_dtype=np.int,
            features_dtype=np.float32)
    #print(test_set.data, ' ', test_set.data.shape)  # (30, 4)
    
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]
    
    classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                            hidden_units = [10, 20, 10],
                            n_classes = 3,
                            model_dir="./kbs/iris_model")
    classifier.fit(x=training_set.data, y=training_set.target, steps=2000)
    accuracy_score = classifier.evaluate(x=test_set.data, y=test_set.target)
    print(accuracy_score)
    print(accuracy_score['loss'])
    print(accuracy_score['accuracy'])
    print()
    accuracy_score = classifier.evaluate(x=test_set.data, y=test_set.target)['accuracy']
    print('정확도 : {0:f}'.format(accuracy_score))
    
    # 예측 : 
    new_samples = np.array([[3.3,4.4,5.5,6.6], [8.8,7.7,2.2,1.1]], dtype=float)
    y = list(classifier.predict(new_samples, as_iterable=True))
    print('예측 결과 : {}'.format(str(y)))
    

if __name__ == '__main__':
    #tf.logging.set_verbosity(tf.logging.WARN)
    #tf.logging.set_verbosity(tf.logging.INFO)
    tf.logging.set_verbosity(tf.logging.DEBUG)
    start()




