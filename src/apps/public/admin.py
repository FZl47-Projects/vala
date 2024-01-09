from django.contrib import admin

from . import models


# Register Story ModelAdmin
@admin.register(models.Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'pinned')
    list_display_links = ('id', 'title')
    list_filter = ('pinned', 'is_active')


# Register Post comments as inline
class PostCommentInline(admin.StackedInline):
    model = models.PostComment
    extra = 0


# Register Story ModelAdmin
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'file', 'pinned')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'category')
    list_filter = ('pinned', 'is_active')
    inlines = (PostCommentInline,)


# Register Podcast ModelAdmin
@admin.register(models.Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'image')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'category')
    list_filter = ('is_active',)
