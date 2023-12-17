from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='account:login'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
]
