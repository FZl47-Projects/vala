from django.utils.crypto import get_random_string
from django.db import models
from django.urls import reverse
from apps.core.models import BaseModel


def random_number_id():
    return get_random_string(10)


class Meeting(BaseModel):
    number_id = models.CharField(max_length=10, default=random_number_id)
    user = models.ForeignKey('account.User', null=True, on_delete=models.SET_NULL)
    operator = models.ForeignKey('account.User', null=True, on_delete=models.SET_NULL,
                                 related_name='meetings_set_operator')
    device_name = models.CharField(max_length=100)
    time_start = models.TimeField(null=True)
    time_end = models.TimeField(null=True)
    description = models.TextField(null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'#{self.id} - Meeting'

    def get_absolute_url(self):
        return reverse('cartex:meeting__detail', args=(self.id,))

    def get_areas(self):
        return self.areabody_set.all()

    def get_time_start(self):
        if self.time_start:
            return self.time_start.strftime('%H:%M')

    def get_time_end(self):
        if self.time_end:
            return self.time_end.strftime('%H:%M')


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
