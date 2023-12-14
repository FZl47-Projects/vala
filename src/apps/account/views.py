from django.views.generic import View, TemplateView
from django.utils.translation import gettext as _
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages

from apps.core.utils import validate_form
from . import forms


# Render Login view
class LoginView(TemplateView):
    template_name = 'account/login.html'

    def post(self, request):
        data = request.POST.copy()

        form = forms.LoginForm(data=data)
        if validate_form(request, form):
            user = form.cleaned_data
            login(request, user=user)

            messages.success(request, _('Login successful.'))
            return redirect('/')

        return redirect('account:login')


# Render Register view
class RegisterView(View):

    def post(self, request):
        data = request.POST.copy()

        form = forms.UserCreationForm(data=data)
        if validate_form(request, form):
            user = form.save()
            # TODO: Login user and redirect to verify phone

            messages.success(request, _('Login successful.'))
            return redirect('/')

        return redirect('account:login')
