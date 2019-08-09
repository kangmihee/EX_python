from django.shortcuts import render
from mysangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import *

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def ListFunc(request):
    """
    sql = "select * from sangdata"
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    """
    """  페이지 나누기 기능 X
    datas = Sangdata.objects.all()  # Django가 제공하는 메소드 사용 : ORM
    return render(request, 'list.html', {'sangpums':datas})
    """
    # paging 처리
    datas = Sangdata.objects.all().order_by('-code')
    
    for d in datas:
        print('-------------', d.code, ' ', d.sang)
    
    paginator = Paginator(datas, 3)
    
    try:
        page = request.GET.get('page')
    except:
        page = 1
        
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    #return render(request, 'list2.html', {'sangpums':data})
    allPage = range(paginator.num_pages + 1)
    return render(request, 'list2.html', {'sangpums':data, 'allPage':allPage})
    
def InsertFunc(request):
    return render(request, 'insert.html')

def InsertokFunc(request):
    if request.method == 'POST':
        Sangdata(
            code = request.POST.get('code'),
            sang = request.POST.get('sang'),
            su = request.POST.get('su'),
            dan = request.POST.get('dan'),
        ).save()
    return HttpResponseRedirect('/sangpum/list/')

def UpdateFunc(request):
    data = Sangdata.objects.get(code=request.GET.get('code'))
    #print(data)
    return render(request, 'update.html', {'sang_one':data})

def UpdateokFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST.get('code'))
        #print(upRec)
        upRec.code = request.POST.get('code')
        upRec.sang = request.POST.get('sang')
        upRec.su = request.POST.get('su')
        upRec.dan = request.POST.get('dan')
        upRec.save()
    return HttpResponseRedirect('/sangpum/list/')

def DeleteFunc(request):
    delRec = Sangdata.objects.get(code=request.GET.get('code'))
    delRec.delete()
    return HttpResponseRedirect('/sangpum/list/')








