from django.utils.translation import gettext as _
from django.contrib import messages
from django.utils import timezone
from datetime import datetime


# Timesince in persian utils
def get_timesince_persian(time):
    time_server = timezone.now()

    diff_time = datetime(
        time_server.year, time_server.month, time_server.day, time_server.hour, time_server.minute
    ) - datetime(
        time.year, time.month, time.day, time.hour, time.minute
    )

    diff_time_sec = diff_time.total_seconds()

    minute = int(diff_time_sec // 60 % 60)
    hour = int(diff_time_sec // 3600)
    day = diff_time.days

    if minute > 0:
        output = _('%(minutes)s minutes ago.') % {'minutes': minute}
    elif hour > 0:
        output = _('%(hours)s hours ago.') % {'hours': hour}
    elif day > 0:
        output = _('%(days)s days ago.') % {'days': day}
    else:
        output = _('Moments ago')

    return output


# Form validator utils
def validate_form(request, form):
    if form.is_valid():
        return True

    errors = form.errors.items()

    if not errors:
        messages.error(request, _('Entered data is not correct.'))
        return False

    for field, message in errors:
        for error in message:
            messages.error(request, error)

    return False

