from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext as _
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from .enums import AccessLevelsEnum
from .managers import UserManager


# Custom User model
class User(AbstractBaseUser):
    ACCESS_LEVELS = AccessLevelsEnum

    # Fields
    phone_number = PhoneNumberField(_('Phone number'), max_length=32, unique=True)
    email = models.EmailField(_("Email address"), max_length=255, null=True, blank=True)
    first_name = models.CharField(_('First name'), max_length=128, null=True, blank=True)
    last_name = models.CharField(_('Last name'), max_length=128, null=True, blank=True)
    is_active = models.BooleanField(_("Active"), default=True)
    is_admin = models.BooleanField(_("Admin"), default=False)
    access_level = models.CharField(_("Access level"), max_length=32, choices=ACCESS_LEVELS.choices, default=ACCESS_LEVELS.USER)

    objects = UserManager()  # Set UserManager as model object manager

    USERNAME_FIELD = "phone_number"

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        """ Does the user have a specific permission? """
        if self.is_admin:
            return True

        return False

    def has_module_perms(self, app_label):
        """ Does the user have permissions to view the app `app_label`? """
        return True

    @property
    def is_staff(self):
        """ Is the user a member of staff? """
        return self.is_admin
