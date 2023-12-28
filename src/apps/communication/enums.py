from django.utils.translation import gettext as _
from django.db.models import TextChoices


# TicketStatus Choices
class TicketStatusChoices(TextChoices):
    OPEN = 'open', _('Open')
    CLOSED = 'closed', _('Closed')
