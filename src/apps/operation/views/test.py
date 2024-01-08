from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from apps.account.mixins import AccessRequiredMixin
from apps.account.enums import UserAccessEnum
from apps.core.utils import remove_first_char
from ..models import Test
from .. import forms


# Render Tests view
class TestsView(LoginRequiredMixin, ListView):
    template_name = 'operation/tests/tests.html'
    model = Test
    context_object_name = 'tests'

    def filter(self, objects):
        q = self.request.GET.get('q')
        if q:
            q = remove_first_char(q)
            objects = objects.filter(Q(user__phone_number__contains=q) | Q(user__last_name__icontains=q))

        return objects

    def get_queryset(self):
        if self.request.user.has_admin_access:
            objects = Test.objects.filter(is_active=True)
            return self.filter(objects)

        return Test.objects.filter(is_active=True, user=self.request.user)


# Render TestDetails view
class TestDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'operation/tests/test-details.html'
    model = Test


# Update Test view
class UpdateTestView(AccessRequiredMixin, UpdateView):
    template_name = 'operation/tests/test-details.html'
    model = Test
    form_class = forms.AnswerTestForm
    roles = [UserAccessEnum.ADMIN]

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
    model = Test
    fields = ('user', 'title', 'text', 'file')

    def form_valid(self, form):
        obj = form.save(commit=False)

        # Check if user saved more than unanswered test
        test_counts = Test.objects.filter(is_active=True, user=obj.user, status='await').count()
        if test_counts >= 3:
            messages.error(self.request, _('You cannot register more than 3 unanswered test'))
            return redirect('operation:tests_list')

        obj.save()

        messages.success(self.request, _('Test added successfully'))
        return super().form_valid(form)
