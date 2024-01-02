from django.views.generic import View, TemplateView, ListView, DetailView
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, get_user_model
from django.utils.translation import gettext as _
from django.contrib import messages

from .mixins import LogoutRequiredMixin, PermissionMixin, AccessRequiredMixin
from apps.notification.models import Notification
from apps.core.utils import validate_form
from .enums import AccessChoices
from random import randint
from .models import Access
from . import forms


User = get_user_model()


# Render Login view
class LoginView(LogoutRequiredMixin, TemplateView):
    template_name = 'account/login.html'

    def post(self, request):
        data = request.POST.copy()

        form = forms.LoginForm(data=data)
        if validate_form(request, form):
            user = form.cleaned_data.get('user')

            # Redirect to phone verification if user is not verified
            if not user.is_verified:
                # Generate token for registration
                token = user.generate_token()
                request.session['register_token'] = token

                messages.info(request, _('Please Complete your profile'))
                return redirect('account:complete_profile')

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

            # Generate token for registration
            token = user.generate_token()
            request.session['register_token'] = token

            messages.info(request, _('Please Complete your profile'))
            return redirect('account:complete_profile')

        return redirect('account:login')


# Render CompleteProfile view
class CompleteProfileView(LogoutRequiredMixin, TemplateView):
    template_name = 'account/complete-profile.html'

    def post(self, request):
        data = request.POST.copy()
        token = request.session.get('register_token')

        instance = get_object_or_404(User, token=token).user_profile

        form = forms.AddProfileForm(data=data, instance=instance, files=request.FILES)
        if validate_form(request, form):
            form.save()

            messages.success(request, _('Code sent to you'))
            return redirect('account:send_verify_code')

        return redirect('account:complete_profile')


# SendCode view
class SendCodeView(View):
    def get(self, request):
        code = randint(10000, 99999)
        request.session['verify_code'] = code

        token = request.session.get('register_token')
        user = get_object_or_404(User, token=token)

        Notification.objects.create(
            type=Notification.TYPES.MOBILE_VERIFICATION_CODE,
            title=_('Phone number verification code'),
            kwargs={'code': code},
            to_user=user,
        )

        return redirect('account:verify_phone')


# Render VerifyPhoneNumber view
class VerifyPhoneNumberView(LogoutRequiredMixin, TemplateView):
    template_name = 'account/verify-phone.html'

    def post(self, request):
        data = int(request.POST.get('code'))
        code = request.session.get('verify_code')
        token = request.session.get('register_token')

        if code != data:
            messages.error(request, _('Entered code is not correct'))
            return redirect('account:verify_phone')

        try:
            user = User.objects.get(token=token)
            user.is_verified = True
            user.clear_token(request)
        except User.DoesNotExist:
            messages.error(request, _('Please try again'))

            return redirect('account:login')

        # Login user
        login(request, user)

        # Delete verification code from sessions
        if 'verify_code' in request.session:
            del request.session['verify_code']

        messages.success(request, _('Register done successful'))
        return redirect('public:index')


# Render Profile view
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'


# Render Profile Detail view
class ProfileDetailView(PermissionMixin, DetailView):
    template_name = 'account/admin/profile-detail.html'
    model = User
    context_object_name = 'user'

    def admin_update(self, data, obj):
        # Get selected access and set them for user
        selected_access = data.getlist('access')
        accesses = Access.objects.filter(title__in=selected_access)
        obj.user.access.set(accesses)

    def get_template_names(self):
        if self.request.user == self.object:
            return 'account/profile-detail.html'
        return super().get_template_names()

    def post(self, request, pk):
        data = request.POST.copy()
        instance = get_object_or_404(User, pk=pk).user_profile

        form = forms.UpdateProfileForm(data=data, instance=instance, files=request.FILES)
        if validate_form(request, form):
            obj = form.save()

            # Do some stuff of editor is not own user
            if request.user.user_profile != obj:
                self.admin_update(data, obj)

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


# Render UsersList view
class UsersListView(AccessRequiredMixin, ListView):
    template_name = 'account/admin/list.html'
    model = User
    # TODO: Add pagination
    roles = [AccessChoices.ADMIN, AccessChoices.DIET_OP, AccessChoices.WORKOUT_OP]

    def get_queryset(self):
        return super().get_queryset()
        # TODO: Add filters and search
