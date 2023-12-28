from django.urls import path
from . import views


app_name = 'communication'

urlpatterns = [
    path('tickets/', views.TicketListView.as_view(), name='tickets_list'),
    path('tickets/add/', views.AddTicketView.as_view(), name='add_ticket'),
]
