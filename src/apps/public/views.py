from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import JsonResponse

from .models import Story, Post, PostLike, PostComment


# Render Index view
class IndexView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data = {
            'stories': Story.get_recent_stories(),  # Recent stories
            'posts': Post.get_recent_posts(self.request.user)  # Last 10 posts
        }

        context.update(data)
        return context


# Post Like view
class LikePostView(LoginRequiredMixin, View):
    def get(self, request, pk):
        try:
            obj = PostLike.objects.get(post_id=pk, user=request.user)
            obj.delete()
        except PostLike.DoesNotExist:
            PostLike.objects.create(post_id=pk, user=request.user)
            return JsonResponse({'response': 'liked'})

        return JsonResponse({'response': 'disliked'})


# Add Post Comment view
class AddPostCommentView(LoginRequiredMixin, CreateView):
    template_name = 'public/index.html'
    model = PostComment
    fields = ('post', 'text')
    success_url = reverse_lazy('public:index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        
        obj.user = self.request.user  # Add user to current comment
        obj.save()
        
        return super().form_valid(form)


# Verify Post Comment view
class VerifyPostCommentView(LoginRequiredMixin, View):
    def post(self):
        pass
