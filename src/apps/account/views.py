from django.views.generic import View, TemplateView, ListView, DetailView
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Q

from .mixins import LogoutRequiredMixin, PermissionMixin, AccessRequiredMixin
from apps.core.utils import validate_form, amit_first_char
from apps.notification.models import Notification
from .models import Access, User
from .enums import AccessChoices
from random import randint
from . import forms


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

            return redirect('account:send_verify_code')

        return redirect('account:complete_profile')


# SendCode view
class SendCodeView(View):
    def get_redirect_url(self):
        next_url = self.request.GET.get('next', reverse('account:verify_phone'))
        return next_url

    def get(self, request):
        code = randint(10000, 99999)
        request.session['verify_code'] = code

        token = request.session.get('register_token')
        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            messages.error(request, _('There is an issue! please try again'))
            return redirect('account:login')

        Notification.objects.create(
            type=Notification.TYPES.MOBILE_VERIFICATION_CODE,
            title=_('Phone number verification code'),
            kwargs={'code': code},
            to_user=user,
            send_notify=False,
        )

        print(code)
        messages.success(request, _('Code sent to you'))
        return redirect(self.get_redirect_url())


# Render VerifyPhoneNumber view
class VerifyPhoneNumberView(LogoutRequiredMixin, TemplateView):
    template_name = 'account/verify-phone.html'

    def post(self, request):
        data = {
            'user_code': int(request.POST.get('code')),
            'code': request.session.get('verify_code')
        }

        form = forms.VerifyCodeForm(data=data)
        if validate_form(request, form):
            return redirect('account:complete_register')

        return redirect('account:verify_phone')


# Complete RegisterView
class CompleteRegisterView(LogoutRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        http_referer = request.META.get('HTTP_REFERER')
        print(http_referer)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        token = request.session.get('register_token')

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

        messages.success(self.request, _('Register done successful'))
        return redirect('public:index')


# Render GetPhoneNumber view
class GetPhoneNumberView(LogoutRequiredMixin, TemplateView):
    template_name = 'account/password/get-phone.html'

    def post(self, request):
        data = request.POST.copy()

        form = forms.GetPhoneNumberForm(data=data)
        if validate_form(request, form):
            user = form.cleaned_data.get('user')

            # Generate token for registration
            token = user.generate_token()
            request.session['register_token'] = token

            return redirect(reverse('account:send_verify_code') + f'?next={reverse("account:reset_password_verify")}')

        return redirect('account:get_phone_number')


# Render ResetPasswordVerify view
class ResetPasswordVerifyView(LogoutRequiredMixin, TemplateView):
    template_name = 'account/password/verify-phone.html'

    def post(self, request):
        data = {
            'user_code': int(request.POST.get('code')),
            'code': request.session.get('verify_code')
        }

        form = forms.VerifyCodeForm(data=data)
        if validate_form(request, form):
            return redirect('account:reset_password_confirm')

        return redirect('account:reset_password_verify')


# Render ResetPasswordConfirm view
class ResetPasswordConfirmView(LogoutRequiredMixin, TemplateView):
    template_name = 'account/password/reset-pass.html'

    def post(self, request):
        data = request.POST.copy()

        form = forms.ResetPasswordForm(data=data)
        if validate_form(request, form):
            password = form.cleaned_data.get('password2')
            token = request.session.get('register_token')

            # Get user and set new password
            try:
                user = User.objects.get(token=token)
                user.set_password(password)
                user.save()
            except User.DoesNotExist:
                messages.error(request, _('There is an issue! please try again'))
                return redirect('account:login')

            user.clear_token(request)

            # Redirect to login page
            messages.success(request, _('Password changed successfully'))
            return redirect('account:login')

        return redirect('account:reset_password_confirm')


# Render Profile view
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'


# Render Profile Detail view
class ProfileDetailView(PermissionMixin, DetailView):
    template_name = 'account/admin/profile-detail.html'
    model = User
    context_object_name = 'object'

    def get_template_names(self):
        if self.request.user == self.object:
            return 'account/profile-detail.html'
        return super().get_template_names()


# Update Profile View
class UpdateProfileView(LoginRequiredMixin, View):

    def admin_update(self, data, obj):
        # Get selected access and set them for user
        selected_access = data.getlist('access')
        accesses = Access.objects.filter(title__in=selected_access)
        obj.user.access.set(accesses)

    def post(self, request):
        data = request.POST.copy()
        pk = data.get('pk')
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
    template_name = 'account/admin/users-list.html'
    model = User
    # TODO: Add pagination
    roles = [AccessChoices.ADMIN, AccessChoices.DIET_OP, AccessChoices.WORKOUT_OP]

    def filter(self, objects):
        q = self.request.GET.get('q')
        if q:
            q = amit_first_char(q)
            objects = objects.filter(Q(phone_number__contains=q) | Q(last_name__icontains=q))

        return objects

    def get_queryset(self):
        objects = User.objects.exclude(access__title=AccessChoices.ADMIN)
        return self.filter(objects)
