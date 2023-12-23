from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView
from apps.core.utils import form_validate_err
from apps.account.auth.mixins import OperatorUserRequiredMixin
from . import forms


class MeetingAdd(TemplateView):
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
        f = forms.AreaBodyFormSetAdd(data)
        if not f.is_valid():
            meeting.delete()
            messages.error(request, 'لطفا فیلد های ناحیه را به درستی پر نمایید')
            return redirect('cartex:meeting__add')
        f.save()
        messages.success(request, 'جلسه با موفقیت ایجاد و ثبت شد')
        return redirect(meeting.get_absolute_url())
