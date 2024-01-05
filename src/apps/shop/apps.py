from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.shop'
    verbose_name = _('Shop')
