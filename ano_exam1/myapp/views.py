from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from myapp.models import Starbucks
from pandas import DataFrame
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import scipy.stats as stats
import statsmodels.api as sm
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt

# Create your views here.

def Main(request):
    return render(request, 'main.html')

def InsertFunc(request):
    return render(request, 'survey.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        try:
            datas = Starbucks.objects.all()
            if datas.count() != 0:
                id = Starbucks.objects.latest('id').id + 1              
            Starbucks(
                job = request.POST.get('job'),
                gender = request.POST.get('gender'),
                survey = request.POST.get('survey')
            ).save() 
        except Exception as e:
            print('Insert err : ' + str(e))
            
    return HttpResponseRedirect('/myapp/list')

def ListFunc(request):
    data = Starbucks.objects.all().values()
    df = DataFrame.from_records(data, 
                                columns=['id','job','gender','survey'])
    ctab2 = pd.crosstab(index=df['gender'], columns=df['survey'])
    chi2, p, ddof, expected = stats.chi2_contingency(ctab2)
    msg = "{} "
    datas = msg.format(p)
    print(datas)
    
    if p > 0.05:
        ans = "이상"
        dif = "차이가 없다(귀무가설채택)"
    else:
        ans = "미만"
        dif = "차이가 있다(대립가설채택)"
    
    df2 = DataFrame.from_records(data, columns=['job','survey'])
     
    df.loc[df.survey=='매우불만족', 'survey'] = '1'
    df.loc[df.survey=='불만족', 'survey'] = '2'
    df.loc[df.survey=='보통', 'survey'] = '3'
    df.loc[df.survey=='만족', 'survey'] = '4'
    df.loc[df.survey=='매우만족', 'survey'] = '5'
    
    gr1 = df.survey[df.job == '화이트칼라']
    gr2 = df.survey[df.job == '블루칼라']
    gr3 = df.survey[df.job == '학생']
    gr4 = df.survey[df.job == '기타']
    
    f_statistic, p_val = stats.f_oneway(gr1,gr2,gr3,gr4)
    
    if p_val > 0.05:
        ans2 = "이상"
        dif2 = "차이가 없다(귀무가설채택)"
    else:
        ans2 = "미만"
        dif2 = "차이가 있다(대립가설채택)"
        
    #각 그룹간 밀집도를 시각화   
    df.survey = df.survey.astype(int) 
    plt.rc('font', family = 'malgun gothic')
    
    fig = plt.gcf()
    gensur = df['survey'].groupby(df['gender'])
    gensur_result = gensur.agg('mean')
    gensur_result.plot(kind = 'bar')

    fig.savefig('ano_exam1/myapp/static/images/bar.png')
    plt.clf()
    
    jobsur = df['survey'].groupby(df['job'])
    jobsur_result = jobsur.agg('mean')
    jobsur_result.plot.pie(subplots = True)
    
    fig.savefig('ano_exam1/myapp/static/images/pie.png')
    plt.clf()
             
    return render(request, 'list.html',
                  {'ctab2':ctab2.to_html(), 'p':datas, 'ans':ans, 'dif':dif,
                   'p_val':p_val, 'ans2':ans, 'dif2':dif})
