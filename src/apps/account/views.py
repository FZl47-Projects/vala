import json
from django.contrib.auth import authenticate, login, get_user_model, logout as logout_handler
from django.http import JsonResponse, HttpResponseBadRequest, Http404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from apps.account.auth.mixins import LoginRequiredMixinCustom, SuperUserRequiredMixin, AdminRequiredMixin
from apps.core.utils import add_prefix_phonenum, random_num, form_validate_err
from apps.core.redis_py import set_value_expire, remove_key, get_value
from apps.notification.models import NotificationUser

from apps.account.models import User
from apps.account import forms

User = get_user_model()
RESET_PASSWORD_CONFIG = settings.RESET_PASSWORD_CONFIG
CONFIRM_PHONENUMBER_CONFIG = settings.CONFIRM_PHONENUMBER_CONFIG


class Login(TemplateView):
    template_name = 'account/login.html'

    def post(self, request):
        data = request.POST
        phonenumber = data.get('phonenumber', None)
        password = data.get('password', None)
        if not (phonenumber or password):
            messages.error(request, 'لطفا فیلد هارا به درستی وارد نمایید')
            return redirect('account:login')
        phonenumber = add_prefix_phonenum(phonenumber)
        user = authenticate(request, username=phonenumber, password=password)
        if user is None:
            messages.error(request, 'کاربری با این مشخصات یافت نشد یا حساب غیر فعال میباشد')
            return redirect('account:login')
        if user.is_active is False:
            messages.error(request, 'حساب شما غیر فعال میباشد')
            return redirect('account:login')
        login(request, user)
        messages.success(request, 'خوش امدید')
        # redirect to url or dashboard
        next_url = request.GET.get('next')
        try:
            # maybe next url not valid
            if next_url:
                return redirect(next_url)
        except Exception as e:
            pass
        return redirect('dashboard:index')


class Register(TemplateView):
    template_name = 'account/register.html'

    def post(self, request):
        data = request.POST
        f = forms.RegisterUserForm(data=data)
        if f.is_valid() is False:
            messages.error(request, 'لطفا فیلد هارا به درستی وارد نمایید')
            return redirect('account:register')
        # check for exists normal_user
        phonenumber = f.cleaned_data['phonenumber']
        if User.objects.filter(phonenumber=phonenumber).exists():
            messages.error(request, 'کاربری با این شماره از قبل ثبت شده است')
            return redirect('account:register')
        # create user
        password = f.cleaned_data['password2']
        user = User(
            phonenumber=phonenumber,
            is_active=True
        )
        user.set_password(password)
        user.save()
        # login
        login(request, user)
        messages.success(request, 'حساب شما با موفقیت ایجاد شد پس از تایید شماره همراه حساب شما فعال میشود')
        return redirect('account:confirm_phonenumber')


class Logout(View):

    def get(self, request):
        logout_handler(request)
        return redirect('public:index')


class ResetPassword(TemplateView):
    template_name = 'account/reset-password.html'


class ResetPasswordSend(View):

    def post(self, request):
        # AJAX view
        data = json.loads(request.body)
        phonenumber = data.get('phonenumber', None)
        # validate data
        if not phonenumber:
            return HttpResponseBadRequest()
        # check user is exists
        try:
            phonenumber = add_prefix_phonenum(phonenumber)
            user = User.objects.get(phonenumber=phonenumber)
        except:
            raise Http404
        code = random_num(RESET_PASSWORD_CONFIG['CODE_LENGTH'])
        key = RESET_PASSWORD_CONFIG['STORE_BY'].format(phonenumber)
        # check code state set
        if get_value(key) is not None:
            # code is already set
            return HttpResponse(status=409)
        # set code
        set_value_expire(key, code, RESET_PASSWORD_CONFIG['TIMEOUT'])
        # send code
        NotificationUser.objects.create(
            type='RESET_PASSWORD_CODE_SENT',
            kwargs={
                'code': code
            },
            to_user=user,
            title='بازیابی رمز عبور',
            description=f"""  کد بازیابی رمز عبور : {code}""",
            send_notify=True
        )
        return JsonResponse({})


