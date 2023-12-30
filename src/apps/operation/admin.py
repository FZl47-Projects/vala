from django.contrib import admin
from . import models


# Register Test model admin
@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status', 'is_active')
    list_display_links = ('user', 'title')
