from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customers(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.TextField()
    updated_on=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')

    LIVE=1
    DELETE=0
    DELETE_CHOICES = ((LIVE,'LIVE'),(DELETE,'DELETE'))
    status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

    def __str__(self) -> str:
        return self.title