from django.views.generic import View, TemplateView, CreateView, DetailView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages

from ..models import RecoveryProcess, RecoveryProcessImage


# Render RecoveryProcesses view
class RecoveryProcessesView(LoginRequiredMixin, TemplateView):
    template_name = 'operation/recovery/processes-list.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        processes = RecoveryProcess.objects.filter(is_active=True, user=self.request.user)
        contexts['processes'] = processes

        return contexts


# Add RecoveryProcess view
class AddRecoveryProcessView(LoginRequiredMixin, CreateView):
    template_name = 'operation/recovery/processes-list.html'
    success_url = reverse_lazy('operation:recoveries_list')
    model = RecoveryProcess
    fields = ('user', 'title')

    def form_valid(self, form):
        messages.success(self.request, _('Recovery process added successfully'))
        return super().form_valid(form)


# Delete RecoveryProcess view
class DeleteRecoveryProcessView(LoginRequiredMixin, View):

    def get(self, request, pk):
        obj = get_object_or_404(RecoveryProcess, pk=pk)
        obj.is_active = False
        obj.save()

        messages.success(request, _('Recovery process deleted successfully'))
        return redirect('operation:recoveries_list')


# Render RecoveryProcessDetails view
class RecoveryProcessDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'operation/recovery/process-details.html'
    model = RecoveryProcess


# Add RecoveryProcessImage view
class AddRecoveryProcessImageView(LoginRequiredMixin, CreateView):
    template_name = 'operation/recovery/process-details.html'
    model = RecoveryProcessImage
    fields = ('recovery_process', 'image')

    def form_valid(self, form):
        messages.success(self.request, _('Image added successfully'))
        return super().form_valid(form)


# Delete RecoveryProcessImage view
class DeleteRecoveryProcessImageView(LoginRequiredMixin, View):

    def post(self, request):
        data = request.POST.copy()
        obj = get_object_or_404(RecoveryProcessImage, pk=data.get('pk'))

        parent_pk = obj.recovery_process.pk
        obj.delete()

        messages.success(self.request, _('Image deleted successfully'))
        return redirect('operation:recovery_process_details', parent_pk)
