from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages

from apps.account.mixins import AccessRequiredMixin
from apps.account.enums import AccessChoices
from .. import models
from .. import forms


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


# Update Test view
class UpdateTestView(AccessRequiredMixin, UpdateView):
    template_name = 'operation/tests/test-details.html'
    model = models.Test
    form_class = forms.AnswerTestForm
    roles = [AccessChoices.ADMIN]

    def get_success_url(self):
        return reverse('operation:test_details', args=[self.object.pk])

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.status = obj.State.ANSWERED
        obj.save()

        # TODO: Send sms for user to see the answer
        messages.success(self.request, _('Answer successfully added'))
        return super().form_valid(form)


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
