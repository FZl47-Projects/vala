from django.contrib import admin
from . import models


# Register DietProgram model amin
@admin.register(models.DietProgram)
class DietProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'status', 'is_active')
    list_display_links = ('id', 'user', 'title')
    list_filter = ('is_active', 'status')


# Register ExerciseProgram model amin
@admin.register(models.ExerciseProgram)
class ExerciseProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'status', 'is_active')
    list_display_links = ('id', 'user', 'title')
    list_filter = ('is_active', 'status')
