from django.views.generic import View
from apps.account.models import User
from apps.core.components import BaseComponentView


class ComponentView(BaseComponentView):
    BASE_DIR_TEMPLATE_COMPONENTS = 'dashboard/components'


class DashboardMain(ComponentView, View):

    def __init__(self, *args, **kwargs):
        super(DashboardMain, self).__init__(*args, **kwargs)
        self.template_name = 'main.html'

    def get_context_super_user(self):
        operators = User.operator_user_objects.all()
        users = User.normal_user_objects.all()
        return {
            'operators_count': operators.count(),
            'operators_latest': operators[:8],
            'users_count': users.count(),
            'users_latest': users[:8],
        }


class DashboardMenu(ComponentView, View):

    def __init__(self, *args, **kwargs):
        super(DashboardMenu, self).__init__(*args, **kwargs)
        self.template_name = 'menu.html'
