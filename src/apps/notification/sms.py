from apps.core.utils import get_host_url
from .utils import send_sms


class NotificationUser:

    @classmethod
    def handler_password_changed_successfully(cls, notification, phonenumber):
        pattern = 'iseiyg8otwl06bi'
        send_sms(phonenumber, pattern, {
            # 'notification_url': '#',
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_reset_password_code_sent(cls, notification, phonenumber):
        pattern = 'xka1tvkiqiwnrjx'
        send_sms(phonenumber, pattern, {
            'code': notification.kwargs['code']
        })

    @classmethod
    def handler_confirm_phonenumber_code_sent(cls, notification, phonenumber):
        pattern = '9mld0scmid2i2wl'
        send_sms(phonenumber, pattern, {
            'code': notification.kwargs['code']
        })

    @classmethod
    def handler_phonenumber_confirmed(cls, notification, phonenumber):
        pattern = 'to1j8k209iigm7f'
        send_sms(phonenumber, pattern, {
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_created_your_account(cls, notification, phonenumber):
        # TODO: should be completed(sms panel and pattern code)
        pattern = 'to1j8k209iigm7f'
        send_sms(phonenumber, pattern, {
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_create_user_by_admin(cls, notification, phonenumber):
        # TODO: should be completed(sms panel and pattern code)
        pattern = 'to1j8k209iigm7f'
        send_sms(phonenumber, pattern, {
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_custom_notification(cls, notification, phonenumber):
        # TODO: should be completed(sms panel and pattern code)
        pattern = 'ar0prdkncw4dk9l'
        send_sms(phonenumber, pattern, {
            'notification_url': get_host_url(notification.get_link()),
            'user_name': notification.to_user.get_full_name()
        })


NOTIFICATION_USER_HANDLERS = {
    'PASSWORD_CHANGED_SUCCESSFULLY': NotificationUser.handler_password_changed_successfully,
    'RESET_PASSWORD_CODE_SENT': NotificationUser.handler_reset_password_code_sent,
    'CONFIRM_PHONENUMBER_CODE_SENT': NotificationUser.handler_confirm_phonenumber_code_sent,
    'PHONENUMBER_CONFIRMED': NotificationUser.handler_phonenumber_confirmed,
    'CREATED_YOUR_ACCOUNT': NotificationUser.handler_created_your_account,
    'CREATE_USER_BY_ADMIN': NotificationUser.handler_create_user_by_admin,
    'CUSTOM_NOTIFICATION': NotificationUser.handler_custom_notification,
}
