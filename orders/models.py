from django.db import models
from customers.models import Customers
from products.models import Product

# Create your models here.
class Order(models.Model):
    owner=models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True,related_name='userCart')
    updated_on=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICES=((ORDER_PROCESSED,'ORDER_PROCESSED'),
                    (ORDER_DELIVERED,'ORDER_DELIVERED'),
                    (ORDER_REJECTED,'ORDER_REJECTED'))
    order_status=models.IntegerField(choices=STATUS_CHOICES,default=CART_STAGE)
    LIVE=1
    DELETE=0
    DELETE_CHOICES = ((LIVE,'LIVE'),(DELETE,'DELETE'))
    status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

class OrdererdItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='addedItems')
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Customers,on_delete=models.CASCADE,related_name='cart')