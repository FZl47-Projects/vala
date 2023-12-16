from django.contrib import admin

from .models import Story


# Register Story ModelAdmin
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_display_links = ('title',)
