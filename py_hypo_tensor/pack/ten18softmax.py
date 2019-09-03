# softmax 알고리즘 함수로 구현
import numpy as np

def softmax_func(a):
    c = np.max(a)
    exp_a = np.exp(a - c)  # 지수함수
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a

a = np.array([0.3, 2.7, 4.0])
#a = np.array([9003, 1000, 1200])
print(softmax_func(a))
print(sum(softmax_func(a)))
