from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from apps.account.mixins import AccessRequiredMixin, UserAccessEnum
from apps.core.utils import validate_form, amit_first_char
from .models import DietProgram, ExerciseProgram
from . import forms


# Render ProgramCategories view
class ProgramCategoriesView(AccessRequiredMixin, TemplateView):
    template_name = 'program/admin/categories.html'
    roles = [UserAccessEnum.ADMIN, UserAccessEnum.OPERATOR]


# Render DietProgramList view
class DietProgramListView(AccessRequiredMixin, ListView):
    template_name = 'program/admin/diet-list.html'
    model = DietProgram
    roles = [UserAccessEnum.ADMIN, UserAccessEnum.DIET_OP]

    def filter(self, objects):
        q = self.request.GET.get('q')
        if q:
            q = amit_first_char(q)
            objects = objects.filter(Q(id=q) | Q(user__phone_number__contains=q))
        return objects

    def get_queryset(self):
        objects = DietProgram.objects.filter(is_active=True)
        return self.filter(objects)


# Render ExerciseProgramList view
class ExerciseProgramListView(AccessRequiredMixin, ListView):
    template_name = 'program/admin/exercise-list.html'
    model = ExerciseProgram
    roles = [UserAccessEnum.ADMIN, UserAccessEnum.WORKOUT_OP]

    def filter(self, objects):
        q = self.request.GET.get('q')
        if q:
            q = amit_first_char(q)
            objects = objects.filter(Q(id=q) | Q(user__phone_number__contains=q))
        return objects

    def get_queryset(self):
        objects = ExerciseProgram.objects.filter(is_active=True)
        return objects


# Render ProgramsList view
class ProgramsListView(LoginRequiredMixin, TemplateView):
    template_name = 'program/list.html'

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        contexts['diet_programs'] = DietProgram.objects.filter(is_active=True, user=self.request.user)
        contexts['exercise_programs'] = ExerciseProgram.objects.filter(is_active=True, user=self.request.user)

        return contexts


# Add Program view
class AddProgramView(LoginRequiredMixin, CreateView):
    template_name = 'program/list.html'
    success_url = reverse_lazy('program:list')

    def get_form_class(self, form_class=None):
        program_type = self.request.POST.get('program_type')
        if program_type == 'diet':
            form = forms.AddDietProgramForm
        else:
            form = forms.AddExerciseProgramForm

        return form

    def form_valid(self, form):
        messages.success(self.request, _('Request successfully sent'))
        return super().form_valid(form)


# Render DietProgramDetails view
class DietProgramDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'program/diet-details.html'
    model = DietProgram

    def post(self, request, pk):
        data = request.POST.copy()
        instance = get_object_or_404(DietProgram, pk=pk)

        form = forms.UpdateDietProgramForm(data=data, instance=instance)
        if validate_form(request, form):
            obj = form.save(commit=False)
            obj.status = DietProgram.StatusEnum.DEFINED
            obj.save()

            messages.success(request, _('Program successfully saved'))
            return redirect('program:diet_details', pk)

        return redirect('program:diet_details', pk)


# Render ExerciseProgramDetails view
class ExerciseProgramDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'program/exercise-details.html'
    model = ExerciseProgram

    def post(self, request, pk):
        data = request.POST.copy()
        instance = get_object_or_404(ExerciseProgram, pk=pk)

        form = forms.UpdateExerciseProgramForm(data=data, instance=instance)
        if validate_form(request, form):
            obj = form.save(commit=False)
            obj.status = ExerciseProgram.StatusEnum.DEFINED
            obj.save()

            messages.success(request, _('Program successfully saved'))
            return redirect('program:exercise_details', pk)

        return redirect('program:exercise_details', pk)
    