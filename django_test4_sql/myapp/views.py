from django.shortcuts import render
from myapp.models import Article, Article2

# Create your views here.
def main(request):
    return render(request, 'main.html')

def dbtest(request):
    print(Article.objects.all())
    return render(request, 'articlelist.html', {'art':Article.objects.all()})

def dbfriends(request):
    print(Article2.objects.all())
    return render(request, 'articlelist2.html', {'art':Article2.objects.all()})
