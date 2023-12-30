from django.utils.translation import gettext as _
from django.db.models import TextChoices


# TestStatus Choices
class TestStatusChoices(TextChoices):
    ANSWERED = 'answered', _('Answered')
    AWAIT = 'await', _('Await')
