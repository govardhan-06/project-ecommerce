from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('view-products/', views.list_products,name='product-list'),
]
