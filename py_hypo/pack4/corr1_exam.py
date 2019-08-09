# 상관관계 문제)
# 유형1) https://github.com/pykwon/python 에 있는 Advertising.csv 파일을 읽어 
# tv,radio,newspaper 간의 상관관계를 파악하시오.
# 이들의 관계를 heatmap 그래프로 표현하시오. 
import pandas as pd
import numpy as np
from matplotlib.pylab import plt


data = pd.read_csv('../testdata/Advertising.csv')
print('\n\n',data.head(3))
print('\n',data.describe())

print('\n-------상관계수 출력 -------')
print('\ncorr:\n',data.corr()) 

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
