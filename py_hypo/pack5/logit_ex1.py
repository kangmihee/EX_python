# 로지스틱 회귀분석 : 독립(연속형), 종속(범주형) - 분류

import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

# 자동차 정보를 이용한 로지스틱 회귀 
#logit 변환(오즈비의 결과에 대해 로그를 씌워 0 ~ 1 사이의 확률값을 반환)
# 의 결과를 이분(양분, 0 or 1))

mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(3))
mtcars = mtcars.loc[:,['mpg', 'hp', 'am']]
print(mtcars.head(2))

# 연비와 마력수에 따른 변속기 분류(소동, 자동)
formula = 'am ~ hp + mpg' # 종속(am), 독립(hp, mpg)
result = smf.logit(formula = formula, data=mtcars).fit()
print(result)
print(result.summary()) # 기울기 : hp(0.0550), mpg(1.2596), 절편 : -33.6052

print('\n예측값 : \n', result.predict())
pred = result.predict(mtcars[:10])
print('\n예측값 : \n', np.around(pred))
print('\n실제값 : \n', mtcars['am'][:10])

conf_tab = result.pred_table()
print('\nconfusion matrix :\n', conf_tab)

# 정확도 확인 - 1
print('분류정확도 : ', (16+10)/len(mtcars))
print('분류정확도 : ', (conf_tab[0][0] + conf_tab[1][1])/ len(mtcars))

# 정확도 확인 - 2
from sklearn.metrics import accuracy_score
pred2 = result.predict(mtcars)
print('분류정화도 : ', accuracy_score(mtcars['am'], np.around(pred2)))

# 방법2 : glm() - R과 유사한 명형
result2 = smf.glm(formula = formula, data = mtcars, family = sm.families.Binomial()).fit()
print(result2)
print(result2.summary())

glm_pred = result2.predict(mtcars[:5])
print('\nglm_pred :\n ',np.around(glm_pred)) # 0 또는 1로 나옴

print('\n\n새로운 값으로 분류 예측-------------')
newdf = mtcars.iloc[:2]
newdf['mpg'] = [10, 30] # 예측을 위해 기존 mpg값을 새로운 값으로 수정
newdf['hp'] = [100, 120]
print(newdf)

glm_pred2 = result2.predict(newdf)
print('\nglm_pred2 :\n ',np.around(glm_pred2))
print('\nglm_pred2 :\n ',np.rint(glm_pred2))

# 새값이 있는 DataFrame 새로 작성
import pandas as pd
newdf2 = pd.DataFrame({'mpg':[10,35], 'hp':[100,125]})
print(newdf2)
glm_pred2 = result2.predict(newdf2)
print('\nglm_pred2 :\n ',np.around(glm_pred2))
print('\nglm_pred2 :\n ',np.rint(glm_pred2))









