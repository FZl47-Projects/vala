from django.views.generic import TemplateView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages

from apps.account.mixins import AccessRequiredMixin
from .models import Ticket


# Render TicketsListView
class TicketsListView(LoginRequiredMixin, TemplateView):
    template_name = 'communication/tickets/ticket-list.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        tickets = Ticket.objects.filter(user=self.request.user, is_active=True)
        contexts['tickets'] = tickets

        return contexts


# Render AdminTicketsListView
class AdminTicketsListView(AccessRequiredMixin, TemplateView):
    template_name = 'communication/tickets/ticket-list-admin.html'
    roles = ['admin']

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        tickets = Ticket.objects.filter(is_active=True)
        contexts['tickets'] = tickets

        return contexts

    def post(self, request):
        data = request.POST.copy()
        ticket = get_object_or_404(Ticket, id=data.get('id'))

        ticket.answer = data.get('answer')
        ticket.save()

        messages.success(request, _('Answer successfully added'))
        return redirect('communication:all_tickets')


# Add Ticket view
class AddTicketView(LoginRequiredMixin, CreateView):
    template_name = 'communication/tickets/ticket-list.html'
    model = Ticket
    fields = ('user', 'title', 'text')
    success_url = reverse_lazy('communication:tickets_list')

    def form_valid(self, form):
        messages.success(self.request, _('Ticket registered successfully'))
        return super().form_valid(form)
