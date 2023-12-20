from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group
from django.db import models as a_model
from django.contrib import admin
from django import forms

from .forms import UserCreationForm
from .models import User, UserProfile


# Unregister the Group model from admin.
admin.site.unregister(Group)


# User model admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The form to add user instances
    add_form = UserCreationForm

    list_display = ('__str__', 'email', 'access_level', 'is_active', 'is_verified')
    list_display_links = ('__str__', 'email',)
    readonly_fields = ('created_at', 'last_login',)
    list_filter = ('is_active', 'access_level',)
    radio_fields = {'access_level': admin.HORIZONTAL}
    fieldsets = (
        (None, {'fields': ('phone_number', 'password',)}),
        (_('Personal info'), {'fields': ('email', 'first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('access_level', 'is_active', 'is_verified', 'is_admin',)}),
        (_('Dates'), {'fields': ('last_login', 'created_at',)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'password1', 'password2'),
        }),
    )

    # Add search and ordering fields
    search_fields = ('phone_number', 'email')
    ordering = ('phone_number',)
    filter_horizontal = ()


# UserProfile model admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth',)
    list_display_links = ('user',)
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('user.phone_number', 'user.last_name',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        (_('Info'), {'fields': ('image', 'date_of_birth', 'height', 'weight')}),
        (_('Admin questions'), {'fields': ('question1', 'question2')}),
        (_('Dates'), {'fields': ('created_at', 'updated_at')}),
    )

    # Change formField attributes(size)
    formfield_overrides = {
        a_model.CharField: {"widget": forms.TextInput(attrs={"size": "60"})},
    }
