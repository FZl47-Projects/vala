from django.urls import path
from . import views

app_name = 'apps.cartex'
urlpatterns = [
    path('meeting/add', views.MeetingAdd.as_view(), name='meeting__add')
]
