from django.urls import path
from . import views


app_name = 'communication'

urlpatterns = [
    path('tickets/', views.TicketsListView.as_view(), name='tickets_list'),
    path('tickets/add/', views.AddTicketView.as_view(), name='add_ticket'),
    path('tickets/all/', views.AdminTicketsListView.as_view(), name='all_tickets'),
]
