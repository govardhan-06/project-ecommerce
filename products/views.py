from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_products(request):
    page=1
    if(request.GET):
        page=request.GET.get('page',1)
    products_lists=Product.objects.all()
    product_pages=Paginator(products_lists,3)
    products=product_pages.get_page(page)
    return render(request, 'products_layout.html',{'products':products})

def detail_product(request):
    return render(request, 'product_details.html')