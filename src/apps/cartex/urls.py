from django.urls import path
from . import views

app_name = 'apps.cartex'
urlpatterns = [
    path('meeting/add', views.MeetingAdd.as_view(), name='meeting__add'),
    path('meeting/list', views.MeetingList.as_view(), name='meeting__list'),
    path('meeting/detail/<int:meeting_id>', views.MeetingDetail.as_view(), name='meeting__detail'),
    path('meeting/delete/<int:meeting_id>', views.MeetingDelete.as_view(), name='meeting__delete'),

    path('area-body/update/<int:area_id>', views.AreaBodyUpdate.as_view(), name='area_body__update'),
    path('area-body/delete/<int:area_id>', views.AreaBodyDelete.as_view(), name='area_body__delete'),
]
