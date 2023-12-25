from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, View
from apps.core.utils import form_validate_err
from apps.notification.models import NotificationUser
from apps.account.auth import mixins
from . import forms, models


class MeetingAdd(mixins.OperatorUserRequiredMixin, TemplateView):
    template_name = 'cartex/dashboard/meeting/add.html'

    def post(self, request):
        data = request.POST.copy()
        operator_user = request.user
        # create and save meeting
        # set additional values
        data['operator'] = operator_user
        f = forms.MeetingAddForm(data)
        if form_validate_err(request, f) is False:
            return redirect('cartex:meeting__add')
        meeting = f.save()
        # create and save area bodies in meeting
        # # set additional values
        data['meeting'] = meeting
        if len(data.getlist('area_code', [])) == 0:
            messages.error(request, 'ناحیه ای را انتخاب نکرده اید')
            return redirect('cartex:meeting__add')
        f = forms.AreaBodyFormSetAdd(data)
        if not f.is_valid():
            meeting.delete()
            messages.error(request, 'لطفا فیلد های ناحیه را به درستی پر نمایید')
            return redirect('cartex:meeting__add')
        f.save()
        messages.success(request, 'جلسه با موفقیت ایجاد و ثبت شد')
        # create notif for user
        NotificationUser.objects.create(
            type='CREATED_MEETING',
            to_user=meeting.user,
            title='ایجاد جلسه',
            description=f"""کاربر گرامی جلسه ای برای شما ایجاد شد"""
        )
        return redirect(meeting.get_absolute_url())


class MeetingList(mixins.LoginRequiredMixinCustom, TemplateView):
    template_name = 'cartex/dashboard/meeting/list.html'


class MeetingDetail(mixins.LoginRequiredMixinCustom, View):

    def get(self, request, meeting_id):
        meeting = get_object_or_404(models.Meeting, id=meeting_id)
        context = {
            'meeting': meeting
        }
        return render(request, 'cartex/dashboard/meeting/detail.html', context)


class MeetingDelete(mixins.SuperUserRequiredMixin, View):

    def post(self, request, meeting_id):
        meeting = get_object_or_404(models.Meeting, id=meeting_id)
        meeting.delete()
        messages.success(request, 'جلسه با موفقیت حذف شد')
        return redirect('cartex:meeting__list')


class AreaBodyUpdate(mixins.OperatorUserRequiredMixin, View):

    def post(self, request, area_id):
        area_body = get_object_or_404(models.AreaBody, id=area_id, meeting__operator=request.user)
        f = forms.AreaBodyUpdateForm(request.POST, instance=area_body)
        if form_validate_err(request, f) is False:
            return redirect(area_body.meeting.get_absolute_url())
        f.save()
        messages.success(request, 'ناحیه مورد نظر با موفقیت بروزرسانی شد')
        return redirect(area_body.meeting.get_absolute_url())


class AreaBodyDelete(mixins.OperatorUserRequiredMixin, View):

    def post(self, request, area_id):
        area_body = get_object_or_404(models.AreaBody, id=area_id, meeting__operator=request.user)
        meeting = area_body.meeting
        area_body.delete()
        messages.success(request, 'ناحیه مورد نظر با موفقیت حذف شد')
        return redirect(meeting.get_absolute_url())
