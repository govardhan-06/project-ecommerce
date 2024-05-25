from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products=Product.objects.all().order_by('-priority')[:4]
    latest_products=Product.objects.all().order_by('-created_at')[:4]
    context={"featured":featured_products,'latest':latest_products}
    return render(request, 'index.html',context)

def list_products(request):
    page=1
    if(request.GET):
        page=request.GET.get('page',1)
    products_lists=Product.objects.all().order_by('priority')
    product_pages=Paginator(products_lists,3)
    products=product_pages.get_page(page)
    return render(request, 'products_layout.html',{'products':products})

def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request, 'product_details.html',{'product':product})