# 최소제곱해를 선형행렬 방정식으로 얻기

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3])
y = np.array([-1,0.2,0.9,2.1])

plt.plot(x,y)
plt.grid(True)
plt.show()

aa = np.vstack([x, np.ones(len(x))]).T
print(aa)

import numpy.linalg as lin

w, b = lin.lstsq(aa, y)[0] # w:기울기, b:절편
print('기울기:{}, 절편:{}'.format(w, b))

plt.plot(x,y,'o',label='Ori data', markersize=10)
plt.plot(x, w*x+b, 'r', label='Fit line')
plt.legend()
plt.show()



























