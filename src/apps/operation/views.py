from django.views.generic import View, TemplateView, CreateView, DetailView
from django.shortcuts import redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages

from apps.account.mixins import AccessRequiredMixin
from apps.notification.models import Notification
from apps.account.models import User
from . import models


# Render Tests view
class TestsView(LoginRequiredMixin, TemplateView):
    template_name = 'operation/tests/tests.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)

        if self.request.user.has_admin_access:
            tests = models.Test.objects.filter(is_active=True)
        else:
            tests = models.Test.objects.filter(is_active=True, user=self.request.user)

        contexts['tests'] = tests
        return contexts


# Render TestDetails view
class TestDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'operation/tests/test-details.html'
    model = models.Test

    def post(self, request, pk):
        data = request.POST.copy()
        test = get_object_or_404(models.Test, pk=data.get('pk'))

        test.answer = data.get('answer')
        test.status = test.State.ANSWERED
        test.save()

        messages.success(request, _('The answer successfully registered'))

        # TODO: Send sms for user to see the answer
        return redirect('operation:test_details', pk=test.pk)


# Add Test view
class AddTestView(LoginRequiredMixin, CreateView):
    template_name = 'operation/tests/tests.html'
    success_url = reverse_lazy('operation:tests_list')
    model = models.Test
    fields = ('user', 'title', 'text', 'file')

    def form_valid(self, form):
        obj = form.save(commit=False)

        # Check if user saved more than unanswered test
        test_counts = models.Test.objects.filter(is_active=True, user=obj.user, status='await').count()
        if test_counts >= 3:
            messages.error(self.request, _('You cannot register more than 3 unanswered test'))
            return redirect('operation:tests_list')

        obj.save()

        messages.success(self.request, _('Test added successfully'))
        return super().form_valid(form)


# Render RecoveryProcesses view
class RecoveryProcessesView(LoginRequiredMixin, TemplateView):
    template_name = 'operation/recovery/processes-list.html'
    
    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        processes = models.RecoveryProcess.objects.filter(is_active=True, user=self.request.user)
        contexts['processes'] = processes

        return contexts


# Add RecoveryProcess view
class AddRecoveryProcessView(LoginRequiredMixin, CreateView):
    template_name = 'operation/recovery/processes-list.html'
    success_url = reverse_lazy('operation:recoveries_list')
    model = models.RecoveryProcess
    fields = ('user', 'title')
    
    def form_valid(self, form):
        messages.success(self.request, _('Recovery process added successfully'))
        return super().form_valid(form)


# Delete RecoveryProcess view
class DeleteRecoveryProcessView(LoginRequiredMixin, View):

    def get(self, request, pk):
        obj = get_object_or_404(models.RecoveryProcess, pk=pk)
        obj.is_active = False
        obj.save()

        messages.success(request, _('Recovery process deleted successfully'))
        return redirect('operation:recoveries_list')


# Render RecoveryProcessDetails view
class RecoveryProcessDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'operation/recovery/process-details.html'
    model = models.RecoveryProcess


# Add RecoveryProcessImage view
class AddRecoveryProcessImageView(LoginRequiredMixin, CreateView):
    template_name = 'operation/recovery/process-details.html'
    model = models.RecoveryProcessImage
    fields = ('recovery_process', 'image')

    def form_valid(self, form):
        messages.success(self.request, _('Image added successfully'))
        return super().form_valid(form)


# Delete RecoveryProcessImage view
class DeleteRecoveryProcessImageView(LoginRequiredMixin, View):

    def post(self, request):
        data = request.POST.copy()
        obj = get_object_or_404(models.RecoveryProcessImage, pk=data.get('pk'))

        parent_pk = obj.recovery_process.pk
        obj.delete()

        messages.success(self.request, _('Image deleted successfully'))
        return redirect('operation:recovery_process_details', parent_pk)
