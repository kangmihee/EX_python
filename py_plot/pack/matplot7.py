'''
Created on 2019. 7. 30.

@author: acorn
'''
# pandas의 plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(0)

df = pd.DataFrame(np.random.randn(10, 3),
                  index=pd.date_range('1/1/2009', periods=10),
                  columns=['a','b','c'])
print(df)
# df.plot()
# df.plot(kind='bar') # bar plot 형태로 출력됨.
df.plot(kind='box') # box plot 형태로 출력.

plt.xlabel('time')
plt.ylabel('data')
plt.show()

df[:5].plot.bar(rot=0)
plt.show()