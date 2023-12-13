from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re


# Check phone number format(IR)
def check_phone_number(string):
    mobile_regex = "^09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}$"
    if re.search(mobile_regex, string):
        return True

    return False


# Check email format
def check_email_format(string):
    try:
        validate_email(string)
        return True
    except ValidationError:
        return False
