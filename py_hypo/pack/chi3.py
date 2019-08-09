# 이원카이제곱 - 교차분할표 이용
# : 두 개 이상의 변인(집단 또는 범주)을 대상으로 검정을 수행한다.
# 분석대상의 집단 수에 의해서 독립성 검정과 동질성 검정으로 나뉜다.
# 독립성(관련성) 검정
# - 동일 집단의 두 변인(학력수준과 대학진학 여부)을 대상으로 관련성이 있는가 없는가?
# - 독립성 검정은 두 변수 사이의 연관성을 검정한다.

# 실습 : 교육수준과 흡연율 간의 관련성 분석 : smoke.csv'

import pandas as pd
import scipy.stats as stats

# 귀무 : 교육수준과 흡연율간에 관련이 없다. (연관성없음, 독립이다.)
# 대립 : 교육수준과 흡연율간에 관련이 있다. (연관성있음, 독립아니다.)

data = pd.read_csv("../testdata/smoke.csv")
print('\nhead:\n',data.head(3))
print('\ntail:\n',data.tail(3))
print('\neducation : ',data['education'].unique())
print('smoking : ',data['smoking'].unique())

# 이원카이제곱의 경우에는 교차표 작성
#ctab = pd.crosstab(index=data['education'], columns=data['smoking'])
ctab = pd.crosstab(index=data['education'], columns=data['smoking']) # 비율보기
ctab.index = ['대졸','고졸','중졸']
ctab.columns = ['과흡연','보통','비흡연']
print('\n교차표 :\n',ctab)

chi_data = [ctab.loc['대졸'], ctab.loc['고졸'], ctab.loc['중졸']]
print('\n',chi_data)

chi2, p, ddof, expected = stats.chi2_contingency(chi_data)
msg = "chi2 : {}, p-value : {} , df : {}"
print('\n',msg.format(chi2, p, ddof))
# p-value : 0.0008 < 0.05 이기 때문에 귀무가설 기각, 대립가설 채택

print('\n예측값:')
print(expected)