class ResetPasswordCheck(View):

    def post(self, request):
        # AJAX view
        data = json.loads(request.body)
        phonenumber = data.get('phonenumber', None)
        code = data.get('code', None)
        # validate data
        if (not code) or (not phonenumber):
            return HttpResponseBadRequest()
        phonenumber = add_prefix_phonenum(phonenumber)
        key = RESET_PASSWORD_CONFIG['STORE_BY'].format(phonenumber)
        # check code
        code_stored = get_value(key)
        if code_stored is None:
            # code is not seted or timeout
            return HttpResponse(status=410)
        if code_stored != code:
            # code is wrong(not same)
            return HttpResponse(status=409)
        return JsonResponse({})


class ResetPasswordSet(View):

    def post(self, request):
        # AJAX view
        data = json.loads(request.body)
        f = forms.ResetPasswordSetForm(data)
        # validate data
        if f.is_valid() is False:
            return HttpResponseBadRequest()
        clean_data = f.cleaned_data
        # phonenumber must get from data (not clean_data)
        phonenumber = data['phonenumber']
        code = clean_data['code']
        password = clean_data['password2']
        # check user is exists
        try:
            phonenumber = add_prefix_phonenum(phonenumber)
            user = User.objects.get(phonenumber=phonenumber)
        except:
            raise Http404
        key = RESET_PASSWORD_CONFIG['STORE_BY'].format(phonenumber)
        # check code
        code_stored = get_value(key)
        if code_stored is None:
            # code is not seted or timeout
            return HttpResponse(status=410)
        if code_stored != code:
            # code is wrong(not same)
            return HttpResponse(status=409)
        user.set_password(password)
        user.save()
        remove_key(key)
        NotificationUser.objects.create(
            type='PASSWORD_CHANGED_SUCCESSFULLY',
            to_user=user,
            title='رمز عبور شما تغییر کرد',
            description="""رمز عبور شما با موفقیت تغییر کرد""",
            send_notify=True
        )
        return JsonResponse({})


class ConfirmPhonenumber(LoginRequiredMixin, View):
    template_name = 'account/confirm-phonenumber.html'

    def get(self, request):
        user = request.user
        if user.is_phonenumber_confirmed:
            return redirect('dashboard:index')
        key = CONFIRM_PHONENUMBER_CONFIG['STORE_BY'].format(user.get_raw_phonenumber())
        context = {
            'code_is_sent': bool(get_value(key))
        }
        return render(request, self.template_name, context)

    def post(self, request):
        # AJAX view
        user = request.user
        code = random_num(CONFIRM_PHONENUMBER_CONFIG['CODE_LENGTH'])
        key = CONFIRM_PHONENUMBER_CONFIG['STORE_BY'].format(user.get_raw_phonenumber())
        # check code state set
        if get_value(key) is not None:
            # code is already set
            return HttpResponse(status=409)
        # set code
        set_value_expire(key, code, CONFIRM_PHONENUMBER_CONFIG['TIMEOUT'])
        # send code
        NotificationUser.objects.create(
            type='CONFIRM_PHONENUMBER_CODE_SENT',
            kwargs={
                'code': code
            },
            to_user=user,
            title='کد تایید شماره همراه',
            description=f""" کد تایید شماره همراه : {code}""",
            send_notify=True
        )
        return JsonResponse({})


class ConfirmPhonenumberCheckCode(LoginRequiredMixin, View):

    def post(self, request):
        # AJAX view
        data = json.loads(request.body)
        code = data.get('code', None)
        # validate data
        if not code:
            return HttpResponseBadRequest()
        user = request.user
        key = CONFIRM_PHONENUMBER_CONFIG['STORE_BY'].format(user.get_raw_phonenumber())
        # check code
        code_stored = get_value(key)
        if code_stored is None:
            # code is not seted or timeout
            return HttpResponse(status=410)
        if code_stored != code:
            # code is wrong(not same)
            return HttpResponse(status=409)
        # confirm phonenumber
        user.is_phonenumber_confirmed = True
        user.save()
        NotificationUser.objects.create(
            type='PHONENUMBER_CONFIRMED',
            to_user=user,
            title='شماره همراه تایید شد',
            description=f"شماره همراه کاربر با موفقیت تایید شد",
            send_notify=True
        )
        messages.success(request, 'شماره همراه شما تایید شد')
        return JsonResponse({})


