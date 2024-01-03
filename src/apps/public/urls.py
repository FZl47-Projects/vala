from django.urls import path
from . import views


app_name = 'public'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('post/add/', views.AddPostViw.as_view(), name='add_post'),
    path('post/delete/', views.DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/like/', views.LikePostView.as_view(), name='like_post'),
    path('post/comments/add/', views.AddPostCommentView.as_view(), name='add_post_comment'),
    path('post/comments/<int:pk>/verify/', views.VerifyPostCommentView.as_view(), name='verify_post_comment'),
    path('post/comments/delete/', views.DeletePostCommentView.as_view(), name='delete_post_comment'),
    path('post/<int:pk>/pin/', views.PinPostView.as_view(), name='pin_post'),

    path('story/add/', views.AddStoryView.as_view(), name='add_story'),
    path('story/<int:pk>/pin/', views.PinStoryView.as_view(), name='pin_story'),

    path('podcasts/', views.PodcastsView.as_view(), name='podcasts_list'),
    path('podcasts/add/', views.AddPodcastView.as_view(), name='add_podcast'),
    path('podcasts/delete/', views.DeletePodcastView.as_view(), name='delete_podcast'),
]
