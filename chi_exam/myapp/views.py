from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from myapp.models import Survey
from pandas import DataFrame
import pandas as pd
import scipy.stats as stats

# Create your views here.

def Main(request):
    return render(request, 'main.html')

def InsertFunc(request):
    return render(request, 'survey.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        try:
            datas = Survey.objects.all()
            if datas.count() != 0:
                rnum = Survey.objects.latest('rnum').rnum + 1              
            Survey(
                gender = request.POST.get('gender'),
                age = request.POST.get('age'),
                co_survey = request.POST.get('co_survey')
            ).save() 
        except Exception as e:
            print('Insert err : ' + str(e))
            
    return HttpResponseRedirect('/myapp/list')

def ListFunc(request):
    data = Survey.objects.all().values()
    df = DataFrame.from_records(data, 
                                columns=['rnum','gender','age','co_survey'])
    ctab2 = pd.crosstab(index=df['gender'], columns=df['co_survey'])
    chi2, p, ddof, expected = stats.chi2_contingency(ctab2)
    msg = "{} "
    datas = msg.format(p)
    return render(request, 'list.html',{'ctab2':ctab2.to_html(), 'p': datas})