class DashboardUserPersonalDetail(LoginRequiredMixin, TemplateView):
    template_name = 'account/dashboard/users/personal-detail.html'

    def post(self, request):
        data = request.POST.copy()
        user = request.user
        form_basic = forms.UpdateUserDetailBasic(instance=user, data=data)
        if form_validate_err(request, form_basic) is False:
            return redirect('account:user_personal__detail')
        form_basic.save()

        profile = user.get_profile()
        # set additional value
        data['user'] = user
        form_profile = forms.UpdateUserProfileDetail(instance=profile, data=data, files=request.FILES)
        if form_validate_err(request, form_profile) is False:
            return redirect('account:user_personal__detail')
        form_profile.save()

        messages.success(request, 'اطلاعات شخصی شما با موفقیت ثبت و بروزرسانی شد')
        return redirect('dashboard:index')


class DashboardUserChangePassword(LoginRequiredMixin, TemplateView):
    template_name = 'account/dashboard/users/change-password.html'

    def post(self, request):
        user = request.user
        data = request.POST
        f = forms.UpdateUserPassword(data=data)
        if form_validate_err(request, f) is False:
            return redirect('account:user_change_password')
        data = f.cleaned_data
        if not user.check_password(data['current_password']):
            messages.error(request, 'رمز عبور فعلی نادرست است')
            return redirect('account:user_change_password')
        user.set_password(data['new_password'])
        user.save()
        messages.success(request, 'رمز عبور شما با موفقیت بروزرسانی شد')
        return redirect('account:login')


class DashboardUserList(LoginRequiredMixinCustom, AdminRequiredMixin, TemplateView):
    template_name = 'account/dashboard/users/normal/list.html'


class DashboardOperatorList(LoginRequiredMixinCustom, SuperUserRequiredMixin, View):
    template_name = 'account/dashboard/users/operator/list.html'

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
            elif sort_by == 'most-meeting':
                # TODO: should be completed
                pass

        return objects

    def get(self, request):
        operators = User.operator_user_objects.all()
        operators = self.filter(operators)
        pagination = self.pagination(operators)
        context = {
            'operators': pagination.object_list,
            'pagination': pagination
        }
        return render(request, 'account/dashboard/users/operator/list.html', context)


class DashboardOperatorAdd(LoginRequiredMixinCustom, SuperUserRequiredMixin, TemplateView):
    template_name = 'account/dashboard/users/operator/add.html'

    def post(self, request):
        data = request.POST.copy()
        # set additional values
        data['role'] = 'operator_user'

        f = forms.AddUserForm(data=data)
        if form_validate_err(request, f) is False:
            return render(request, self.template_name)
        # create user
        user = f.save(commit=False)
        user.is_active = True
        user.set_password(f.cleaned_data['password2'])
        user.save()

        if data.get('send_notify'):
            # create notif for user
            NotificationUser.objects.create(
                type='CREATED_YOUR_ACCOUNT',
                to_user=user,
                title='ایجاد حساب شما توسط ادمین',
                description=f"""
                    کاربر گرامی حساب شما توسط ادمین ایجاد شد
                """
            )

        # create notif for admin
        NotificationUser.objects.create(
            type='CREATE_USER_BY_ADMIN',
            to_user=request.user,
            title='ایجاد کاربر اپراتور توسط شما',
            description=f"""
                    کاربر {user.phonenumber}
                    ایجاد شد
            """
        )

        messages.success(request, 'حساب اپراتور با موفقیت ایجاد شد')
        return redirect(user.get_dashboard_absolute_url())


class DashboardUserAdd(LoginRequiredMixinCustom, AdminRequiredMixin, TemplateView):
    template_name = 'account/dashboard/users/normal/add.html'

    def post(self, request):
        data = request.POST.copy()
        # set additional values
        data['role'] = 'operator_user'

        f = forms.AddUserForm(data=data)
        if form_validate_err(request, f) is False:
            return render(request, self.template_name)
        # create user
        user = f.save(commit=False)
        user.is_active = True
        user.set_password(f.cleaned_data['password2'])
        user.save()

        if data.get('send_notify'):
            # create notif for user
            NotificationUser.objects.create(
                type='CREATED_YOUR_ACCOUNT',
                to_user=user,
                title='ایجاد حساب شما توسط ادمین',
                description=f"""
                            کاربر گرامی حساب شما توسط ادمین ایجاد شد
                        """
            )

        # create notif for admin
        NotificationUser.objects.create(
            type='CREATE_USER_BY_ADMIN',
            to_user=request.user,
            title='ایجاد کاربر عادی توسط شما',
            description=f"""
                            کاربر {user.phonenumber}
                            ایجاد شد
                    """
        )

        messages.success(request, 'حساب اپراتور با موفقیت ایجاد شد')
        return redirect(user.get_dashboard_absolute_url())
