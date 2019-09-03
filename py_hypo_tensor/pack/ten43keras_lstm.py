# Keras + RNN(LSTM) - 기존 소설을 읽어 새로은 소설 작성
import numpy as np
import random, sys
import tensorflow as tf

f = open("개미1권.txt", 'r', encoding="utf-8")
text = f.read()
print(text)
f.close()

print('라인 수 :', len(text))
print(set(text))
chars = sorted(list(set(text)))
print(chars)
print('문자 수 :', len(chars))

print()
char_ind = dict((c, i) for i, c in enumerate(chars))
ind_char = dict((i, c) for i, c in enumerate(chars))
print(char_ind)
print(ind_char)

# 학습할 구문 수 
maxlen = 30 # 학습할 문장을 인위적으로 20개씩 끊기 
step = 3
sentences = []
next_chars = []

for i in range(0, len(text) - maxlen, step):
    #print(text[i : i+maxlen])  
    sentences.append(text[i : i+maxlen])
    next_chars.append(text[i + maxlen])

print('학습할 구문 수  : ', len(sentences))  # 483343
#print(next_chars)  # 너 새로운 경험할꺼야!!!

# text를 id벡터로 변환
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
print(x[:2], ' ', x.shape)
print(y[:2], ' ', y.shape)

print('---------------')
for i, sent in enumerate(sentences):
    for t, char in enumerate(sent):
        x[i, t, char_ind[char]] = 1
    y[i, char_ind[next_chars[i]]] = 1

print(x[:5])
print(y[:5])

# 모델 생성 후 처리
model = tf.keras.Sequential()
model.add(tf.keras.layers.LSTM(128, input_shape=(maxlen, len(chars))))
model.add(tf.keras.layers.Dense(len(chars)))
model.add(tf.keras.layers.Activation('softmax'))
optimizer = tf.keras.optimizers.RMSprop(lr=0.01)

model.compile(optimizer = optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

def sample_func(preds, variety = 1.0):  # 후보를 배열에서 빼내기
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / variety  # 로그확률벡터식 작성 (soft알고리즘)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1) # 다항식 분포로 샘플 얻기
    return np.argmax(probas)

for num in range(1, 2):
    print('----' * 20)
    print('반복 : ', num)
    model.fit(x, y, batch_size=128, epochs=1)
    start_index = random.randint(0, len(text) - maxlen - 1) # 임의의 시작 구문 선택

    for variety in [0.2, 1.0, 1.2]:  # 다양한 문장 생성 용
        print('다양성 : ', variety)
        generate = ''
        sentence = text[start_index : start_index + maxlen]
        generate += sentence
        print('임의의 시작 문장 : "' + sentence + '"') # seed
        sys.stdout.write(generate)
        
        for i in range(500):
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_ind[char]] = 1.
            
            #다음에 올 문자 예측
            preds = model.predict(x, verbose=0)[0]
            next_index = sample_func(preds, variety)
            next_char = ind_char[next_index]
            #출력
            generate += next_char
            sentence = sentence[1:] + next_char
            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()
        












