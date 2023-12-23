import json
from django.core.paginator import Paginator
from django.core import serializers
from django.urls import reverse
from django.views.generic import View
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.db.models import Q, Value
from django.db.models.functions import Concat
from apps.account.auth.mixins import AdminRequiredMixin
from apps.account.models import User
from apps.core.components import BaseComponentView


class ComponentView(BaseComponentView):
    BASE_DIR_TEMPLATE_COMPONENTS = 'account/dashboard/components'


class DashboardUserList(ComponentView, View):

    def __init__(self, *args, **kwargs):
        super(DashboardUserList, self).__init__(*args, **kwargs)
        self.template_name = 'user-list.html'

    def pagination(self, objects):
        COUNT_PER_PAGE = 20
        paginator = Paginator(objects, COUNT_PER_PAGE)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return page_obj

    def filter(self, objects):
        request = self.request
        # search
        search_text = request.GET.get('search')
        if search_text:
            objects = objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
            lookup = Q(full_name__icontains=search_text) | Q(phonenumber__icontains=search_text)
            objects = objects.filter(lookup)

        # sort
        sort_by = request.GET.get('sort_by', 'latest')
        if sort_by:
            if sort_by == 'latest':
                objects = objects.order_by('-id')
            elif sort_by == 'oldest':
                objects = objects.order_by('id')
            elif sort_by == 'most-visited':
                # TODO: should be completed
                pass

        return objects

    def get_base_context(self):
        users = User.normal_user_objects.all()
        users = self.filter(users)
        pagination = self.pagination(users)
        return {
            'users': pagination.object_list,
            'pagination': pagination
        }


class DashboardUserPersonalDetail(ComponentView, View):

    def __init__(self, *args, **kwargs):
        super(DashboardUserPersonalDetail, self).__init__(*args, **kwargs)
        self.template_name = 'personal-detail.html'


class UserListPartial(AdminRequiredMixin, View):

    def get_users(self):
        return User.objects.exclude(role__in=User.SUPER_USER_ROLES)

    def get_url_search_view(self):
        return reverse('account:user_component_partial__list')

    def get(self, request, **kwargs):
        users = self.get_users()
        page_num = request.GET.get('page', 1)
        pagination = Paginator(users, 15)
        pagination = pagination.get_page(page_num)
        users = pagination.object_list
        context = {
            'users': users,
            'pagination': pagination,
            'url_search_view': self.get_url_search_view()
        }
        return render(request, 'account/dashboard/components/base/user-list-partial.html', context)

    def post(self, request):
        data = json.loads(request.body)

        def search(self, objects):
            s = data.get('search')
            if not s:
                return objects
            objects = objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
            lookup = Q(phonenumber__icontains=s) | Q(full_name__icontains=s)
            return objects.filter(lookup)

        # ajax view
        if not request.headers.get('X_REQUESTED_WITH') == 'XMLHttpRequest':
            raise Http404
        users = self.get_users()
        users = search(request, users)
        users_serialized = serializers.serialize('json', users,
                                                 fields=('id', 'first_name', 'last_name', 'phonenumber', 'role'))
        return JsonResponse(users_serialized, safe=False)


class UserNormalListPartial(UserListPartial):

    def get_users(self):
        return User.objects.exclude(role__in=User.ADMIN_ROLES)

    def get_url_search_view(self):
        return reverse('account:user_normal_component_partial__list')