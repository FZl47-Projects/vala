from django.utils.translation import gettext as _
from django.db.models import TextChoices


# Users access levels choices
class AccessChoices(TextChoices):
    USER = 'user', _('User')
    ADMIN = 'admin', _('Admin')
    OPERATOR = 'operator', _('Operator')
    DIET_OP = 'diet_op', _('Diet operator')
    WORKOUT_OP = 'workout_op', _('Workout operator')
