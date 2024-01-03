from django.contrib import admin

from . import models


# Register Story ModelAdmin
@admin.register(models.Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_display_links = ('title',)


# Register Post comments as inline
class PostCommentInline(admin.StackedInline):
    model = models.PostComment
    extra = 0


# Register Story ModelAdmin
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'file', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)
    inlines = (PostCommentInline,)


# Register Podcast ModelAdmin
@admin.register(models.Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image')
    list_display_links = ('title',)
