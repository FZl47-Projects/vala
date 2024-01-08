from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, ListView, View
from apps.account.mixins import AccessRequiredMixin
from apps.account.enums import UserAccessEnum
from apps.core.utils import validate_form
from django.contrib import messages
from . import models
from . import forms


class OperatorCategoryListView(ListView):
    template_name = 'service/operator/category/list.html'
    model = models.OperatorCategory
    context_object_name = 'categories'


class OperatorCategoryDetailView(View):

    def get(self, request, category_id):
        context = {
            'category': get_object_or_404(models.OperatorCategory, id=category_id)
        }
        return render(request, 'service/operator/category/detail.html', context)


class OperatorCategoryAddView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def post(self, request):
        data = request.POST

        form = forms.OperatorCategoryAdd(data)
        if validate_form(request, form) is False:
            return redirect('service:operator_category__list')
        category = form.save()

        messages.success(request, _('Category Created Successfully'))
        return redirect('service:operator_category__list')


class OperatorCategoryDeleteView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def post(self, request, category_id=0):
        """ if category_id is 0 then get category in request data """
        data = request.POST

        category_id = category_id or data.get('category', 0)
        category = get_object_or_404(models.OperatorCategory, id=category_id)
        category.delete()

        messages.success(request, _('Category Deleted Successfully'))
        return redirect('service:operator_category__list')


class OperatorAddView(View):

    def post(self, request):
        referer_url = request.META.get('HTTP_REFERER')
        data = request.POST

        form = forms.OperatorAdd(data, files=request.FILES)
        if validate_form(request, form) is False:
            return redirect(referer_url)
        operator = form.save()

        messages.success(request, _('Operator Created Successfully'))
        return redirect(referer_url)


class OperatorDeleteView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def post(self, request, operator_id):
        referer_url = request.META.get('HTTP_REFERER')
        operator = get_object_or_404(models.Operator, id=operator_id)
        operator.delete()

        messages.success(request, _('Operator Deleted Successfully'))
        return redirect(referer_url)


class OperatorDetailView(TemplateView):
    template_name = 'service/operator/detail.html'

    def get_context_data(self, **kwargs):
        context = super(OperatorDetailView, self).get_context_data(**kwargs)
        operator_id = kwargs.get('operator_id')

        context.update({
            'operator': get_object_or_404(models.Operator, id=operator_id)
        })
        return context


class OperatorWorkSampleAddView(AccessRequiredMixin, TemplateView):
    roles = [UserAccessEnum.ADMIN]

    def post(self, request):
        referer_url = request.META.get('HTTP_REFERER')
        data = request.POST

        form = forms.OperatorWorkSampleAdd(data, files=request.FILES)
        if validate_form(request, form) is False:
            return redirect(referer_url)
        form.save()

        messages.success(request, _('Work Sample Created Successfully'))
        return redirect(referer_url)


class OperatorWorkSampleDeleteView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def get(self, request, work_sample_id):
        work_sample = get_object_or_404(models.OperatorWorkSample, id=work_sample_id)
        work_sample.delete()

        messages.success(request, _('Work Sample Deleted Successfully'))
        return redirect(work_sample.operator.get_absolute_url())


class OperatorReserveAddView(View):

    def post(self, request, operator_id):
        operator = get_object_or_404(models.Operator, id=operator_id)
        data = request.POST.copy()

        # Set additional values
        data['operator'] = operator

        form = forms.OperatorReserveAdd(data)
        if validate_form(request, form) is False:
            return redirect(operator.get_absolute_url())
        form.save()

        messages.success(request, _('Operator Time Was Successfully Booked'))
        # TODO: send sms to admins
        ...
        return redirect(operator.get_absolute_url())


class OperatorReserveListView(AccessRequiredMixin, TemplateView):
    template_name = 'service/operator/reserve/list.html'
    roles = [UserAccessEnum.ADMIN]

    def get_context_data(self, **kwargs):
        context = super(OperatorReserveListView, self).get_context_data(**kwargs)

        context.update({
            'reserves': models.OperatorReserve.objects.all()
        })
        return context
