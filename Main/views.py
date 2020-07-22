from django.shortcuts import render
from Main.models import *

def home(request):
    return render(request,'base/home.html')

def user_home(request):
    return render(request,'user/homepage.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user_details = UserRegister.objects.all().filter(name=username,password=password)
        if user_details:
            return render(request,'user/homepage.html')
        else:
            message = 'Invaild username and password!'
            return render(request,'user/login.html',{'message':message})
    else:
        return render(request,'user/login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phonenumber = request.POST['phoneno']
        password = request.POST['pass']
        user_details = UserRegister(name=username,email=email,password=password,phone_number=phonenumber)
        user_details.save()
        return render(request,'user/register.html')
    else:
        return render(request,'user/register.html')

def user_profile(request):
    return render(request,'user/profile.html')

def company_login(request):
    return render(request,'company/login.html')

def company_register(request):
    return render(request,'company/register.html')


