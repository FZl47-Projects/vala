from django.shortcuts import redirect


class LogoutRequiredMixin:
    """ Allows access only to unauthenticated users. """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        return redirect("public:index")
