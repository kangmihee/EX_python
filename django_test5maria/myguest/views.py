from django.shortcuts import render
from myguest.models import Guest
from datetime import datetime
from django.http.response import HttpResponseRedirect

# Create your views here.

def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    gdata = Guest.objects.all()                       # 기본 입력순서
    #gdata = Guest.objects.all().order_by('title')    # ㄱㄴㄷ 순으로 정렬(sort)
    #gdata = Guest.objects.all().order_by('-id')[0:2] # 내림차순으로 정렬, 부분적 나타냄(slicing)

    return render(request, 'list.html', {'gdata':gdata})

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertFuncOk(requset):
    if requset.method == 'POST':
        Guest(
            title = requset.POST.get('title'),
            content = requset.POST.get('content'),
            regdate = datetime.now()
        ).save()  # insert 처리
        
    return  HttpResponseRedirect('/guest')







