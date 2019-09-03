# SVM으로 얼굴인식 예

from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from matplotlib.pyplot import xticks, yticks, xlabel
from sklearn.metrics.classification import classification_report

faces = fetch_lfw_people(min_faces_per_person=60)
print(faces)
print(faces.target_names)
print(faces.images.shape) #(1348, 62, 47)

fig, ax = plt.subplots(3, 5)
print(fig, ' ', ax)
for i, axi in enumerate(ax.flat):
    axi.imshow(faces.images[i], cmap='bone')
    axi.set(xticks=[], yticks=[], xlabel=faces.target_names[faces.target[i]])

#plt.show() # 각 이미지는 62*17 약 3000픽셀

from sklearn.svm import SVC
from sklearn.decomposition import PCA  # 약3000 픽셀중에서 이미지에 영행을 크게 주는 150 픽셀 정도의 추출해 분석 
from sklearn.pipeline import make_pipeline
m_pca = PCA(n_components=150, whiten=True, random_state=0)
m_svc = SVC(gamma='scale')
model = make_pipeline(m_pca, m_svc) # 선처리가와 분류기를 하나의 파이프라인으로 묶어서 처리

# train, test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(faces.data, faces.target, random_state=1)
#print(x_train, len(x_train)) # 1011

model.fit(x_train, y_train)
y_fit = model.predict(x_test)
#print(y_fit)  # model이 예측한 값

#plt.imshow(x_train[0].reshape(62,47), cmap='bone')
#plt.show()

# test 이미지 중 몇개에 대해 예측한 값과 시각화
for i, axi in enumerate(ax.flat):
    axi.imshow(x_test[i].reshape(62,47), cmap='bone')
    axi.set(xticks=[], yticks=[])
    axi.set_ylabel(faces.target_names[y_fit[i]].split()[-1],\
                   color='black' if y_fit[i] == y_test[i] else 'red')
plt.show()

# 모델성능확인
from sklearn.metrics import accuracy_score
mat = accuracy_score(y_test, y_fit)
print('정확도 : ', mat) # 0.795252...

from sklearn.metrics import classification_report
print('분류 결과표:\n',classification_report(y_test, y_fit, target_names=faces.target_names)) # 실제값, 예측값


from sklearn.metrics import confusion_matrix
mat = confusion_matrix(y_test, y_fit)
print('mat : ', mat)

# 오차 행렬 시각화
import  seaborn as sns
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,\
            xticklabels = faces.target_names,
            yticklabels = faces.target_names,
            )
plt.xlabel('true value')
plt.ylabel('predict value')
plt.show()

