from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart,name='cart'),
    path('add-Cart/', views.addCart,name='addtoCart'),
    path('delete-item/<pk>', views.delete_item,name='deleteItem'),
    path('checkout/', views.checkout,name='checkout'),
    path('showOrders/',views.show_orders,name='orders')
]
