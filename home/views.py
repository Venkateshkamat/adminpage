from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method =='POST':
        username = request.POST['7']
        pass3 = request.POST['8']
        user = auth.authenticate(username = username,password=pass3)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name = request.POST['1']
        last_name = request.POST['2']
        username = request.POST['3']
        email = request.POST['4']
        pass1 = request.POST['5']
        pass2 = request.POST['6']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=pass1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'User Created')
                return redirect('login')
        
        else:
            messages.info(request,'Password not matching')
            return redirect('register')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')