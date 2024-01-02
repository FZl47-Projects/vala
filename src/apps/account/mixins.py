from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from .enums import AccessChoices

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
        elif request.user.access.filter(title__in=self.roles).exists():
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden()


class ProfileCompletionMixin:
    """ Allow access only to users those completed profile info. """

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.user_profile.is_verified:
            return redirect('account:complete_profile')

        return super().dispatch(request, *args, **kwargs)


class PermissionMixin:
    """ Limit access permission to the view. """
    access = [AccessChoices.ADMIN, AccessChoices.WORKOUT_OP, AccessChoices.DIET_OP]

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        
        try:
            obj = User.objects.get(pk=pk)
        except User.DoesNotExist:
            obj = None

        if request.user.is_anonymous:
            return redirect('account:login')
        elif request.user.access.filter(title__in=self.access).exists() or request.user == obj:
            return super().dispatch(request, *args, **kwargs)

        return redirect('account:profile')
