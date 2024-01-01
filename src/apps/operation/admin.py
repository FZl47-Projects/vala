from django.contrib import admin
from . import models


# Register Test model admin
@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status', 'is_active')
    list_display_links = ('user', 'title')


# Register RecoveryProcessImage as inline
class RecoveryProcessInline(admin.StackedInline):
    model = models.RecoveryProcessImage
    extra = 0


# Register RecoveryProcess model admin
@admin.register(models.RecoveryProcess)
class RecoveryProcessAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_active')
    list_display_links = ('user', 'title')
    inlines = (RecoveryProcessInline,)
