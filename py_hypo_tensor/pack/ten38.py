#Boston dataset으로 주택가격 예측(regression)
from keras.datasets import boston_housing
import numpy as np
from keras import models
from keras import layers

# data = boston_housing.load_data()
# print(data)
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()
print(x_train[:3], x_train.shape)  # (404, 13)
print(y_train[:3], y_train.shape)  # (404,)

# 표준화
mean = x_train.mean(axis = 0)
x_train -= mean
std = x_train.std(axis = 0)
x_train /= std
print(x_train[:3])

x_test -= mean
x_test /= std

# keras 모델 구성 후 처리 : overfitting을 피하기 위해 k-fold cross validation을 수행 가능
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(x_train.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model

# 모델 학습 및 검정
k = 4
num_val_samples = len(x_train) // k
num_epochs = 100
all_scores = []
all_mae_historis = []  # 전체 평균절대에러를 기억

for i in range(k):
    print('processing fold : ', i)
    val_data = x_train[i * num_val_samples:(i+1) * num_val_samples]
    val_target = y_train[i * num_val_samples:(i+1) * num_val_samples]
    
    # 훈련 데이터 분리
    partial_train_data = np.concatenate([x_train[:i*num_val_samples],
                                         x_train[(i+1) * num_val_samples:]], axis=0)
    partial_train_target = np.concatenate([y_train[:i*num_val_samples],
                                         y_train[(i+1) * num_val_samples:]], axis=0)

#print(partial_train_data[1])
model = build_model()

history = model.fit(partial_train_data, partial_train_target, 
                    validation_data=(val_data, val_target), \
                    epochs=num_epochs, batch_size = 1, verbose=0)
mae_historis = history.history['val_mean_absolute_error']  # 예측값과 실제값의 차이를 알기 위함
all_mae_historis.append(mae_historis)

val_mse, val_mae =  model.evaluate(val_data, val_target, verbose=1)
all_scores.append(val_mae)
print('val_mse : ', val_mse)
print('all_scores : ', all_scores)

# 매 epoch 마다 k번 검증한 값의 평균
average_mae_history = [np.mean([x[i] for x in all_mae_historis]) for i in range(num_epochs)]
print('average_mae_history:', average_mae_history)

import matplotlib.pyplot as plt
plt.plot(range(1, len(average_mae_history) + 1), average_mae_history, 'r')
plt.xlabel('epochs')
plt.ylabel('validation mae')
plt.legend()
plt.show()

# 모델에 의한 예측값 얻기
#print(model.predict(x_test))
print('예측값:', np.squeeze(model.predict(x_test)))
print('실제값:', y_test)


