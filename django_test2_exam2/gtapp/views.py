from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def MainFunc(request):
    return render(request, 'index.html')

class CallView(TemplateView):
    template_name = "callget.html"


def InsertFunc2(request):
    if request.method == 'GET':
        print('get요청 처리')
        return render(request, 'insert2.html')
    elif request.method == 'POST':
        print('post요청 처리')
        sangpum = request.POST.get("sangpum")
        su = request.POST.get("su")
        danga = request.POST.get("danga")
        ga = int(su) * int(danga)        
        return render(request, 'list2.html', {'sangpum':sangpum,'ga':ga})    
    else:
        print('요청 실패')