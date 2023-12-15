from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.views.generic import View
from django.core.paginator import Paginator
from account.auth.mixins import LoginRequiredMixinCustom
from account.auth.decorators import admin_required_cbv
from apps.core.utils import form_validate_err
from apps.notification.forms import NotificationUserForm
from apps.notification.models import NotificationUser

User = get_user_model()


class NotificationAdd(View):
    template_name = 'notification/dashboard/add.html'

    @admin_required_cbv(['super_user'])
    def get(self, request):
        return render(request, self.template_name)

    @admin_required_cbv(['super_user'])
    def post(self, request):
        data = request.POST
        f = NotificationForm(data, request.FILES)
        if form_validate_err(request, f) is False:
            return render(request, self.template_name)
        f.save()
        messages.success(request, 'اعلان با موفقیت ایجاد شد')
        return redirect('notification:notification_dashboard_add')


class NotificationList(View):
    template_name = 'notification/dashboard/list.html'

    @admin_required_cbv()
    def get(self, request):
        page_num = request.GET.get('page', 1)
        notifications = Notification.objects.all()
        pagination = Paginator(notifications, 20)
        pagination = pagination.get_page(page_num)
        notifications = pagination.object_list
        context = {
            'notifications': notifications,
            'pagination': pagination
        }
        return render(request, self.template_name, context)


class NotificationDetail(View):
    template_name = 'notification/dashboard/detail.html'

    @admin_required_cbv()
    def get(self, request, notification_id):
        notification = get_object_or_404(Notification, id=notification_id)
        context = {
            'notification': notification
        }
        return render(request, self.template_name, context)


class NotificationDelete(View):

    @admin_required_cbv(['super_user'])
    def post(self, request, notification_id):
        notification = get_object_or_404(Notification, id=notification_id)
        notification.delete()
        messages.success(request, 'اعلان با موفقیت حذف شد')
        return redirect('notification:notification_dashboard_list')


class NotificationUpdate(View):

    @admin_required_cbv(['super_user'])
    def post(self, request, notification_id):
        notification = get_object_or_404(Notification, id=notification_id)
        f = NotificationUpdateForm(request.POST, request.FILES,instance=notification)
        if form_validate_err(request,f) is False:
            return redirect(notification.get_absolute_url())
        f.save()
        messages.success(request, 'اعلان با موفقیت بروزرسانی شد')
        return redirect(notification.get_absolute_url())


class NotificationUserAdd(View):
    template_name = 'notification/dashboard/add-user.html'

    @admin_required_cbv()
    def get(self, request):
        context = {
            'users': User.objects.all()
        }
        return render(request, self.template_name, context)

    @admin_required_cbv()
    def post(self, request):
        data = request.POST.copy()
        data['type'] = 'CUSTOM_NOTIFICATION'
        f = NotificationUserForm(data, request.FILES)
        if form_validate_err(request, f) is False:
            return render(request, self.template_name)
        f.save()
        messages.success(request, 'اعلان با موفقیت ایجاد شد')
        return redirect('notification:notification_dashboard_user_add')


class NotificationUserList(View):
    template_name = 'notification/dashboard/list-user.html'

    @admin_required_cbv()
    def get(self, request):
        page_num = request.GET.get('page', 1)
        notifications = NotificationUser.objects.all()
        pagination = Paginator(notifications, 20)
        pagination = pagination.get_page(page_num)
        notifications = pagination.object_list
        context = {
            'notifications': notifications,
            'pagination': pagination
        }
        return render(request, self.template_name, context)


class NotificationUserPersonalList(LoginRequiredMixinCustom, View):
    template_name = 'notification/dashboard/personal-list.html'

    def get(self, request):
        page_num = request.GET.get('page', 1)
        notifications = request.user.get_notifications()
        pagination = Paginator(notifications, 20)
        pagination = pagination.get_page(page_num)
        notifications = pagination.object_list
        context = {
            'notifications': notifications,
            'pagination': pagination
        }
        return render(request, self.template_name, context)


class NotificationUserDetail(LoginRequiredMixinCustom, View):
    template_name = 'notification/dashboard/detail-user.html'

    def get(self, request, notification_id):
        notification = get_object_or_404(NotificationUser, id=notification_id)
        user = request.user
        # only own user and admin can access
        if notification.to_user != user and user.is_admin is False:
            raise Http404
        context = {
            'notification': notification
        }
        return render(request, self.template_name, context)
