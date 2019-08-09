from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def MainFunc(request):
    return render(request, 'index.html')


class CallView(TemplateView):
    template_name = "callget.html"
    
    
def InsertFunc(request):
    if request.method == 'GET':
        print('get요청 처리')
        return render(request, 'insert.html')
    elif request.method == 'POST':
        print('post요청 처리')
        irum = request.POST.get("name") + '님'
        #irum = request.POST.get["name"]  # request 방법 2가지               
        return render(request, 'list.html', {'irum':irum})    
    else:
        print('요청 실패')
        

    
        
        
        