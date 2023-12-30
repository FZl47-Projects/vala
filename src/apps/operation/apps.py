from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class OperationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.operation'
    verbose_name = _('Operation')
