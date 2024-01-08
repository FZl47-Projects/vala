from django.views.generic import ListView, CreateView, View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages

from apps.account.mixins import AccessRequiredMixin, UserAccessEnum
from .models import Product, OrderRequest
from . import forms


# Render ProductsList view
class ProductListView(ListView):
    template_name = 'shop/products.html'
    model = Product

    def get_template_names(self):
        if self.request.user.has_admin_access:
            return 'shop/admin/products.html'
        return super().get_template_names()

    def get_queryset(self):
        objects = Product.objects.filter(is_active=True)
        return objects


# Add Product View
class AddProductView(AccessRequiredMixin, CreateView):
    template_name = 'shop/admin/products.html'
    form_class = forms.AddProductForm
    success_url = reverse_lazy('shop:product_list')
    roles = [UserAccessEnum.ADMIN]

    def form_valid(self, form):
        messages.success(self.request, _('Product successfully added'))
        return super().form_valid(form)


# Delete Product view
class DeleteProductView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def get(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        obj.is_active = False
        obj.save()

        messages.success(request, _('Product successfully deleted'))
        return redirect('shop:product_list')


# Render AddOrderRequest view
class AddOrderRequestView(LoginRequiredMixin, CreateView):
    template_name = 'shop/products.html'
    model = OrderRequest
    form_class = forms.AddOrderRequestForm
    success_url = reverse_lazy('shop:product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, _('Your request successfully sent and You will be contacted as soon as possible'))
        return super().form_valid(form)


# Render OrderRequestsList view
class OrderRequestsListView(AccessRequiredMixin, ListView):
    template_name = 'shop/admin/order-requests.html'
    model = OrderRequest
    roles = [UserAccessEnum.ADMIN]


# Set OrderRequestStatusView
class SetOrderRequestStatusView(AccessRequiredMixin, View):
    roles = [UserAccessEnum.ADMIN]

    def get(self, request, pk):
        try:
            obj = OrderRequest.objects.get(pk=pk)
            obj.delivered = not obj.delivered
            obj.save()
        except OrderRequest.DoesNotExist:
            return JsonResponse({'response': 'error'}, status=400)

        return JsonResponse({'response': 'ok'}, status=200)
