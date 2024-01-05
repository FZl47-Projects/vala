from django.views.generic import ListView, CreateView
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from apps.account.mixins import AccessRequiredMixin, UserAccessEnum
from .models import Product
from . import forms


# Render ProductsList view
class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'shop/products.html'
    model = Product

    def get_template_names(self):
        if self.request.user.has_admin_access:
            return 'shop/admin/products.html'
        return super().get_template_names()
