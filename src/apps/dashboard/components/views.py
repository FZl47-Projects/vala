from django.views.generic import View
from apps.account.models import User
from apps.core.components import BaseComponentView
from apps.cartex.models import Meeting


class ComponentView(BaseComponentView):
    BASE_DIR_TEMPLATE_COMPONENTS = 'dashboard/components'


class DashboardMain(ComponentView, View):

    def __init__(self, *args, **kwargs):
        super(DashboardMain, self).__init__(*args, **kwargs)
        self.template_name = 'main.html'

    def get_context_super_user(self):
        operators = User.operator_user_objects.all()
        users = User.normal_user_objects.all()
        meetings = Meeting.objects.all()
        return {
            'operators_count': operators.count(),
            'operators_latest': operators[:8],
            'users_count': users.count(),
            'users_latest': users[:8],
            'meetings': meetings,
        }

    def get_context_operator_user(self):
        user = self.request.user
        meetings = user.get_meetings()
        users = User.normal_user_objects.filter(meeting__operator=user).distinct()
        return {
            'users': users,
            'meetings': meetings,
        }

    def get_context_normal_user(self):
        user = self.request.user
        meetings = user.get_meetings()
        return {
            'meetings': meetings,
        }


class DashboardMenu(ComponentView, View):

    def __init__(self, *args, **kwargs):
        super(DashboardMenu, self).__init__(*args, **kwargs)
        self.template_name = 'menu.html'
