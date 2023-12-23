from django.db import models
from django.urls import reverse
from apps.core.models import BaseModel


class Meeting(BaseModel):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    operator = models.ForeignKey('account.User', null=True, on_delete=models.SET_NULL, related_name='operator_user')
    time_start = models.TimeField(null=True)
    time_end = models.TimeField(null=True)
    description = models.TextField(null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'#{self.id} - Meeting'

    def get_absolute_url(self):
        # TODO: should be completed
        return reverse('dashboard:index')


class AreaBody(BaseModel):
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE)
    area_name = models.CharField(max_length=20)
    area_code = models.CharField(max_length=8)
    intensity = models.CharField(max_length=15)
    note = models.TextField(null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'{self.meeting} - Area Body({self.area_code})'
