from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
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


# ChatRooms model
class ChatRoom(BaseModel):
    participants = models.ManyToManyField(User, related_name='chat_rooms', verbose_name=_('Participants'))
    title = models.CharField(_('Title'), max_length=255, default=_('No title'))
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Chat room')
        verbose_name_plural = _('Chat rooms')
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('communication:chat_room', args=[self.pk])

    def get_messages(self):
        return self.messages.all()

    def get_unread_messages(self):
        return self.messages.filter(is_read=False)

    def get_participant(self):
        return self.participants.first()

    def get_date_created(self):
        return self.created_at.strftime('%Y-%m-%d')


# ChatMessages model
class Message(BaseModel):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages', verbose_name=_('Chat room'))
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='chat_messages', null=True, blank=True, verbose_name=_('Sender'))
    content = models.TextField(_('Content'))
    is_read = models.BooleanField(_('Is read'), default=False)

    class Meta:
        verbose_name = _('Chat message')
        verbose_name_plural = _('Chat messages')
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.chat_room} - {self.sender} - {self.created_at}'
