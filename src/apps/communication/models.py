from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db import models

from apps.core.models import BaseModel
from .enums import TicketStatusChoices

User = get_user_model()


# Tickets model
class Ticket(BaseModel):
    Status = TicketStatusChoices

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='tickets')
    title = models.CharField(_('Title'), max_length=128, null=True, blank=True)
    text = models.TextField(_('Ticket text'))
    status = models.CharField(_('Status'), max_length=64, choices=Status.choices, default=Status.OPEN)
    answer = models.TextField(_('Admin answer'), null=True, blank=True)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
        ordering = ('-id',)

    def __str__(self):
        return f'{self.user} - {self.title}'
