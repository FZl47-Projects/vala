from django.shortcuts import redirect


class LogoutRequiredMixin:
    """ Allows access only to unauthenticated users. """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        return redirect("public:index")


class ProfileCompletionMixin:
    """ Allow access only to users those completed profile info. """

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.user_profile.is_verified:
            return redirect('account:complete_profile')

        return super().dispatch(request, *args, **kwargs)
