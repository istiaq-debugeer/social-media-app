from django.shortcuts import render

from .forms import LoginForm,UserRegistarationForm,UserEditForm,ProfileEditForm
from django.http import HttpResponse
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from Post.models import Post

def index(request):
    current_user=request.user
    posts=Post.objects.filter(user=current_user).all()
    profile=Profile.objects.filter(user=current_user).first()
    return render(request,'index.html',{'posts':posts,'profile':profile})

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

@login_required
def custom_logout(request):
    logout(request)
    # Add any custom logic here, such as:
    # - Logging the logout event
    # - Redirecting to a specific page
    # - Clearing session data
    return HttpResponse('redirect logout')  # Redirect 


def register(request):
    if request.method=='POST':
        user_form=UserRegistarationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'register_done.html')
    else:
        user_form=UserRegistarationForm()
    return render(request,'register.html',{'user_form':user_form})

@login_required
def edit(request):
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user,data=request.POST)
        user_profile=ProfileEditForm(instance=request.user,data=request.POST,files=request.FILES)

        if user_form.is_valid() and user_profile.is_valid():
            user_form.save()
            user_profile.save()

    else:
        user_form=UserEditForm(instance=request.user)
        user_profile=ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
    return render(request,'edit_form.html',{'user_form':user_form ,'user_profile':user_profile})            

