from django.views.generic import View, TemplateView
from apps.account.auth.mixins import LoginRequiredMixinCustom


class Index(LoginRequiredMixinCustom, TemplateView):
    template_name = 'dashboard/index.html'


