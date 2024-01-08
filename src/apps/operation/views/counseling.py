from django.views.generic import View, TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from apps.account.mixins import AccessRequiredMixin
from apps.account.enums import UserAccessEnum
from apps.core.utils import remove_first_char
from ..models import Counseling
from .. import forms


# Render CounselingsList view
class CounselingsListView(LoginRequiredMixin, ListView):
    template_name = 'operation/counselings/list.html'
    model = Counseling

    def get_template_names(self):
        if self.request.user.has_admin_access:
            return 'operation/counselings/admin/list.html'
        return super().get_template_names()

    def filter(self, objects):
        q = self.request.GET.get('q')
        if q:
            q = remove_first_char(q)
            objects = objects.filter(Q(user__phone_number__contains=q) | Q(user__last_name__icontains=q))

        return objects

    def get_queryset(self):
        if self.request.user.has_admin_access:
            objects = Counseling.objects.filter(is_active=True)
            return self.filter(objects)

        return Counseling.objects.filter(is_active=True, user=self.request.user)


# Add Counseling view
class AddCounselingView(LoginRequiredMixin, CreateView):
    template_name = 'operation/counselings/list.html'
    model = Counseling
    form_class = forms.AddCounselingForm
    success_url = reverse_lazy('operation:counselings_list')

    def form_valid(self, form):
        messages.success(self.request, _('Counseling request registered successfully'))
        return super().form_valid(form)


# Toggle Counseling answer view
class ToggleCounselingAnswerView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def get(self, request, pk):
        try:
            obj = Counseling.objects.get(pk=pk)
            obj.is_answered = not obj.is_answered
            obj.save()
        except Counseling.DoesNotExist:
            return JsonResponse({'response': 'error'}, status=404)

        return JsonResponse({'response': 'answered'}, status=200)
