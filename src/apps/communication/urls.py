from django.urls import path
from . import views


app_name = 'communication'

urlpatterns = [
    path('tickets/', views.TicketsListView.as_view(), name='tickets_list'),
    path('tickets/add/', views.AddTicketView.as_view(), name='add_ticket'),
    path('tickets/all/', views.AdminTicketsListView.as_view(), name='all_tickets'),

    path('chat/list/', views.ChatListView.as_view(), name='chats_list'),
    path('chat/session/<int:pk>/', views.ChatRoomView.as_view(), name='chat_room'),
    path('chat/create/', views.CreateChatRoomView.as_view(), name='create_chat'),
    path('chat/session/send-message/', views.SendMessageView.as_view(), name='send_chat_message'),
]
