from django.urls import path
from . import views

app_name = 'apps.account'
urlpatterns = [
    # login logout and register
    path('login', views.Login.as_view(), name='login'),
    path('register', views.Register.as_view(), name='register'),
    path('logout', views.Logout.as_view(), name='logout'),
    # confirm account
    path('confirm/phonenumber', views.ConfirmPhonenumber.as_view(), name='confirm_phonenumber'),
    path('confirm/phonenumber/check', views.ConfirmPhonenumberCheckCode.as_view(),
         name='confirm_phonenumber_check_code'),
    # reset password
    path('reset-password', views.ResetPassword.as_view(), name='reset_password'),
    path('reset-password/send-code', views.ResetPasswordSend.as_view(), name='reset_password_send_code'),
    path('reset-password/check-code', views.ResetPasswordCheck.as_view(), name='reset_password_check_code'),
    path('reset-password/set', views.ResetPasswordSet.as_view(), name='reset_password_set'),
]
