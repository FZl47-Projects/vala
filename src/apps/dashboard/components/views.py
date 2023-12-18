from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, TemplateDoesNotExist
from django.views.generic import View, TemplateView
from apps.account.auth.mixins import LoginRequiredMixinCustom
from apps.account.models import User


class BaseComponentView:
    BASE_DIR_TEMPLATE_COMPONENTS = 'dashboard/components'
    USER_ROLES = User.ALL_USER_ROLES
    CONTEXT_FUNC_ROLES = {
        'super_user': 'get_context_super_user',
        'operator_user': 'get_context_operator_user',
        'normal_user': 'get_context_normal_user',
    }

    template_name = None

    def get_template_by_user_role(self):
        user = self.request.user
        try:
            return loader.get_template(f"{self.BASE_DIR_TEMPLATE_COMPONENTS}/{user.role}/{self.template_name}")
        except TemplateDoesNotExist:
            try:
                return loader.get_template(f"{self.BASE_DIR_TEMPLATE_COMPONENTS}/base/{self.template_name}")
            except:
                pass
        raise FileNotFoundError(
            "template not found in component and base folder '%s' for '%s'" % (
                self.template_name, user.role))
    def get_context_by_user_role(self):
        user = self.request.user
        context_func_name = self.CONTEXT_FUNC_ROLES.get(user.role, None)
        context_callable = getattr(self, context_func_name, None)
        try:
            return context_callable()
        except NotImplementedError:
            pass
        return {}

    def get_context_super_user(self):
        raise NotImplementedError

    def get_context_operator_user(self):
        raise NotImplementedError

    def get_context_normal_user(self):
        raise NotImplementedError

    def get(self, request):
        template = self.get_template_by_user_role()
        context = self.get_context_by_user_role()
        return HttpResponse(template.render(context, request), content_type="application/xhtml+xml")


class DashboardMain(BaseComponentView, View):

    def __init__(self, *args, **kwargs):
        super(DashboardMain, self).__init__(*args, **kwargs)
        self.template_name = 'main.html'


