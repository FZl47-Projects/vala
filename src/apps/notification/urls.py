from django.urls import path
from . import views

app_name = 'notification'
urlpatterns = [
    # dashboard
    path('dashboard/user/add', views.NotificationUserAdd.as_view(), name='notification_user__add'),
    path('dashboard/user/<int:notification_id>/delete', views.NotificationUserDelete.as_view(), name='notification_user__delete'),
    path('dashboard/user/detail/<int:notification_id>', views.NotificationUserDetail.as_view(),
         name='notification_user__detail'),
    path('dashboard/personal/list', views.NotificationUserPersonalList.as_view(), name='notification_personal__list'),
    path('dashboard/user/list', views.NotificationUserList.as_view(), name='notification_user__list'),
]
