from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class ProgramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.program'
    verbose_name = _('Program')
