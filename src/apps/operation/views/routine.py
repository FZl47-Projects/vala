from django.views.generic import View, UpdateView, CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages

from apps.account.mixins import AccessRequiredMixin
from apps.account.enums import UserAccessEnum
from ..models import SkinRoutine
from .. import forms


# Render Routines view
class RoutinesView(LoginRequiredMixin, ListView):
    template_name = 'operation/routines/routines.html'
    model = SkinRoutine

    def get_template_names(self):
        if self.request.user.has_admin_access:
            return 'operation/routines/admin/routines.html'
        return super().get_template_names()

    def get_queryset(self):
        if self.request.user.has_admin_access:
            objects = SkinRoutine.objects.filter(is_active=True)
            return objects

        return SkinRoutine.objects.filter(is_active=True, user=self.request.user)


# Render RoutineDetails view
class RoutineDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'operation/routines/details.html'
    model = SkinRoutine


# Add Routine view
class AddRoutineView(LoginRequiredMixin, CreateView):
    template_name = 'operation/routines/add.html'
    model = SkinRoutine
    form_class = forms.AddSkinRoutineForm
    success_url = reverse_lazy('operation:routines_list')

    def form_valid(self, form):
        messages.success(self.request, _('Routine registered successfully'))
        return super().form_valid(form)


# Answer Routine view
class AnswerRoutineView(AccessRequiredMixin, UpdateView):
    template_name = 'operation/routines/details.html'
    model = SkinRoutine
    form_class = forms.AnswerRoutineForm
    roles = [UserAccessEnum.ADMIN]

    def get_success_url(self):
        return reverse('operation:routine_details', args=[self.object.pk])

    def form_valid(self, form):
        messages.success(self.request, _('Answer successfully added'))
        return super().form_valid(form)


# Delete Routine view
class DeleteRoutineView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def get(self, request, pk):
        try:
            obj = SkinRoutine.objects.get(pk=pk)
            obj.is_active = False
            obj.save()
        except SkinRoutine.DoesNotExist:
            messages.error(request, _('There is an issue'))
            return redirect('operation:routines_list')

        messages.success(request, _('Routine successfully deleted'))
        return redirect('operation:routines_list')
