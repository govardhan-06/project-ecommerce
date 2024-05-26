from django.shortcuts import render,redirect
from django.contrib import messages
from products.models import Product
from . models import Order,OrdererdItem
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="account")
def cart(request):
    user=request.user 
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    ordered_items = OrdererdItem.objects.filter(owner=customer)
    return render(request,'cart.html',{'cart':ordered_items})

@login_required(login_url="account")
def addCart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        product_id=request.POST.get('productID')
        qty=int(request.POST.get('quantity'))
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Product.objects.get(id=product_id)
        ordered_item,created=OrdererdItem.objects.get_or_create(
            product=product,
            owner=customer,
        )
        if created:
            ordered_item.quantity=qty
        else:
            ordered_item.quantity=ordered_item.quantity+qty
        ordered_item.save()
        return redirect('cart')
    return redirect('cart')

@login_required(login_url="account")
def delete_item(request,pk):
    item=OrdererdItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

@login_required(login_url="account")
def checkout(request):
    try:
        if request.POST:
            user=request.user
            customer=user.customer_profile
            total=request.POST.get('total')
            order_obj,created=Order.objects.get_or_create(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                statusMessage='Your order is processed. Delivery within two days...'
                messages.success(request,statusMessage)
            else:
                statusMessage='Checkout Failed'
                messages.success(request,statusMessage)
    except Exception as e:
        statusMessage=e
        messages.success(request,statusMessage)
    return redirect('cart')
    
@login_required(login_url="account")
def show_orders(request):
    user=request.user 
    customer=user.customer_profile
    ordered_items = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    return render(request,'orders.html',{'orders':ordered_items})