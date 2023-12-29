from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.service'
    verbose_name = _('Service')
