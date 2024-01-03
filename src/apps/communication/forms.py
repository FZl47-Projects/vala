from django import forms
from . import models


# Create Chat Message form
class CreateChatMessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ('chat_room', 'sender', 'content')
