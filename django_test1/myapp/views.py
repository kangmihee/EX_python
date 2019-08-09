from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def indexFunc(request):
    return HttpResponse("인덱스 요청 처리") # 페이지 소스보기 불가능 (그냥 값만 넘겨받았기 때문)


def hello(request):
    ss = "<html><body>장고 프로젝트 만세</body></html>"
    return HttpResponse(ss)  # 페이지 소스보기 가능


def worldFunc(request):
    msg = "장마철"
    return render(request, 'world.html', {'message':msg}) # rendering 해준다.
    