from users.models import Profile
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import PostForm,CommentForm
from .models import Post,Comment
# Create your views here.
@login_required
def post_create(request):
    if request.method=='POST':
        post_form=PostForm(data=request.POST,files=request.FILES)
        if post_form.is_valid():
            new_post=post_form.save(commit=False)
            new_post.user=request.user
            new_post.save()
            Post.objects.create(user=request.user)
            return HttpResponse('saved post')    
        else: 
            print(post_form.errors)   
            return HttpResponse('form data is not valid') 
    else:
        post_form=PostForm(data=request.GET)
    return render(request,'post_form.html',{'post_form':post_form})        

def feed(request):
    if request.method=='POST':
        comment_form=CommentForm(data=request.POST)
        new_comment=comment_form.save(commit=False)
        post_id=request.POST.get('post_id')
        post=get_object_or_404(Post,id=post_id)
        new_comment.post=post
        new_comment.save()
        return 
    else:
        comment_form=CommentForm()
            
    posts=Post.objects.all()
    
    return render(request,'feed.html',{'posts':posts,'comment':comment_form})


def like_post(request):
    post_id=request.POST.get('post_id')
    post=get_object_or_404(Post,id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('feed')