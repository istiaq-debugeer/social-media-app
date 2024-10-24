from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('create/',views.post_create,name='post_create'),
    path('feed/',views.feed,name='post_feed'),
    path('like',views.like_post,name='like')
    
]