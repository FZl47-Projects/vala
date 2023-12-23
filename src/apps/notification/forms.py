from django import forms
from . import models


class NotificationUserFormAdd(forms.ModelForm):
    class Meta:
        model = models.NotificationUser
        exclude = ('is_showing', 'is_seen', 'number_id')
