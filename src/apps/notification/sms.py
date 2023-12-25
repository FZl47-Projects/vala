from apps.core.utils import get_host_url
from .utils import send_sms


class NotificationUser:

    @classmethod
    def handler_password_changed_successfully(cls, notification, phonenumber):
        pattern = 'rar4cihhq3l9rzr'
        send_sms(phonenumber, pattern, {
            'notification_url': notification.get_absolute_url(),
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_reset_password_code_sent(cls, notification, phonenumber):
        pattern = 'sbtqhxqh6ip8b5h'
        send_sms(phonenumber, pattern, {
            'code': notification.kwargs['code']
        })

    @classmethod
    def handler_confirm_phonenumber_code_sent(cls, notification, phonenumber):
        pattern = 'awdm4kkt8sqbtg4'
        send_sms(phonenumber, pattern, {
            'code': notification.kwargs['code']
        })

    @classmethod
    def handler_phonenumber_confirmed(cls, notification, phonenumber):
        pattern = 'asovuukjjznkdct'
        send_sms(phonenumber, pattern, {
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_created_your_account(cls, notification, phonenumber):
        pattern = 'ixcrflvdbbqf7xl'
        send_sms(phonenumber, pattern, {
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_create_user_by_admin(cls, notification, phonenumber):
        pattern = 'lbv9bxk817cl19c'
        send_sms(phonenumber, pattern, {
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_create_meeting(cls, notification, phonenumber):
        pattern = '5ebfdiuvivq4xw3'
        send_sms(phonenumber, pattern, {
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_custom_notification(cls, notification, phonenumber):
        pattern = 'sgrwqtbth5n6jkw'
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
    'CREATED_MEETING': NotificationUser.handler_create_meeting,
    'CUSTOM_NOTIFICATION': NotificationUser.handler_custom_notification,
}
