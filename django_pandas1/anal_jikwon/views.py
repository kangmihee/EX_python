from django.shortcuts import render
from anal_jikwon.models import Jikwon
from pandas import DataFrame
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def DispFunc(request):
    datas = Jikwon.objects.all().values()
    df = DataFrame.from_records(datas, 
                                columns=['jikwon_no','jikwon_name','buser_num',
                                         'jikwon_jik','jikwon_pay','jikwon_gen']) # 원하는 칼럼만 가져오기
    # print(df)
    
    buser_group = df['jikwon_pay'].groupby(df['buser_num'])
    buser_group_detail = {'sum':buser_group.sum(), 'avg':buser_group.mean()}
    
    fig = plt.gcf()
    bu_result = buser_group.agg(['sum','mean'])
    bu_result.plot(kind='barh')
    fig.savefig('django_pandas1/anal_jikwon/static/images/chart1.png')
    
    return render(request, 'list.html', {'datas':df.to_html(), 'buser_group':buser_group_detail})