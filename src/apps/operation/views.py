from django.views.generic import View, TemplateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages

from apps.account.mixins import AccessRequiredMixin
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
