from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q
from apps.core.components import BaseComponentView
from apps.core.utils import add_prefix_phonenum
from apps.cartex import models


class ComponentView(BaseComponentView):
    BASE_DIR_TEMPLATE_COMPONENTS = 'cartex/dashboard/components'


class MeetingDetail(ComponentView, View):

    def __init__(self, *args, **kwargs):
        super(MeetingDetail, self).__init__(*args, **kwargs)
        self.template_name = 'cartex/detail.html'

    def get_base_context(self, *args, **kwargs):
        return kwargs


class MeetingList(ComponentView, View):

    def __init__(self, *args, **kwargs):
        super(MeetingList, self).__init__(*args, **kwargs)
        self.template_name = 'cartex/list.html'

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
            lookup = Q(number_id__icontains=search_text) | Q(areabody__area_code__icontains=search_text)
            # search by phonenumber
            search_text = add_prefix_phonenum(search_text)
            lookup = lookup | Q(
                user__phonenumber=search_text) | Q(operator__phonenumber=search_text)

            objects = objects.filter(lookup)

        # sort
        sort_by = request.GET.get('sort_by', 'latest')
        if sort_by:
            if sort_by == 'latest':
                objects = objects.order_by('-id')
            elif sort_by == 'oldest':
                objects = objects.order_by('id')

        return objects

    def get_meetings(self):
        user = self.request.user
        if user.role == 'super_user':
            return models.Meeting.objects.all()
        return user.get_meetings()

    def get_base_context(self, *args, **kwargs):
        meetings = self.get_meetings()
        meetings = self.filter(meetings)
        pagination = self.pagination(meetings)
        context = {
            'meetings': pagination.object_list,
            'pagination': pagination
        }
        return context
