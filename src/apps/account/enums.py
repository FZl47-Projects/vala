from django.utils.translation import gettext as _
from django.db.models import TextChoices


# Users access levels choices
class AccessLevelsEnum(TextChoices):
    USER = 'user', _('User')
    ADMIN = 'admin', _('Admin')
    OPERATOR = 'operator', _('Operator')
