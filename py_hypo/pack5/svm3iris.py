# iris data로 Species 분류

#from sklearn.linear_model.logistic import LogisticRegression
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
#print(iris)
#print(iris.DESCR)

x = iris.data[:,[2,3]] # petal.length, petal.width
print(x[:2])
y = iris.target
print(y[:2])

# train / test로 분류 (7:3)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print(x_train.shape, ' ', x_test.shape)
print(y_train.shape, ' ', y_test.shape)

# 표준화(전체자료의 분포를 평균0, 표준편차1로 전처리)-최적화과정에서 안정성, 속도 증진, 오버플로, 언더플로를 최소화
sc = StandardScaler()
print(sc)
sc.fit(x_train)
sc.fit(x_test)
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)
print(x_train_std)

# 분류모델 생성 및 학습
#ml = svm.SVC(c=100)
ml = svm.LinearSVC() # SVC의 개량 (속도향상)

print('ml : ',ml) 
result = ml.fit(x_train_std, y_train)
print(result)

y_pred = ml.predict(x_test_std)
print('추정값 :\n', y_pred)
print('실제값 :\n', y_test)

print('추정실제값 분류 결과 : 총테스트 수 :%d, 오류수:%d'%(len(y_test), (y_test != y_pred).sum()))

# 정확도 확인 방법1
import pandas as pd
con_met = pd.crosstab(y_test, y_pred)
print('\ncrosstab:\n',con_met)
print('정확도:', (con_met[0][0] + con_met[1][1] + con_met[2][2]) / len(y_test))

# 정확도 확인 방법2
print('정확도:',accuracy_score(y_test, y_pred))

# 정확도 확인 방법3
print('정확도:',ml.score(x_test_std, y_test))



#* 붓꽃 자료에 대한 로지스틱 회귀 결과를 차트로 그리기 *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)      #그래프에서 한글깨짐 방지용
plt.rcParams['axes.unicode_minus']= False

def plot_decision_region(X, y, classifier, test_idx=None, resolution=0.02, title=''):
    markers = ('s', 'x', 'o', '^', 'v')  # 점표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])
    # decision surface 그리기

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
   
    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 
    # predict()의 안자로 입력하여 계산된 예측값을 Z로 둔다.

    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape) #Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.

    # X를 xx, yy가 축인 그래프상에 cmap을 이용해 등고선을 그림
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())  

    X_test = X[test_idx, :]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], c=cmap(idx), marker=markers[idx], label=cl)     

    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='', linewidth=1, marker='o', s=80, label='testset')

    plt.xlabel('표준화된 꽃잎 길이')
    plt.ylabel('표준화된 꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()

x_combined_std = np.vstack((x_train_std, x_test_std))
y_combined = np.hstack((y_train, y_test))
plot_decision_region(X=x_combined_std, y=y_combined, classifier=ml, 
                    test_idx=range(105, 150), title='scikit-learn제공')     



# 새로운 자료로 꽃의 종류 분류하기
# 선형회귀  ... 0 또는 1 또는 2로 결과 나옴
import numpy as np
new_data = [[5.1, 2.2],[2.1, 1.2],[4.4, 0.2]] 
sc.fit(new_data)
new_test_std = sc.transform(new_data)
print(new_test_std)
new_pred = ml.predict(new_test_std)
print('예측결과:',new_pred) # [2 0 1]


















