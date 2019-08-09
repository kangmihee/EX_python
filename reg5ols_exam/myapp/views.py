from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from myapp.models import Jikwon, Gogek
from pandas import DataFrame
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import scipy.stats as stats
import statsmodels.api as sm
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import statsmodels.formula.api as smf


# Create your views here.

# 회귀분석 문제 3) 
# 원격 DB의 jikwon 테이블에서 근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성하시오.
# 장고로 작성한 웹에서 근무년수를 입력하면 예상연봉이 나올 수 있도록 프로그래밍 하시오.

def Main(request):
    return render(request, 'main.html')

def InsertFunc(request):
    return render(request, 'insert.html')

# def ListFunc(request):
#     if request.method == 'POST':
#         try:
#             year = request.POST.get('year')
#             now = datetime.now()
#             print(year)
#             print(now.year)
#             
#             datas = Jikwon.objects.all().values()                       
#             df = DataFrame.from_records(datas,columns=['jikwon_pay','jikwon_ibsail'])
#             print(df)
#             
#             t = pd._tslib.Timestamp.now()
#             df['jikwon_ibsail_year'] = df['jikwon_ibsail'].apply(lambda x:x.strftime('%Y'))
#             
#             df.jikwon_ibsail_year = df.jikwon_ibsail_year.astype(int)            
#             print(df['jikwon_ibsail_year'])  
#             
#             df.loc[df.jikwon_ibsail_year, 'jikwon_ibsail_year'] = df.jikwon_ibsail_year - now.year
#             print(df['jikwon_ibsail_year']) 
#             
#         except Exception as e:
#             print('Insert err : ' + str(e))
#             
#     return render(request, 'list.html')

def ListFunc(request):
    day = request.POST.get('year')
    day = float(day)
    datas = Jikwon.objects.all()
    pd_data = pd.DataFrame(list(datas.values()))  
    
    pd_data['jikwon_sustain']=[(date.today() - x).days for x in pd_data['jikwon_ibsail']]
    year_pay = smf.ols(formula="jikwon_pay ~ jikwon_sustain", data=pd_data).fit()
    print(year_pay.summary())
    
    print('근무년수를 입력한 예상연봉 :', 1.5533 * day*365 + 1987.8949)   
    result = 1.5533 * day*365 + 1987.8949
       
       
    #---------------------------------------    
    pd_data['jikwon_ibsail_year'] = pd_data['jikwon_ibsail'].apply(lambda x:x.strftime('%Y'))   
    pd_data.jikwon_ibsail_year = pd_data.jikwon_ibsail_year.astype(int)

    pd_data['jikwon_ibsail_year'] = date.today().year - pd_data['jikwon_ibsail_year'] 
    year_pay2 = smf.ols(formula="jikwon_pay ~ jikwon_ibsail_year", data=pd_data).fit()
    print(year_pay2.summary())
    
    print('근무년수를 입력한 예상연봉 :', 1983.8832 * day + 592.1637)   
    result2 = 1983.8832 * day + 592.1637
    
    return render(request, 'list.html', {'result':result, 'day':day, 'result2':result2})



