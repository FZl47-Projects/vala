from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate
from django import forms

from .utils import check_phone_number, get_coded_phone_number
from .models import User, UserProfile


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
        user.set_password(self.cleaned_data['password2'])
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

        return {'user': user}


# VerifyCode form
class VerifyCodeForm(forms.Form):
    user_code = forms.IntegerField(widget=forms.NumberInput)
    code = forms.IntegerField(widget=forms.NumberInput)

    def clean_code(self):
        user_code = self.cleaned_data.get('user_code')
        code = self.cleaned_data.get('code')

        if code != user_code:
            raise ValidationError(_('Entered code is not correct'))

        return code


# Add Profile form
class AddProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, widget=forms.TextInput)
    last_name = forms.CharField(max_length=128, widget=forms.TextInput)

    class Meta:
        model = UserProfile
        exclude = ('user', 'question2')

    def save(self, commit=True):
        profile = super().save(commit=True)
        user = profile.user

        # Save User info
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return profile


# Update Profile form
class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, widget=forms.TextInput)
    last_name = forms.CharField(max_length=128, widget=forms.TextInput)
    phone_number = forms.CharField(max_length=11, widget=forms.TextInput)

    class Meta:
        model = UserProfile
        fields = ('date_of_birth', 'height', 'weight', 'image',)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if not check_phone_number(phone_number):
            raise ValidationError(_('Enter a valid phone number'))

        return get_coded_phone_number(phone_number)

    def save(self, commit=True):
        profile = super().save(commit=True)
        user = profile.user

        # Save User info
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()

        return profile


# GetPhoneNumber form
class GetPhoneNumberForm(forms.Form):
    phone = forms.CharField(max_length=11, widget=forms.TextInput)

    def clean(self):
        phone = self.cleaned_data.get('phone')

        # Check phone number format
        if not check_phone_number(phone):
            raise ValidationError(_('Enter a valid phone number'))
        phone = get_coded_phone_number(phone)

        try:
            user = User.objects.get(phone_number=phone)
        except User.DoesNotExist:
            raise ValidationError(_('User not found'))

        return {'user': user}


# ResetPassword form
class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Passwords are not the same'))

        return password2
