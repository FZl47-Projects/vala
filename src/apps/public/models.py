from django.utils.translation import gettext as _
from django.db import models

from datetime import datetime, timedelta
from apps.core.models import BaseModel
from apps.core.utils import get_time


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
    def get_recent_stories(cls):
        """ Return objects created within the last 24 hours """
        active_time = datetime.now() - timedelta(hours=24)
        objects = cls.objects.filter(is_active=True, created_at__gte=active_time)

        return objects
