from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        ConfirmPassword=request.POST.get('ConfirmPassword')

        if password == ConfirmPassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
                return redirect('register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register/')
            else:
                user_reg=User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                messages.info(request,"successfully created")
                return redirect("/")
        else:
            messages.success(request,"password doesn't match")
            return redirect('register/')    
        
    return render(request,'userapp/register.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Login Successfully")
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('register/')
        

    return render(request,'userapp/login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')