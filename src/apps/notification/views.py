from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q
from apps.account.auth.mixins import LoginRequiredMixinCustom, SuperUserRequiredMixin, AdminRequiredMixin
from apps.core.utils import form_validate_err
from apps.notification.forms import NotificationUserFormAdd
from apps.notification.models import NotificationUser

User = get_user_model()


class NotificationUserAdd(AdminRequiredMixin, View):

    def get(self, request):
        return render(request, 'notification/dashboard/user/add.html')

    def post(self, request):
        data = request.POST.copy()
        data['type'] = 'CUSTOM_NOTIFICATION'
        f = NotificationUserFormAdd(data, request.FILES)
        if form_validate_err(request, f) is False:
            return redirect('notification:notification_user__add')
        f.save()
        messages.success(request, 'اعلان با موفقیت ایجاد شد')
        return redirect('notification:notification_user__add')


class NotificationUserDelete(LoginRequiredMixinCustom, View):

    def post(self, request, notification_id):
        notification = get_object_or_404(NotificationUser, id=notification_id, to_user=request.user)
        notification.delete()
        messages.success(request, 'اعلان با موفقیت حذف شد')
        return redirect('notification:notification_personal__list')


class NotificationUserPersonalList(LoginRequiredMixinCustom, View):

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
            lookup = Q(number_id__icontains=search_text) | Q(title__icontains=search_text)
            objects = objects.filter(lookup)

        # sort
        sort_by = request.GET.get('sort_by', 'latest')
        if sort_by:
            if sort_by == 'latest':
                objects = objects.order_by('-id')
            elif sort_by == 'oldest':
                objects = objects.order_by('id')
            elif sort_by == 'unread':
                objects = objects.order_by('is_seen')

        return objects

    def get(self, request):

        notifications = request.user.get_notifications()
        notifications = self.filter(notifications)
        pagination = self.pagination(notifications)
        context = {
            'notifications': pagination.object_list,
            'pagination': pagination
        }
        return render(request, 'notification/dashboard/personal-list.html', context)


class NotificationUserList(SuperUserRequiredMixin, View):

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
            lookup = Q(number_id__icontains=search_text) | Q(title__icontains=search_text) | Q(
                to_user__phonenumber__icontains=search_text)
            objects = objects.filter(lookup)

        # filter
        filter_by = request.GET.get('filter_by')
        if filter_by:
            if filter_by == 'normal_user':
                objects = objects.filter(to_user__role='normal_user')
            elif filter_by == 'operator_user':
                objects = objects.filter(to_user__role='operator_user')

        # sort
        sort_by = request.GET.get('sort_by', 'latest')
        if sort_by:
            if sort_by == 'latest':
                objects = objects.order_by('-id')
            elif sort_by == 'oldest':
                objects = objects.order_by('id')

        return objects

    def get(self, request):
        notifications = NotificationUser.objects.all().exclude(to_user__role__in=User.SUPER_USER_ROLES).filter(
            is_showing=True)
        notifications = self.filter(notifications)
        pagination = self.pagination(notifications)
        context = {
            'notifications': pagination.object_list,
            'pagination': pagination
        }
        return render(request, 'notification/dashboard/user/list.html', context)


class NotificationUserDetail(LoginRequiredMixinCustom, View):

    def get(self, request, notification_id):
        notification = get_object_or_404(NotificationUser, id=notification_id)
        user = request.user
        # only own user and admin can access
        if notification.to_user != user and user.is_super_admin is False:
            raise Http404
        if notification.to_user == user:
            notification.is_seen = True
            notification.save()
        context = {
            'notification': notification
        }
        return render(request, 'notification/dashboard/user/detail.html', context)
