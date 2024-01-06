from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages

from apps.account.mixins import AccessRequiredMixin
from apps.account.enums import UserAccessEnum
from . import models

User = get_user_model()


# Render Index view
class IndexView(TemplateView):
    template_name = 'public/index.html'

    def get_template_names(self):
        user = self.request.user
        if user.is_authenticated and user.has_admin_access:
            return 'public/admin/index-admin.html'

        return super().get_template_names()

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        contexts['stories'] = models.Story.get_recent_stories()  # Recent stories
        contexts['posts'] = models.Post.get_recent_posts(self.request.user)  # Last 10 posts

        return contexts


# Add Post view
class AddPostViw(AccessRequiredMixin, CreateView):
    template_name = 'public/admin/index-admin.html'
    model = models.Post
    fields = ('title', 'caption', 'category', 'file')
    success_url = reverse_lazy('public:index')
    roles = [UserAccessEnum.ADMIN]

    def form_valid(self, form):
        messages.success(self.request, _('Post successfully added'))
        return super().form_valid(form)


# Delete Post view
class DeletePostView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def post(self, request):
        data = request.POST.copy()

        obj = get_object_or_404(models.Post, pk=data.get('pk'))
        obj.delete()

        messages.success(request, _('Post deleted successfully'))
        return redirect('public:index')


# Post Like view
class LikePostView(LoginRequiredMixin, View):
    def get(self, request, pk):
        try:
            obj = models.PostLike.objects.get(post_id=pk, user=request.user)
            obj.delete()
        except models.PostLike.DoesNotExist:
            models.PostLike.objects.create(post_id=pk, user=request.user)
            return JsonResponse({'response': 'liked'})

        return JsonResponse({'response': 'disliked'})


# Add Post Comment view
class AddPostCommentView(LoginRequiredMixin, CreateView):
    template_name = 'public/index.html'
    model = models.PostComment
    fields = ('post', 'text')
    success_url = reverse_lazy('public:index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        
        obj.user = self.request.user  # Add user to current comment
        obj.save()

        messages.success(self.request, _('Comment successfully sent and will be shown after admin verification'))
        return super().form_valid(form)


# Verify Post Comment view
class VerifyPostCommentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        obj = get_object_or_404(models.PostComment, pk=pk)

        obj.is_verified = True
        obj.save()

        return JsonResponse({'response': 'verified'})


# Delete Post Comment view
class DeletePostCommentView(LoginRequiredMixin, View):
    def post(self, request):
        data = request.POST.copy()
        obj = get_object_or_404(models.PostComment, pk=data.get('pk'))

        # Delete comment (deactivate)
        obj.is_active = False
        obj.save()

        messages.success(request, _('Comment deleted'))
        return redirect('public:index')


# Add Story view
class AddStoryView(AccessRequiredMixin, CreateView):
    template_name = 'public/admin/index-admin.html'
    model = models.Story
    fields = ('title', 'caption', 'image')
    success_url = reverse_lazy('public:index')
    roles = [UserAccessEnum.ADMIN]

    def form_valid(self, form):
        messages.success(self.request, _('Story successfully added'))
        return super().form_valid(form)


# Delete Story view
class DeleteStoryView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def post(self, request):
        pk = request.POST.get('pk')
        obj = get_object_or_404(models.Story, pk=pk)

        obj.is_active = False
        obj.save()

        messages.success(self.request, _('Story successfully deleted'))
        return redirect('public:index')


# Pin Story view
class PinStoryView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def get(self, request, pk):
        obj = get_object_or_404(models.Story, pk=pk)
        pin_state = request.GET.get('state')

        if pin_state == 'False':
            pinned_count = models.Story.objects.filter(is_active=True, pinned=True).count()

            if pinned_count >= 3:
                messages.error(request, _('You cannot pin more than 3 stories'))
                return redirect('public:index')

        obj.pinned = not obj.pinned
        obj.save()

        messages.success(request, _('Operation done successfully'))
        return redirect('public:index')


# Pin Post view
class PinPostView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def get(self, request, pk):
        obj = get_object_or_404(models.Post, pk=pk)
        pin_state = request.GET.get('state')

        if pin_state == 'False':
            pinned_count = models.Post.objects.filter(is_active=True, pinned=True).count()

            if pinned_count >= 3:
                messages.error(request, _('You cannot pin more than 3 posts'))
                return redirect('public:index')

        obj.pinned = not obj.pinned
        obj.save()

        messages.success(request, _('Operation done successfully'))
        return redirect('public:index')


# Render Podcast view
class PodcastsView(TemplateView):
    template_name = 'public/podcasts.html'

    def get_template_names(self):
        user = self.request.user
        if user.is_authenticated and user.has_admin_access:
            return 'public/admin/podcasts-admin.html'
        
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        contexts['stories'] = models.Story.get_recent_stories()  # Get recent stories
        contexts['podcasts'] = models.Podcast.objects.filter(is_active=True)

        return contexts


# Add Podcast view
class AddPodcastView(AccessRequiredMixin, CreateView):
    template_name = 'public/admin/podcasts-admin.html'
    model = models.Podcast
    fields = ('title', 'text', 'category', 'image', 'audio')
    success_url = reverse_lazy('public:podcasts_list')
    roles = [UserAccessEnum.ADMIN]

    def form_valid(self, form):
        messages.success(self.request, _('Podcast successfully added'))
        return super().form_valid(form)


# Delete Podcast view
class DeletePodcastView(AccessRequiredMixin, View):
    template_name = 'public/admin/podcasts-admin.html'
    roles = [UserAccessEnum.ADMIN]

    def post(self, request):
        data = request.POST.copy()
        obj = get_object_or_404(models.Podcast, pk=data.get('pk'))

        # Delete podcast (deactivate)
        obj.is_active = False
        obj.save()

        messages.success(request, _('Podcast successfully deleted'))
        return redirect('public:podcasts_list')
