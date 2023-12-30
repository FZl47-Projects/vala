from django.utils.translation import gettext as _
from django.shortcuts import reverse
from django.db import models

from apps.core.models import BaseModel
from apps.core.utils import get_time
from apps.account.models import User
from .enums import TestStatusChoices


# Tests model
class Test(BaseModel):
    State = TestStatusChoices

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='tests')
    title = models.CharField(_('Title'), max_length=128, default=_('No title'))
    text = models.TextField(_('Test text'), null=True, blank=True)
    file = models.FileField(_('Test file'), upload_to=f'files/tests/{get_time("%Y-%m-%d")}/')
    status = models.CharField(_('Status'), max_length=64, choices=State.choices, default=State.AWAIT)
    answer = models.TextField(_('Admin answer'), null=True, blank=True)

    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Test')
        verbose_name_plural = _('Tests')
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.title} - {self.text[:15]}'

    def get_file_url(self):
        if self.file:
            return self.file.url

    def get_status_label(self):
        return self.get_status_display()

    def get_absolute_url(self):
        return reverse('operation:test_details', args=[self.pk])

    def get_date_created(self):
        return self.created_at.strftime('%Y/%m/%d')
