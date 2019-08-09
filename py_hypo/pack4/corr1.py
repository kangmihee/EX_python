# 확률변수간의 관계를 공분산으로 알 수 있다.
# 공분산의 한계를 해결한 것으로  상관계수(공분산을 정규화)를 사용, (-1 - 0 -1)

import pandas as pd
import numpy as np
from matplotlib.pylab import plt

df = pd.DataFrame({'id1':(1,2,3,4,5),'id2':(2,3,-1,7,9)})
# plt.scatter(df.id1, df.id2)
# plt.show()

print('cov:\n',df.cov()) # 공분산계산
print('\ncorr:\n',df.corr()) # 상관계수 알려줌

data = pd.read_csv('../testdata/drinking_water.csv')
print('\n\n',data.head(3))
print('\n',data.describe())

print('-------표준편차 출력 -------')
print(np.std(data.친밀도))
print(np.std(data.적절성))
print(np.std(data.만족도))

# plt.hist([np.std(data.친밀도), np.std(data.적절성),np.std(data.만족도)])
# plt.show()

print('\n-------공분산 출력 -------')
print(np.cov(data.친밀도, data.적절성))
print(np.cov(data.친밀도, data.만족도))
print('\ncov:\n',data.cov())


print('\n-------상관계수 출력 -------')
print(np.corrcoef(data.친밀도, data.적절성))
print('\ncorr:\n',data.corr()) 
print('\ncorr-pearson:\n',data.corr(method='pearson'))  # 변수가 등간 또는 비율척도
print('\ncorr-spearman:\n',data.corr(method='spearman')) # 변수가 서열척도
print('\ncorr-kendall:\n',data.corr(method='kendall'))   # spearman만 유사

# 상관계수를 방향성 있는 색으로 시각화 (heatmap)
import seaborn as sns
plt.rc('font', family='malgun gothic')
sns.heatmap(data.corr())
plt.show()


# hitmap에 텍스트 표시 추가사항 적용해 보기
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()













