from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import newfile


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
                return redirect('admin_login')  # Assuming you have a named URL for admin dashboard
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
def user_view(request):
    return render(request,'user.html')

def princi(request):
    context = {}  # Define context here
    
    if request.method == 'POST':

        newfiles = newfile()
        newfiles.save()
        context = {'newfile': newfiles}
        return HttpResponse("success")
        
    return render(request, 'principal.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home_page')
