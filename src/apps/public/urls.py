from django.urls import path
from . import views


app_name = 'public'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('post/<int:pk>/like/', views.LikePostView.as_view(), name='like_post'),
    path('post/comments/add/', views.AddPostCommentView.as_view(), name='add_post_comment'),
    path('post/comments/<int:pk>/edit/', views.EditPostCommentView.as_view(), name='edit_post_comment'),
]
