from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    return render(request,'index.html')

def user_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(f"Received form data: {data}")  # Print received data for debugging
            user=authenticate(
                request,username=data['username'],password=data['password'])
            if  user is not None:
                login(request,user)
                return HttpResponse('login successfully')
            else:
                return HttpResponse('Invalid credential')
            
    else:

        form=LoginForm()
    return render(request,'login.html',{'form':form})


def custom_logout(request):
    logout(request)
    # Add any custom logic here, such as:
    # - Logging the logout event
    # - Redirecting to a specific page
    # - Clearing session data
    return HttpResponse('redirect logout')  # Redirect 