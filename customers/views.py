from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Customers

# Create your views here.
def account(request):
    if request.POST and 'register' in request.POST:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email=request.POST.get('email')
            address = request.POST.get('address')
            phoneNumber = request.POST.get('phone')
            user=User.objects.create_user(username=username,password=password,email=email)
            customer=Customers.objects.create(user=user,phone=phoneNumber,address=address)
            login(request,user)
            return redirect('home')
        except:
            messages.error(request, 'Username already exists')
        
    elif request.POST and 'login' in request.POST:
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        email= request.POST.get('email')
        user = authenticate(username=username, password=password,email=email)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return redirect('account')
        
    return render(request, 'account.html')

def logout_view(request):
    logout(request)
    return redirect('home')