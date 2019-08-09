from django.shortcuts import render
from examapp.models import Score
from django.http.response import HttpResponseRedirect

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def list(request):
    score = Score.objects.all()
    count = Score.objects.count()
    return render(request, 'list.html', {'score' : score, 'count' : count})

def insert(request):
    return render(request, 'insert.html')

def insertok(request):
    if request.method == 'POST':
        Score(
            id = request.POST.get('id'),
            irum = request.POST.get('irum'),
            kor = request.POST.get('kor'),
            eng = request.POST.get('eng'),
            
        ).save()
    return HttpResponseRedirect('/list')


