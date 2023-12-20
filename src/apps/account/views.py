from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.contrib.auth import login, get_user_model
from django.utils.translation import gettext as _
from django.shortcuts import reverse
from django.contrib import messages

from apps.core.utils import validate_form
from .mixins import LogoutRequiredMixin
from . import forms


User = get_user_model()


# Render Login view
class LoginView(LogoutRequiredMixin, TemplateView):
    template_name = 'account/login.html'

    def post(self, request):
        data = request.POST.copy()

        form = forms.LoginForm(data=data)
        if validate_form(request, form):
            user = form.cleaned_data
            login(request, user=user)

            # Modify login session if remember me is not checked
            remember_me = data.get('remember_me', False)
            if not remember_me:
                self.request.session.set_expiry(0)
                self.request.session.modified = True

            messages.success(request, _('Login successful.'))
            return redirect('public:index')

        return redirect('account:login')


# Render Register view
class RegisterView(LogoutRequiredMixin, View):

    def post(self, request):
        data = request.POST.copy()

        form = forms.UserCreationForm(data=data)
        if validate_form(request, form):
            user = form.save()
            # TODO: Login user and redirect to verify phone

            messages.success(request, _('Login successful.'))
            return redirect('/')

        return redirect('account:login')


# Render CompleteProfile view
class CompleteProfileView(TemplateView):
    template_name = 'account/complete-profile.html'


# Render Profile view
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'


# Render Profile Detail view
class ProfileDetailView(LoginRequiredMixin, View):
    template_name = 'account/profile-detail.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)

        return render(request, 'account/profile-detail.html', context={'user': user})

    def post(self, request, pk):
        data = request.POST.copy()
        instance = get_object_or_404(User, pk=pk).user_profile

        form = forms.UpdateProfileForm(data=data, instance=instance, files=request.FILES)
        if validate_form(request, form):
            form.save()

            messages.success(request, _('Profile saved successfully'))

        return redirect(reverse('account:profile_details', args=[pk]))


# Edit User Pass view
class EditUserPassView(LoginRequiredMixin, View):

    def post(self, request):
        data = request.POST
        user = request.user

        if user.check_password(data.get('password1')):
            user.set_password(data.get('password2'))
            user.save()

            messages.success(request, _('Password updated successfully'))
            return redirect(reverse('account:profile_details', args=[user.id]))

        messages.error(request, _('Password is wrong!'))
        return redirect(reverse('account:profile_details', args=[user.id]))
