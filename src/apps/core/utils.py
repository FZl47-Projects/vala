import string
import random
import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib import messages


def random_str(size=15, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_num(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_time(frmt='%Y-%m-%d_%H:%M'):
    t = timezone.now()
    if frmt is not None:
        t = t.strftime(frmt)
    return t


def get_timesince_persian(time):
    time_server = get_time(None)

    diff_time = datetime.datetime(time_server.year, time_server.month, time_server.day, time_server.hour,
                                  time_server.minute) - datetime.datetime(time.year, time.month, time.day, time.hour,
                                                                          time.minute)

    diff_time_sec = diff_time.total_seconds()
    # sec = diff_time_sec % 60
    min = int(diff_time_sec // 60 % 60)
    hour = int(diff_time_sec // 3600)
    day = diff_time.days
    result = ''
    if min > 0:
        result = f'{min} دقیقه پیش'
    else:
        result = f'لحظاتی پیش'

    if hour > 0:
        result = f'{hour} ساعت پیش'

    if day > 0:
        result = f'{day}  روز پیش'

    return result


def add_prefix_phonenum(phonenumber):
    phonenumber = str(phonenumber).replace('+98', '')
    return f'+98{phonenumber}'


def get_raw_phonenum(phonenumber):
    p = str(phonenumber).replace('+98', '')
    return p


def form_validate_err(request, form):
    if form.is_valid():
        return True
    errors = form.errors.as_data()
    if errors:
        for field, err in errors.items():
            err = str(err[0])
            err = err.replace('[', '').replace(']', '')
            err = err.replace("'", '').replace('This', '')
            err = f'{field} {err}'
            messages.error(request, err)
    else:
        messages.error(request, 'دیتای ورودی نامعتبر است')
    return False


def get_host_url(url):
    return settings.HOST_ADDRESS + url


def get_media_url(url):
    return settings.MEDIA_URL + url



