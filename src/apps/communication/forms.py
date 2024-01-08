from django.core.exceptions import ValidationError
from django import forms
from .models import ChatRoom, Message


# Create Chat Message form
class CreateChatMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('chat_room', 'sender', 'content')

    def clean(self):
        room = self.cleaned_data.get('chat_room')
        sender = self.cleaned_data.get('sender')

        try:
            chat_room = ChatRoom.objects.get(pk=room.pk)
            if not chat_room.participants.filter(pk=sender.pk).exists():
                raise ValidationError('An error has occurred', code='403_FORBIDDEN')
        except (ChatRoom.DoesNotExist, AttributeError):
            raise ValidationError('An error has occurred', code='403_FORBIDDEN')

        return self.cleaned_data
