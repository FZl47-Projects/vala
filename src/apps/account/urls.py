from django.urls import path
from . import views
from . import components

app_name = 'apps.account'
urlpatterns = [
    # login logout and register
    path('login', views.Login.as_view(), name='login'),
    path('register', views.Register.as_view(), name='register'),
    path('logout', views.Logout.as_view(), name='logout'),
    # confirm account
    path('confirm/phonenumber', views.ConfirmPhonenumber.as_view(), name='confirm_phonenumber'),
    path('confirm/phonenumber/check', views.ConfirmPhonenumberCheckCode.as_view(),
         name='confirm_phonenumber_check_code'),
    # reset password
    path('reset-password', views.ResetPassword.as_view(), name='reset_password'),
    path('reset-password/send-code', views.ResetPasswordSend.as_view(), name='reset_password_send_code'),
    path('reset-password/check-code', views.ResetPasswordCheck.as_view(), name='reset_password_check_code'),
    path('reset-password/set', views.ResetPasswordSet.as_view(), name='reset_password_set'),

    # Dashboard
    # users
    path('dashboard/personal/detail', views.DashboardUserPersonalDetail.as_view(), name='user_personal__detail'),
    path('dashboard/change-password', views.DashboardUserChangePassword.as_view(), name='user_change_password'),
    path('dashboard/user/list', views.DashboardUserList.as_view(), name='user__list'),
    path('dashboard/operator/list', views.DashboardOperatorList.as_view(), name='operator__list'),
    path('dashboard/user/add', views.DashboardUserAdd.as_view(), name='user__add'),
    path('dashboard/operator/add', views.DashboardOperatorAdd.as_view(), name='operator__add'),

    # components view
    path('dashboard/user/component/list', components.views.UserListPartial.as_view(),
         name='user_component_partial__list'),
    path('dashboard/user/normal/component/list', components.views.UserNormalListPartial.as_view(),
         name='user_normal_component_partial__list'),
]
