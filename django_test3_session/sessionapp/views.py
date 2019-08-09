from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.

def main(request):
    return render(request, 'main.html')


def setosFunc(request):
    if "favorite_os" in request.GET:
        print(request.GET["favorite_os"])
        request.session['f_os'] = request.GET["favorite_os"] # 세션생성(절대시간이 아니기 때문에  설정 하지 않으면 30초가 기본임)
        return HttpResponseRedirect('/showos')
    else:
        return render(request, 'setos.html')
    
    
def showosFunc(request):
    context = {}
    if "f_os" in request.session:
        context['f_os'] = request.session['f_os']
        context['message'] = "당신이 선택한 운영체제는 %s"%request.session['f_os']
    else:
        context['f_os'] = None
        context['message'] = "운영체제를 선택하지 않았군요"
        
    request.session.set_expiry(5) # 5초동안만 session을 가짐
    
    return render(request, 'shows.html', context)
        
        
        

