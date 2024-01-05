from django.utils.translation import gettext as _
from django.db.models import TextChoices


# ProgramStatus choices
class ProgramStatusEnum(TextChoices):
    DEFINED = 'defined', _('Defined')
    UNDEFINED = 'undefined', _('Undefined')
    EDITED = 'edited', _('Edited')
