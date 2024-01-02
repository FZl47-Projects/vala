from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='account:login'), name='logout'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/verify/', views.VerifyPhoneNumberView.as_view(), name='verify_phone'),
    path('register/questions/', views.CompleteProfileView.as_view(), name='complete_profile'),
    path('register/send-code/', views.SendCodeView.as_view(), name='send_verify_code'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/details/', views.ProfileDetailView.as_view(), name='profile_details'),

    path('password/edit/', views.EditUserPassView.as_view(), name='edit_password'),

    path('users/list/', views.UsersListView.as_view(), name='users_list'),
]
