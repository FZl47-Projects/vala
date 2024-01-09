from django.contrib import admin
from . import models


# Register Tickets ModelAdmin
@admin.register(models.Ticket)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'status')
    list_display_links = ('id', 'user', 'title')
    list_filter = ('status', 'is_active')
    search_fields = ('id', 'user__phone_number', 'title')


# Register ChatRoom ModelAdmin
@admin.register(models.ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title')
    filter_horizontal = ('participants',)
