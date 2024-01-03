from django.contrib import admin
from . import models


# Register Tickets ModelAdmin
@admin.register(models.Ticket)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status', 'is_active')
    list_display_links = ('user', 'title')


# Register ChatRoom ModelAdmin
@admin.register(models.ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    list_display_links = ('id', 'title',)
    filter_horizontal = ('participants',)
