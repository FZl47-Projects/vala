from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class CommunicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.communication'
    verbose_name = _('Communication')

    def ready(self):
        from . import signals
