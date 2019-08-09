# 분산의 중요성
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(0)
print(stats.norm(loc=1, scale=2).rvs(10))

centers = [1, 1.5, 2]
col ='rgb'

#############################

std = 0.1 # 분산값 0.1
data_1 = []

for i in range(3):
    data_1.append(stats.norm(centers[i], std).rvs(100))
    plt.plot(np.arange(len(data_1[i])) + i * len(data_1[0]),
             data_1[i], '*', color=col[i])
plt.show()

#############################

std = 3 # 분산값이 클수록 집단간의 의미가 없음(분산값작을수록 밀집한다)
data_1 = []

for i in range(3):
    data_1.append(stats.norm(centers[i], std).rvs(100))
    plt.plot(np.arange(len(data_1[i])) + i * len(data_1[0]),
             data_1[i], '*', color=col[i])
plt.show()    
    
#############################    
    
    
    
    