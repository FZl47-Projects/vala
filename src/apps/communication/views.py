from django.views.generic import TemplateView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Ticket


# Render TicketsListView
class TicketListView(LoginRequiredMixin, TemplateView):
    template_name = 'communication/tickets/ticket-list.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        contexts['tickets'] = Ticket.objects.filter(user=self.request.user, is_active=True)

        return contexts


# Add Ticket view
class AddTicketView(LoginRequiredMixin, CreateView):
    template_name = 'communication/tickets/ticket-list.html'
    model = Ticket
    fields = ('user', 'title', 'text')
    success_url = reverse_lazy('communication:tickets_list')

    def form_valid(self, form):
        messages.success(self.request, _('Ticket registered successfully'))
        return super().form_valid(form)
