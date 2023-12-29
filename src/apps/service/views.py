from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from apps.account.mixins import AccessRequiredMixin
from apps.core.utils import validate_form
from apps.account.enums import AccessLevelsEnum
from . import models
from . import forms


class OperatorCategoryListView(TemplateView):
    template_name = 'service/operator/category/list.html'

    def get_context_data(self, **kwargs):
        context = super(OperatorCategoryListView, self).get_context_data(**kwargs)
        context.update({
            'categories': models.OperatorCategory.objects.all()
        })
        return context


class OperatorCategoryDetailView(View):

    def get(self, request, category_id):
        context = {
            'category': get_object_or_404(models.OperatorCategory, id=category_id)
        }
        return render(request, 'service/operator/category/detail.html', context)


class OperatorCategoryAddView(AccessRequiredMixin, View):
    roles = (AccessLevelsEnum.ADMIN,)

    def post(self, request):
        data = request.POST
        f = forms.OperatorCategoryAdd(data)
        if validate_form(request, f) is False:
            return redirect('service:operator_category__list')
        category = f.save()
        messages.success(request, _('Category Created Successfully'))
        return redirect('service:operator_category__list')


class OperatorCategoryDeleteView(AccessRequiredMixin, View):
    roles = (AccessLevelsEnum.ADMIN,)

    def post(self, request, category_id=0):
        """
            if category_id is 0 then get category in request data
        """
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
        f = forms.OperatorAdd(data, files=request.FILES)
        if validate_form(request, f) is False:
            return redirect(referer_url)
        operator = f.save()
        messages.success(request, _('Operator Created Successfully'))
        return redirect(referer_url)


class OperatorDeleteView(AccessRequiredMixin, View):
    roles = (AccessLevelsEnum.ADMIN,)

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
        context.update({

        })
        return context
