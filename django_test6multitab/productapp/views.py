from django.shortcuts import render
from productapp.models import Maker, Product

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def List1(request):
    makers = Maker.objects.all()
    return render(request, 'list1.html', {'makers':makers})

def List2(request):
    products = Product.objects.all()
    pcount = len(products)
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})

def List3(request):
    mid = request.GET.get('id')
    prod = Product.objects.all().filter(maker_name=mid)
    pcount = len(prod)
    return render(request, 'list3.html', {'products':prod, 'pcount':pcount})



