from django.shortcuts import render
from . models import Product

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_products(request):
    products_lists=Product.objects.all()
    return render(request, 'products_layout.html',{'products':products_lists})

def detail_product(request):
    return render(request, 'product_details.html')