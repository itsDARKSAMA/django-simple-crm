from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_register(request):
    if request.user.is_authenticated:
        messages.warning(request,"You're already Signed in")
        return redirect('index')
    else:
        form = CreateNewUserForm()
        if request.method == 'POST':
            form = CreateNewUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'User has been created successfully')
                redirect('login')
        else:
            form = CreateNewUserForm()

        return render(request,'register.html',{'form':form})



def user_login(request):
    if request.user.is_authenticated:
        messages.warning(request,"You're already Signed in")
        return redirect('index')
    else:
        form = UserLoginForm()

        if request.method == "POST":
            form = UserLoginForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
            
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request,user=user)
                    messages.success(request,f'Login Success , Welcome {user}')
                    return redirect('index')
        else:
            form = UserLoginForm()
        
        return render(request,'login.html',{'form':form})
        

@login_required
def user_logout(request):
    
    # if User.is_authenticated:
        logout(request=request)
        messages.success(request,'Logout Success')
        return redirect('login')


@login_required
def user_settings(request):
    
    return render(request,'user_settings.html')