from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from . import models


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ('phonenumber',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = ('phonenumber',)


class RegisterUserForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phonenumber = PhoneNumberField(region='IR')
    password = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError('passwords is not same')
        return p2


class AddUserForm(forms.ModelForm):
    password2 = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())

    class Meta:
        model = models.User
        exclude = ('date_joined', 'is_phonenumber_confirmed')
        error_messages = {
            'phonenumber': {
                'invalid': 'شماره همراه نامعتبر است',
                'unique': 'کاربری با این شماره از قبل ثبت شده است'
            },
        }

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError('رمز های عبور وارد شده بایکدیگر مغایرت دارند ')
        return p2


class ResetPasswordSetForm(forms.Form):
    phonenumber = PhoneNumberField(region='IR')
    code = forms.CharField()
    password = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError('رمز های عبور وارد شده با یکدیگر مغایرت دارند')
        return p2


class UpdateUserProfileDetail(forms.ModelForm):
    picture = forms.FileField(required=False)
    note = forms.CharField(required=False)

    class Meta:
        model = models.UserProfile
        fields = '__all__'


class UpdateUserDetailBasic(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('first_name', 'last_name')


class UpdateUserDetail(forms.ModelForm):
    last_name = forms.CharField(required=False)

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'is_active', 'is_phonenumber_confirmed', 'phonenumber')
        error_messages = {
            'phonenumber': {
                'invalid': 'شماره همراه نامعتبر است',
                'unique': 'کاربری با این شماره از قبل ثبت شده است'
            },
        }


class UpdateUserPassword(forms.Form):
    current_password = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())
    new_password2 = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())

    def clean_new_password2(self):
        p1 = self.cleaned_data.get('new_password')
        p2 = self.cleaned_data.get('new_password2')
        if p1 != p2:
            raise forms.ValidationError('رمز های عبور وارد شده با یکدیگر مغایرت دارند')
        return p2
