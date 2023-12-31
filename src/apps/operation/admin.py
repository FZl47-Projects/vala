from django.contrib import admin
from . import models


# Register Test model admin
@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'status', 'is_active')
    list_display_links = ('id', 'user', 'title')
    search_fields = ('id', 'user__phone_number', 'title')


# Register RecoveryProcessImage as inline
class RecoveryProcessInline(admin.StackedInline):
    model = models.RecoveryProcessImage
    extra = 0


# Register RecoveryProcess model admin
@admin.register(models.RecoveryProcess)
class RecoveryProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'is_active')
    list_display_links = ('id', 'user', 'title')
    inlines = (RecoveryProcessInline,)
    search_fields = ('id', 'user__phone_number', 'title')


# Register SkinRoutine model admin
@admin.register(models.SkinRoutine)
class SkinRoutineAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_active')
    list_display_links = ('id', 'user',)
    search_fields = ('id', 'user__phone_number', 'title')
