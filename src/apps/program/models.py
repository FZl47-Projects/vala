from django.utils.translation import gettext as _
from django.shortcuts import reverse
from django.db import models

from apps.core.models import BaseModel
from apps.account.models import User
from .enums import ProgramStatusEnum


# DietProgram model
class DietProgram(BaseModel):
    StatusEnum = ProgramStatusEnum

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diet_programs', verbose_name=_('User'))
    title = models.CharField(_('Title'), max_length=128, default=_('No title'))
    description = models.TextField(_('Description'), null=True, blank=True)
    status = models.CharField(_('Status'), max_length=64, choices=StatusEnum.choices, default=StatusEnum.UNDEFINED)

    saturday = models.TextField(_('Saturday program'), null=True, blank=True)
    sunday = models.TextField(_('Sunday program'), null=True, blank=True)
    monday = models.TextField(_('Monday program'), null=True, blank=True)
    tuesday = models.TextField(_('Tuesday program'), null=True, blank=True)
    wednesday = models.TextField(_('Wednesday program'), null=True, blank=True)
    thursday = models.TextField(_('Thursday program'), null=True, blank=True)
    friday = models.TextField(_('Friday program'), null=True, blank=True)

    is_active = models.BooleanField(_('Is active'), default=True)

    class Meta:
        verbose_name = _('Diet program')
        verbose_name_plural = _('Diet programs')
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('program:diet_details', args=[self.pk])

    def get_date_created(self):
        return self.created_at.strftime('%Y-%m-%d')


# ExerciseProgram model
class ExerciseProgram(BaseModel):
    StatusEnum = ProgramStatusEnum

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exercise_programs', verbose_name=_('User'))
    title = models.CharField(_('Title'), max_length=128, default=_('No title'))
    description = models.TextField(_('Description'), null=True, blank=True)
    status = models.CharField(_('Status'), max_length=64, choices=StatusEnum.choices, default=StatusEnum.UNDEFINED)

    saturday = models.TextField(_('Saturday program'), null=True, blank=True)
    sunday = models.TextField(_('Sunday program'), null=True, blank=True)
    monday = models.TextField(_('Monday program'), null=True, blank=True)
    tuesday = models.TextField(_('Tuesday program'), null=True, blank=True)
    wednesday = models.TextField(_('Wednesday program'), null=True, blank=True)
    thursday = models.TextField(_('Thursday program'), null=True, blank=True)
    friday = models.TextField(_('Friday program'), null=True, blank=True)

    is_active = models.BooleanField(_('Is active'), default=True)

    class Meta:
        verbose_name = _('Exercise program')
        verbose_name_plural = _('Exercise programs')
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('program:exercise_details', args=[self.pk])

    def get_date_created(self):
        return self.created_at.strftime('%Y-%m-%d')
