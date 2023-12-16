from django.contrib import admin

from .models import Story, Post, PostComment


# Register Story ModelAdmin
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_display_links = ('title',)


# Register Post comments as inline
class PostCommentInline(admin.StackedInline):
    model = PostComment
    extra = 0


# Register Story ModelAdmin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)
    inlines = (PostCommentInline,)
