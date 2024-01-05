from django.views.generic import TemplateView, CreateView, View, ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from apps.account.mixins import AccessRequiredMixin, UserAccessEnum
from apps.core.utils import amit_first_char
from . import models
from . import forms


# Render TicketsListView
class TicketsListView(LoginRequiredMixin, TemplateView):
    template_name = 'communication/tickets/tickets.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        tickets = models.Ticket.objects.filter(user=self.request.user, is_active=True)
        contexts['tickets'] = tickets

        return contexts


# Render AdminTicketsListView
class AdminTicketsListView(AccessRequiredMixin, TemplateView):
    template_name = 'communication/tickets/tickets-admin.html'
    roles = [UserAccessEnum.ADMIN]

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        tickets = models.Ticket.objects.filter(is_active=True)
        contexts['tickets'] = tickets

        return contexts

    def post(self, request):
        data = request.POST.copy()
        ticket = get_object_or_404(models.Ticket, id=data.get('id'))

        ticket.answer = data.get('answer')
        ticket.save()

        messages.success(request, _('Answer successfully added'))
        return redirect('communication:all_tickets')


# Add Ticket view
class AddTicketView(LoginRequiredMixin, CreateView):
    template_name = 'communication/tickets/tickets.html'
    model = models.Ticket
    fields = ('user', 'title', 'text')
    success_url = reverse_lazy('communication:tickets_list')

    def form_valid(self, form):
        messages.success(self.request, _('Ticket registered successfully'))
        return super().form_valid(form)


# Render ChatList view
class ChatListView(LoginRequiredMixin, ListView):
    template_name = 'communication/chat/chat-list.html'
    model = models.ChatRoom

    def get_template_names(self):
        if self.request.user.has_admin_access:
            return 'communication/chat/admin/chat-list.html'
        return super().get_template_names()

    def filter(self, objects):
        q = self.request.GET.get('q')
        if q:
            q = amit_first_char(q)
            objects = objects.filter(Q(id=q) | Q(participants__phone_number__contains=q))

        return objects

    def get_queryset(self):
        if self.request.user.has_admin_access:
            objects = models.ChatRoom.objects.filter(is_active=True)
            return self.filter(objects)

        objects = models.ChatRoom.objects.filter(is_active=True, participants=self.request.user)
        return self.filter(objects)


# Render ChatRoom view
class ChatRoomView(LoginRequiredMixin, DetailView):
    template_name = 'communication/chat/chat-room.html'
    model = models.ChatRoom

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        chat_room = get_object_or_404(models.ChatRoom, pk=pk)
        chat_room.messages.update(is_read=True)

        return super().dispatch(request, *args, **kwargs)
    
    def get_template_names(self):
        if self.request.user.has_admin_access:
            return 'communication/chat/admin/chat-room.html'
        return super().get_template_names()


# Create ChatRoom view
class CreateChatRoomView(LoginRequiredMixin, View):

    def get(self, request):
        # Check if user created more than 1 chat rooms
        if models.ChatRoom.objects.filter(is_active=True, participants=request.user).count() >= 1:
            messages.error(request, _('You cannot create more than 1 active chat room'))
            return redirect('communication:chats_list')

        # Create chatroom and set the current user as participant
        obj = models.ChatRoom.objects.create()
        obj.participants.add(request.user)
        obj.save()

        return redirect('communication:chat_room', obj.pk)


# SendMessage view
class SendMessageView(LoginRequiredMixin, CreateView):
    template_name = 'communication/chat/chat-room.html'
    model = models.Message
    form_class = forms.CreateChatMessageForm

    def get_success_url(self):
        pk = self.request.POST.get('chat_room')
        return reverse('communication:chat_room', args=[pk])
