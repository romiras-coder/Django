from django.shortcuts import render
from .models import ProductCategory, Product

def main(request):
    return render(request, 'mainapp/index.html')


def about(request):
    return render(request, 'mainapp/about.html')


def contact(request):
    return render(request, 'mainapp/contact.html')

def pricelist(request, pk=None):
    print(pk)
    products = Product.objects.all()
    content = {'products': products}
    return render(request, 'mainapp/pricelist.html', content)
