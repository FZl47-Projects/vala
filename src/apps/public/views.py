from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.shortcuts import redirect, reverse
from django.db.models import Exists, OuterRef
from django.http import JsonResponse

from .models import Story, Post, PostLike


# Render Index view
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data = {
            'stories': Story.get_recent_stories(),  # Recent stories
            'posts': Post.objects.annotate(
                user_liked=Exists(PostLike.objects.filter(post=OuterRef('pk'), user=self.request.user)))[:10],  # Last 10 posts
        }

        context.update(data)
        return context


# PostLike view
class LikePostView(LoginRequiredMixin, View):
    def get(self, request, pk):
        try:
            obj = PostLike.objects.get(post_id=pk, user=request.user)
            obj.delete()
        except PostLike.DoesNotExist:
            PostLike.objects.create(post_id=pk, user=request.user)
            return JsonResponse({'response': 'liked'})

        return JsonResponse({'response': 'disliked'})
