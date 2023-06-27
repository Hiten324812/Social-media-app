
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('passchange/',auth_view.PasswordChangeView.as_view(template_name='password_change.html'),name='passchange'),
    path('pass_change_done/',auth_view.PasswordChangeDoneView.as_view(template_name='pass_done.html'),name='password_change_done'),


    path('pass_res/',auth_view.PasswordResetView.as_view(template_name='pass_res.html'),name='password_reset'),
    path('pass_res_done/',auth_view.PasswordResetDoneView.as_view(template_name='pass_res_done.html'),name='password_reset_done'),
    path('pass_res_confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='pass_res_confirm.html'),name='password_reset_confirm'),
    path('pass_com/',auth_view.PasswordResetCompleteView.as_view(template_name='pass_comp.html'),name='password_reset_complete'),

    path('register/',views.register,name='register'),
    path('edit/',views.edit,name='edit'),
    

]
