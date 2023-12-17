from django.utils.translation import gettext as _
from django.db import models

from datetime import datetime, timedelta
from apps.core.models import BaseModel
from apps.core.utils import get_time
from apps.account.models import User


# Stories model
class Story(BaseModel):
    title = models.CharField(_('Title'), max_length=64, default=_('No title'))
    caption = models.TextField(_('Caption'), max_length=512, null=True, blank=True)
    image = models.ImageField(_('Image'), upload_to=f'images/story/{get_time("%Y-%m-%d")}/')
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
            objects = cls.objects.filter(is_active=True, created_at__gte=active_time)
        else:
            objects = cls.objects.filter(is_active=True)[:8]

        return objects


# Posts model
class Post(BaseModel):
    title = models.CharField(_('Title'), max_length=64, default=_('No title'))
    caption = models.TextField(_('Caption'), null=True, blank=True)
    category = models.CharField(_('Category'), max_length=64, null=True, blank=True)
    image = models.ImageField(_('Image'), upload_to=f'images/post/{get_time("%Y-%m-%d")}/')
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def get_image_url(self):
        if self.image:
            return self.image.url

    def get_verified_comments(self):
        objects = self.post_comments.filter(is_verified=True)
        return objects


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
    text = models.TextField(_('Text'), max_length=255)
    is_verified = models.BooleanField(_('Verified'), default=False)

    class Meta:
        verbose_name = _('Post comment')
        verbose_name_plural = _('Post comments')
        ordering = ('-id',)

    def __str__(self):
        return f'{self.user} - {self.post}'
