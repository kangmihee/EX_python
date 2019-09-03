# 모든 이진 분류 모형은 판별 평면으로부터의 거리에 해당하는 판별 함수를 가지며 판별 함수 값이 음수이면 0인 클래스, 양수이면 1인 클래스에 해당한다고 판별한다. 즉 0 이 클래스 판별 기준값이 된다. ROC 커브는 이 클래스 판별 기준값이 달라진다면 판별 결과가 어떻게 달라지는지는 표현한 것이다.
# Scikit-Learn 의 Classification 클래스는 판별 함수 값을 계산하는 decision_function 메서드를 제공한다. ROC 커브는 이 판별 함수 값을 이용하여 다음과 같이 작성한다.
# 모든 표본 데이터에 대해 판별 함수 값을 계산한다.
#   계산된 판별 함수 값을 정렬한다.
#   만약 0이 아닌 가장 작은 판별 함수값을 클래스 구분 기준값으로 하면 모든 표본은 클래스 1(Positive)이 된다. 
#   이 때의 Fall-out과 Recall을 계산하면 Recall과 Fall-out이 모두 1이된다.
#   두번째로 작은 판별 함수값을 클래스 구분 기준값으로 하면 판별 함수 값이 가장 작은 표본 1개를 제외하고 나머지 표본은 클래스 1(Positive)이 된다. 마찬가지로 이 때의 Fall-out과 Recall을 계산하여 기록한다.
#   가장 큰 판별 함수값이 클래스 구분 기준값이 될 때까지 이를 반복한다. 
#   이 때는 모든 표본이 클래스 0(Negative)으로 판별되며 Recall과 Fall-out이 모두 0이 된다.
# 일반적으로 클래스 판별 기준이 변화함에 따라 Recall과 Fall-out은 같이 증가하거나 감소한다. 
# Fall-out보다 Recall이 더 빠르게 증가하는 모형은 좋은 모형으로 생각할 수 있다.

#https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html

import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp

# Import some data to play with
iris = datasets.load_iris()
x_data = iris.data
y_data = iris.target

# Binarize the output
y_data = label_binarize(y_data, classes=[0, 1, 2])
n_classes = y_data.shape[1]

# Add noisy features to make the problem harder
random_state = np.random.RandomState(0)
n_samples, n_features = x_data.shape
x_data = np.c_[x_data, random_state.randn(n_samples, 200 * n_features)]
print(x_data.shape) #(150, 804)
print(y_data.shape) #(150, 3)

# shuffle and split training and test sets
X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=.5, random_state=0)

####################

# Learn to predict each class against the other
model = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True, random_state=random_state))

####################

model.fit(X_train, y_train)

# Compute ROC curve and ROC area for each class
y_score = model.decision_function(X_test)
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    #roc_auc[i] = auc(fpr[i], tpr[i])
    roc_auc[i] = roc_auc_score(y_test[:, i], y_score[:, i])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())

#roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
roc_auc["micro"] = roc_auc_score(y_test.ravel(), y_score.ravel())

print('-----' * 5)

##print(y_test)
##print(y_test.ravel())
##plt.figure()

plt.plot(fpr[2], tpr[2],
         color='darkorange', label='ROC curve (area = {:0.2f})'.format(roc_auc[2]))
plt.plot([0, 1], [0, 1],
         color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()

#####################
#Plot ROC curves for the multiclass problem
# Plot all ROC curves

colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i],
             color=color, label='ROC curve of class {0} (area = {1:0.2f})'.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1],
         color='navy', linestyle='--')

# Compute macro-average ROC curve and ROC area
# First aggregate all false positive rates

all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

# Then interpolate all ROC curves at this points
mean_tpr = np.zeros_like(all_fpr)
for i in range(n_classes):
    mean_tpr += interp(all_fpr, fpr[i], tpr[i])

# Finally average it and compute AUC
mean_tpr /= n_classes
fpr["macro"] = all_fpr
tpr["macro"] = mean_tpr
roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
plt.plot(fpr["micro"], tpr["micro"],
         label='micro-average ROC curve (area = {:0.2f})'.format(roc_auc["micro"]), color='deeppink', linestyle=':')
plt.plot(fpr["macro"], tpr["macro"],
         label='macro-average ROC curve (area = {:0.2f})'.format(roc_auc["macro"]), color='navy', linestyle=':')

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Some extension of Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.show()

