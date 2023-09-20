from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import newfile
from django.contrib.auth.models import User
from .decorators import role_required
from datetime import datetime


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            print("User logged in successfully")  # Add this line for debugging
            if request.user.is_staff:
                return redirect('admin_login')  # Assuming you have a named URL for admin dashboard  # Assuming you have a named URL for office staff dashboard
            elif user.groups.filter(name='PRINCIPAL').exists():
                return redirect('principal_dashbord')
              
            elif user.groups.filter(name='SUPERINTENDENT').exists():
                return redirect('superintendent_dashbord')
            
            else:
                return redirect('user_dashbord')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    else:
        return render(request, "login.html")
     

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request,"about.html")


@role_required('OFFICE STAFFS')
def staff_view(request):
    return render(request,'user.html')

@role_required('SUPERINTENDENT')
def superintendent_view(request):
    context = {}  # Define context here
    if request.method == 'POST':
        section = request.POST['section']
        newfiles = newfile()
        newfiles.reciver = section
        newfiles.created_date=datetime.now() 
        newfiles.save()
        context = {'newfile': newfiles}
        messages.success(request, 'Succes')        
    
    usernames = User.objects.filter(is_superuser=False).values_list('username', flat=True)
    context['usernames'] = usernames
    return render(request,'superintendent.html',context)

@role_required('PRINCIPAL')
def princi(request):
    context = {}  # Define context here
    if request.method == 'POST':
        section = request.POST['section']
        newfiles = newfile()
        newfiles.reciver = section
        newfiles.created_date=datetime.now() 
        newfiles.save()
        context = {'newfile': newfiles}
        messages.success(request, 'Succes')        
    
    usernames = User.objects.filter(is_superuser=False).values_list('username', flat=True)
    context['usernames'] = usernames
    file = {'newfile': newfiles}

    return render(request, 'principal.html', context,file)


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home_page')
