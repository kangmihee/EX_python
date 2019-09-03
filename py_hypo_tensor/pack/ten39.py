# 자동차 연비 예측
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

data_path = keras.utils.get_file("auto-mpg.data", 
                    "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")

column_names = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin']
raw_dataset = pd.read_csv(data_path, names=column_names, \
                          na_values="?", comment="\t", sep=" ", skipinitialspace=True)
print(raw_dataset.head(2))

dataset = raw_dataset.copy()

print(dataset.isna().sum())
dataset = dataset.dropna()
print(dataset.isna().sum())

origin = dataset.pop('origin')
#print(origin)
dataset['usa'] = (origin == 1) * 1.0
dataset['europe'] = (origin == 2) * 1.0
dataset['japan'] = (origin == 3) * 1.0

print(dataset.head(2))

# train / test
train_dataset = dataset.sample(frac=0.8, random_state = 0)
test_dataset = dataset.drop(train_dataset.index)
print(len(train_dataset))  # 318
print(len(test_dataset))   # 80

# sns.pairplot(train_dataset[['mpg','cylinders','horsepower','weight']], diag_kind='kde')
# plt.show()

train_stats = train_dataset.describe()
#print(train_stats)
train_stats.pop('mpg')
train_stats = train_stats.transpose()
print(train_stats)

# label : mpg
train_labels = train_dataset.pop('mpg')
test_labels = test_dataset.pop('mpg')
print(train_labels[:2])
print(test_labels[:2])

# 데이터 표준화
def st_func(x):
    return (x - train_stats['mean']) / train_stats['std']

#print(st_func(10))
st_train_data = st_func(train_dataset)
st_test_data = st_func(test_dataset)
#print(st_train_data[:2])

# keras 모델을 사용
def build_model():
    model = keras.Sequential([
        layers.Dense(64, activation=tf.nn.relu, input_shape=[9]),
        layers.Dense(64, activation=tf.nn.relu),
        layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(optimizer=optimizer, loss='mean_squared_error',
                metrics=['mean_absolute_error', 'mean_squared_error'])

    return model

model = build_model()
#print(model.summary())

# 일단은 train data에서 3개를 추출해서 predict을 해보기
example_batch = st_train_data[:3]
example_result = model.predict(example_batch)
print(example_result)

epochs = 1000

history = model.fit(st_train_data, train_labels, 
                    epochs=epochs, validation_split=0.2, verbose=1)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
print(hist.tail(3))

import matplotlib.pyplot as plt

def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    plt.figure(figsize=(8,12))
    plt.subplot(2,1,1)
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [MPG]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'],label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'],label = 'Val Error')
    plt.ylim([0,5])
    plt.legend()
    plt.subplot(2,1,2)
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [$MPG^2$]')
    plt.plot(hist['epoch'], hist['mean_squared_error'],label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'],label = 'Val Error')
    plt.ylim([0,20])
    plt.legend()
    plt.show()

plot_history(history)

print('***' * 20)
# 학습 조기 종료하기
model = build_model()
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(st_train_data, train_labels, 
                    epochs=epochs, validation_split=0.2, verbose=1,
                    callbacks=[early_stop])
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
print(hist.tail(3))

plot_history(history)

loss, mae, mse = model.evaluate(st_test_data, test_labels)
print('loss:', loss, '  mae:', mae, '   mse:', mse)

print()
print(st_test_data[:2])
test_prediction = model.predict(st_test_data).flatten()
print('test_prediction : ', test_prediction)

plt.scatter(test_labels, test_prediction)
plt.xlabel('true value[mpg]')
plt.ylabel('pred value[mpg]')
plt.axis('equal')
plt.axis('square')
plt.xlim([0, plt.xlim()[1]])
plt.ylim([0, plt.ylim()[1]])
plt.plot([-100, 100],[-100, 100])
plt.show()

# 오차 분포 시각화
err = test_prediction - test_labels
plt.hist(err, bins=25)
plt.xlabel('pred err[mpg]')
plt.ylabel('count')
plt.show()













