from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages

from . import forms


# Render Login view
class LoginView(TemplateView):
    template_name = 'account/login.html'

    def post(self, request):
        data = request.POST.copy()

        form = forms.LoginForm(data=data)
        if form.is_valid():
            user = form.cleaned_data
            login(request, user=user)

            messages.success(request, _('Login successful.'))
            return redirect('/')

        # Send error messages
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, error)

        return redirect('account:login')
