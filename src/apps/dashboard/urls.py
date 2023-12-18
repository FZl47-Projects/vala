from django.urls import path
from . import views

app_name = 'apps.dashboard'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    # Notification
    path('notifications', views.Notifications.as_view(), name='notifications'),

]
