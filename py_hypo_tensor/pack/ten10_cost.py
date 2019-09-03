# 모델의 정확도에 따라 비용함수 값 확인
import math

# 선형회귀모델은 이미 작성된 상태라 가정
#pred = [11,5,5,4,5]  # 모델에 의해 예측값
pred = [10,8,2,1,11]  # 모델에 의해 예측값

real = [10,9,3,2,11] # 실제값

cost = 0
for i in range(5):
    cost += math.pow(pred[i] - real[i], 2)
    print(cost)
    
print(cost / 5)  # 비용1 : 12.2, 비용2 : 0.6

