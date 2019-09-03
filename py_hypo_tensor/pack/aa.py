#Keras를 이용한 One-hot encoding
from keras_preprocessing.text import Tokenizer

text="우리 공부하러 갈래 언어는 자바 파이썬 자바 만세"
t = Tokenizer()
t.fit_on_texts([text])
# 입력으로 [text]가 아닌 text를 넣을 경우 한 글자 단위 인코딩이 된다. ex 갈 : 1, 래 : 2
print(t.word_index) # 각 단어에 대한 인코딩 결과 보기
#{'자바': 1, '우리': 2, '공부하러': 3, '갈래': 4, '언어는': 5, '파이썬': 6, '만세': 7}

#생성된 단어 집합(Vocabulary)에 있는 단어들로만 구성된 텍스트가 있다면, texts_to_sequences()를 통해서 인덱스의 나열로 변환가능. 
#Vocabulary의 단어들로만 구성된 서브 텍스트 text2를 가지고 확인해보겠다.
text2 = "공부하러 갈래 프로그래밍 언어는 자바 만세"
x = t.texts_to_sequences([text2])[0]
print(x)  # [3, 4, 5, 1, 7]
# 지금까지 정수 인코딩 과정을 진행함

# 이제 해당 결과를 가지고, 원-핫 인코딩을 진행한다. 
# 케라스는 정수 인코딩 된 결과를 입력으로 받아 바로 원-핫 인코딩 과정을 수행하는 to_categorical() 지원.
vocab_size = len(t.word_index) # 단어 집합의 크기. 
print('vocab_size : ', vocab_size) # 단어의 개수가 7이므로 7

from keras.utils import to_categorical
x = to_categorical(x, num_classes=vocab_size + 1) # 실제 단어 집합의 크기보다 +1로 크기를 준다.

print(x)
    # [[0. 0. 0. 1. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 1. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 1. 0. 0.]
    #  [0. 1. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 1.]]