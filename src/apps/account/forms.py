from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate
from django import forms

from .utils import check_phone_number, get_coded_phone_number
from .models import User


# Custom User creation form
class UserCreationForm(forms.ModelForm):
    """ A form for creating new users. Includes all the required
    fields, plus a repeated password. """

    phone_number = forms.CharField(label=_('Phone number'), max_length=11)
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password repeat'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number',)

    def clean_phone_number(self):
        # Check phone number format and return raw form
        phone_number = self.cleaned_data.get('phone_number')

        if not check_phone_number(phone_number):
            raise ValidationError(_('Enter a valid phone number'))

        return get_coded_phone_number(phone_number)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Passwords are not match.'))

        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user


# Login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=11, required=True, widget=forms.TextInput)
    password = forms.CharField(max_length=64, required=True, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Check username format (username is phone number in here)
        if not check_phone_number(username):
            raise ValidationError(_('Enter a valid phone number'))
        username = get_coded_phone_number(username)

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError(_('Entered data is incorrect'))

        return user
