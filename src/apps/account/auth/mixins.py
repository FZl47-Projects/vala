from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from apps.account.models import User


class LoginRequiredMixinCustom(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.is_phonenumber_confirmed:
            return redirect('account:confirm_phonenumber')
        if getattr(request.user,'profile',None) is None:
            return redirect('account:user_personal__detail')
        return super().dispatch(request, *args, **kwargs)


class SuperUserRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        role = request.user.role
        if role not in User.SUPER_USER_ROLES:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class OperatorUserRequiredMixin(LoginRequiredMixinCustom):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        role = request.user.role
        if role not in User.OPERATOR_USER_ROLES:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AdminRequiredMixin(LoginRequiredMixinCustom):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        role = request.user.role
        if role not in User.ADMIN_ROLES:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
