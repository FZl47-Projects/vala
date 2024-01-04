from django.views.generic import View, TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from apps.account.mixins import AccessRequiredMixin
from apps.account.enums import AccessChoices
from apps.core.utils import amit_first_char
from .. import models
from .. import forms


# Render CounselingsList view
class CounselingsListView(LoginRequiredMixin, ListView):
    template_name = 'operation/counselings/list.html'
    model = models.Counseling

    def get_template_names(self):
        if self.request.user.has_admin_access:
            return 'operation/counselings/admin/list.html'
        return super().get_template_names()

    def filter(self, objects):
        q = self.request.GET.get('q')
        if q:
            q = amit_first_char(q)
            objects = objects.filter(Q(user__phone_numbe__contains=q) | Q(user__last_name__icontains=q))

        return objects

    def get_queryset(self):
        if self.request.user.has_admin_access:
            objects = models.Counseling.objects.filter(is_active=True)
            return self.filter(objects)

        return models.Counseling.objects.filter(is_active=True, user=self.request.user)


# Add Counseling view
class AddCounselingView(LoginRequiredMixin, CreateView):
    template_name = 'operation/counselings/list.html'
    model = models.Counseling
    form_class = forms.AddCounselingForm
    success_url = reverse_lazy('operation:counselings_list')

    def form_valid(self, form):
        messages.success(self.request, _('Counseling request registered successfully'))
        return super().form_valid(form)


# Toggle Counseling answer view
class ToggleCounselingAnswerView(AccessRequiredMixin, View):
    roles = [AccessChoices.ADMIN]

    def get(self, request, pk):
        try:
            obj = models.Counseling.objects.get(pk=pk)
            obj.is_answered = not obj.is_answered
            obj.save()
        except models.Counseling.DoesNotExist:
            return JsonResponse({'response': 'error'}, status=404)

        return JsonResponse({'response': 'answered'}, status=200)
