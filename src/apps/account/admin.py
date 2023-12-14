from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group
from django.contrib import admin

from .forms import UserCreationForm
from .models import User


# User model admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The form to add user instances
    add_form = UserCreationForm

    list_display = ('phone_number', 'email', 'access_level', 'is_active',)
    list_display_links = ('phone_number', 'email',)
    readonly_fields = ('created_at', 'last_login',)
    list_filter = ('is_active', 'access_level',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password',)}),
        (_('Personal info'), {'fields': ('email', 'first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('access_level', 'is_admin', 'is_active',)}),
        (_('Dates'), {'fields': ('last_login', 'created_at',)}),
    )
    radio_fields = {'access_level': admin.HORIZONTAL}

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'password1', 'password2'),
        }),
    )

    # Add search fields and ordering fields
    search_fields = ('phone_number', 'email')
    ordering = ('phone_number',)
    filter_horizontal = ()


# Unregister the Group model from admin.
admin.site.unregister(Group)
