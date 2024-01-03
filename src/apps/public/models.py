from django.utils.translation import gettext as _
from django.db.models import Exists, OuterRef
from django.db import models

from apps.core.utils import get_time, get_file_extension
from datetime import datetime, timedelta
from apps.core.models import BaseModel
from apps.account.models import User


# Stories model
class Story(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='stories', null=True, blank=True)
    title = models.CharField(_('Title'), max_length=64, default=_('No title'))
    caption = models.TextField(_('Caption'), max_length=512, null=True, blank=True)
    image = models.ImageField(_('Image'), upload_to=f'images/story/{get_time("%Y-%m-%d")}/')
    pinned = models.BooleanField(_('Pinned'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Story')
        verbose_name_plural = _('Stories')
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def get_image_url(self):
        if self.image:
            return self.image.url

    @classmethod
    def get_recent_stories(cls, daily=False):
        """ Return objects created within the last 24 hours or last 8 ones """
        if daily:
            active_time = datetime.now() - timedelta(hours=24)
            objects = cls.objects.filter(is_active=True, pinned=False, created_at__gte=active_time)
        else:
            objects = cls.objects.filter(is_active=True, pinned=False)[:8]

        pinned = cls.objects.filter(is_active=True, pinned=True)
        objects = pinned | objects

        return objects.order_by('-pinned', '-created_at')


# Posts model
class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='posts', null=True, blank=True)
    title = models.CharField(_('Title'), max_length=64, default=_('No title'))
    caption = models.TextField(_('Caption'), null=True, blank=True)
    category = models.CharField(_('Category'), max_length=64, null=True, blank=True)
    file = models.FileField(_('File'), upload_to=f'files/posts/{get_time("%Y-%m-%d")}/', null=True)
    pinned = models.BooleanField(_('Pinned'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def get_file_url(self):
        if self.file:
            return self.file.url

    def get_file_type(self):
        image_files = ['.jpg', '.jpeg', '.png', '.svg', '.webp']
        extension = get_file_extension(self.file)

        if extension in image_files:
            return 'image'
        return 'video'

    def get_verified_comments(self):
        objects = self.post_comments.filter(is_active=True, is_verified=True)
        return objects

    def get_all_comments(self):
        objects = self.post_comments.filter(is_active=True)
        return objects

    @classmethod
    def get_recent_posts(cls, user=None):
        """ Return recent posts based on user login. if user is authenticated, returns posts with like state. """
        objects = cls.objects.filter(is_active=True, pinned=False)[:20]
        pinned = cls.objects.filter(is_active=True, pinned=True)
        objects = pinned | objects

        if user.is_authenticated:
            objects = objects.annotate(user_liked=Exists(PostLike.objects.filter(post=OuterRef('pk'), user=user)))

        return objects.order_by('-pinned', '-created_at')


# PostLikes model
class PostLike(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Post, verbose_name=_('Post'), on_delete=models.CASCADE, related_name='post_likes')

    class Meta:
        verbose_name = _('Post like')
        verbose_name_plural = _('Post likes')

    def __str__(self):
        return f'{self.user} - {self.post}'


# PostComments model
class PostComment(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE, related_name='post_comments')
    post = models.ForeignKey(Post, verbose_name=_('Post'), on_delete=models.CASCADE, related_name='post_comments')
    text = models.TextField(_('Text'))
    is_verified = models.BooleanField(_('Verified'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Post comment')
        verbose_name_plural = _('Post comments')
        ordering = ('-id',)

    def __str__(self):
        return f'{self.user} - {self.post}'


# Podcasts model
class Podcast(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='podcasts', null=True, blank=True)
    title = models.CharField(_('Title'), max_length=128)
    text = models.TextField(_('Podcast text'), null=True, blank=True)
    category = models.CharField(_('Category'), max_length=128, null=True, blank=True)
    image = models.ImageField(_('Podcast image'), upload_to='images/podcasts/')
    audio = models.FileField(_('Podcast audio'), upload_to='audios/podcasts/')
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Podcast')
        verbose_name_plural = _('Podcasts')
        ordering = ('-id',)

    def __str__(self):
        return f'{self.title} - {self.text[:15]}'

    def get_image_url(self):
        if self.image:
            return self.image.url

    def get_audio_url(self):
        if self.audio:
            return self.audio.url
