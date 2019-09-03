# SVM으로 XOR 분류

from sklearn import svm, metrics
from pandas import DataFrame

xor_data = [
   # p  q  re
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

xor_df = DataFrame(xor_data)
data = xor_df.iloc[:, 0:2]
label = xor_df.iloc[:, 2]
print(data) 
print(label) # 실제값

# 모델 생성 후 학습
train_model = svm.SVC()
#print(train_model)
train_model.fit(data, label)

# 예측
pred = train_model.predict(data)
print('예측결과 :',pred)

# 정확도
ac_score = metrics.accuracy_score(label, pred) # 실제값, 예측값
print('정확도 :',ac_score)

#---------------------------
data2 = DataFrame([[0,0,1,1], [0,0,1,1]])
data2 = data2.T
print(data2)
# 예측
pred2 = train_model.predict(data2)
print('예측결과2 :',pred2)
# 정확도
ac_score2 = metrics.accuracy_score(label, pred2) # 실제값, 예측값
print('정확도2 :',ac_score2)
#---------------------------

# 분류 결과표
# precision(정밀도),recall(재현율),macro(단순평균),weighted(가중평균),support(자료수)
ac_report = metrics.classification_report(label, pred2)
print('분류 결과표:\n',ac_report) 














