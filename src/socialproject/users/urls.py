from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns=[
    path('index/',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.custom_logout,name='logout'),
    path('password_change/',auth_view.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='pass_reset_form'),name='password_reset'),
    path('password_reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='pass_reset.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='passwordreset.html'),name='password_reset_confirm'),
    path('reset/done/',auth_view.PasswordResetCompleteView.as_view(template_name='reset_complete.html'),name='password_rest_complete '),
    path('register/',views.register,name='registation'),
    path('edit/',views.edit,name='edit_form'),
    
   
]
     