import requests
import json
from django.conf import settings
from django.core.mail import send_mail as _send_email_django
from django_q.tasks import async_task


def send_sms(phonenumber, pattern_code, values={}):
    phonenumber = str(phonenumber).replace('+', '')
    payload = json.dumps({
        "pattern_code": pattern_code,
        "originator": settings.SMS_CONFIG['ORIGINATOR'],
        "recipient": phonenumber,
        "values": values
    })
    headers = {
        'Authorization': "AccessKey {}".format(settings.SMS_CONFIG['API_KEY']),
        'Content-Type': 'application/json'
    }

    async_task(requests.request,
               'POST',
               settings.SMS_CONFIG['API_URL'],
               headers=headers,
               data=payload
               )


def send_email(email, subject, content, **kwargs):
    # send email in background
    async_task(_send_email_django,
               subject,
               content,
               settings.EMAIL_HOST_USER,
               [email]
               )
