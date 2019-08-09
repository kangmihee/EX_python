from django.shortcuts import render
from myapp.models import BoardTab
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from _datetime import datetime
from django.http.response import HttpResponseRedirect

# Create your views here.

def Main(request):
    return render(request, 'main.html')

def ListFunc(request):
    #datas = BoardTab.objects.all().order_by('-id')
    datas = BoardTab.objects.all().order_by('-gnum', 'onum') # gnum : desc, onum : asc
    paginator = Paginator(datas, 10)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
        
    except EmptyPage:
        data = paginator.page(paginator.num_page)
        
    return render(request, 'board.html', {'data':data})

    
def InsertFunc(request):
    return render(request, 'insert.html')

def get_ip_address(request): # client의 ip 얻기
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def InsertokFunc(request):
    if request.method == 'POST':
        try:
            gbun = 1
            datas = BoardTab.objects.all()
            if datas.count() != 0:
                gbun = BoardTab.objects.latest('id').id + 1              
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = get_ip_address(request),
                bdate = datetime.now(),
                readcnt = 0,
                gnum = gbun,
                onum = 0,
                nested = 0,
            ).save() 
        except Exception as e:
            print('InsertokFunc err : ' + str(e))
            
    return HttpResponseRedirect('/board/list') # 추가 후 목록보기


def SearchFunc(request):
    if request.method == 'POST':
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        if s_type == 'title':
            datas = BoardTab.objects.filter(title__contains = s_value)
        elif s_type == 'name' :
            datas = BoardTab.objects.filter(name__contains = s_value)
        paginator = Paginator(datas, 5)
        page = request.GET.get('page')
        
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_page)
        
    return render(request, 'board.html', {'data':data})
 
 
def UpdateFunc(request):
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))
    except:
        print('UpdateFunc err : ')
    return render(request, 'update.html', {'data_one':data})
    

def UpdateokFunc(request):
    if request.method == 'POST':
        upRec = BoardTab.objects.get(id = request.POST.get('id'))
        if upRec.passwd == request.POST.get('up_passwd'):
            #print('성공')
            upRec.name = request.POST.get('name')
            upRec.mail = request.POST.get('mail')
            upRec.title = request.POST.get('title')
            upRec.cont = request.POST.get('cont') 
            upRec.save()          
            
        else:
            print('실패')
            return render(request, 'error.html')
        
    return HttpResponseRedirect('/board/list') # 수정 후 목록 보기
        

def DeleteFunc(request):
    try:
        data = BoardTab.objects.get(id = request.GET.get('id'))
    except:
        print('deleteFunc err : ')
    return render(request, 'deleteok.html', {'data':data})



def DeleteokFunc(request):
    if request.method == 'POST':
        delRec = BoardTab.objects.get(id = request.POST.get('id'))        
        if delRec.passwd == request.POST.get('del_passwd'):
            delRec.delete()
            return HttpResponseRedirect('/board/list')
        else:
            return render(request, 'error.html')
    return HttpResponseRedirect('/board/list')


def ContentFunc(request):
    data = BoardTab.objects.get(id = request.GET.get('id'))
    data.readcnt = data.readcnt + 1
    data.save()
    page = request.GET.get('page')
    return render(request, 'content.html', {'data_one':data, 'page':page})


# 댓글용
def ReplyFunc(request):
    try:
        data = BoardTab.objects.get(id = request.GET.get('id'))
    except:
        print('ReplyFunc err')
        
    return render(request, 'reply.html', {'data_one':data})
  

def ReplyokFunc(request):
    if request.method == 'POST':
        try:
            re_gnum = request.POST.get('gnum')
            re_onum = int(request.POST.get('onum'))
            tempRec = BoardTab.objects.get(id = request.POST.get('id'))
            old_gnum = tempRec.gnum
            old_onum = tempRec.onum
            
            if old_onum >= re_onum and old_gnum == re_gnum:
                old_onum = old_gnum + 1 # old_onum 갱신
                
            # 댓글 저장
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = get_ip_address(request),
                bdate = datetime.now(),
                readcnt = 0,
                gnum = re_gnum,
                onum = old_onum,
                nested = int(request.POST.get('nested')) + 1,              
                ).save() 
                
                
        except:
            print('ReplyokFunc err')
    
    return HttpResponseRedirect('/board/list') # 댓글 후 목록 보기
            

    
