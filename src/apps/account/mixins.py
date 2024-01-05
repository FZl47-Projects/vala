from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q

from .enums import UserAccessEnum
from .models import UserProfile
from functools import reduce

User = get_user_model()


class LogoutRequiredMixin:
    """ Allows access only to unauthenticated users. """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        return redirect("public:index")


class AccessRequiredMixin:
    """ Allow access only to given roles. """
    roles = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('account:login')

        q = reduce(lambda x, y: x | y, [Q(title__contains=role) for role in self.roles])
        if request.user.access.filter(q).exists():
            return super().dispatch(request, *args, **kwargs)

        messages.error(request, _('You do not have permission to access this page!'))
        return HttpResponseForbidden()


class VIPRequiredMixin:
    """ Allow access only to VIP users. """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('account:login')

        if request.user.user_profile.level == UserProfile.LEVELS.VIP:
            return super().dispatch(request, *args, **kwargs)

        messages.error(request, _('You do not have permission to access this page!'))

        http_referer = request.META.get('HTTP_REFERER')
        return redirect(http_referer)


class ProfileCompletionMixin:
    """ Allow access only to users those completed profile info. """

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.user_profile.is_verified:
            return redirect('account:complete_profile')

        return super().dispatch(request, *args, **kwargs)


class PermissionMixin:
    """ Limit access permission to the view. """

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        
        try:
            obj = User.objects.get(pk=pk)
        except User.DoesNotExist:
            obj = None

        if request.user.is_anonymous:
            return redirect('account:login')
        elif request.user.access.filter(title__in=User.OP_ROLES).exists() or request.user == obj:
            return super().dispatch(request, *args, **kwargs)

        return redirect('account:profile')
