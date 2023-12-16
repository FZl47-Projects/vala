from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.shortcuts import redirect, reverse
from django.db.models import Exists, OuterRef

from .models import Story, Post, PostLike


# Render Index view
class IndexView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {
            'stories': Story.get_recent_stories(),  # Recent 24 hours stories
            'posts': Post.objects.annotate(user_liked=Exists(PostLike.objects.filter(post=OuterRef('pk'), user=self.request.user)))
        }

        context.update(data)

        return context
