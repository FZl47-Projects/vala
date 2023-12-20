from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext as _
from django.templatetags.static import static
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from apps.core.models import BaseModel
from .utils import get_raw_phone_number
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
    is_verified = models.BooleanField(_('Verify'), default=False)
    is_admin = models.BooleanField(_("Admin"), default=False)
    access_level = models.CharField(_("Access level"), max_length=32, choices=ACCESS_LEVELS.choices, default=ACCESS_LEVELS.USER)

    created_at = models.DateTimeField(_('Creation time'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update time'), auto_now=True)

    objects = UserManager()  # Set UserManager as model object manager

    USERNAME_FIELD = "phone_number"

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        phone_number = self.get_phone_number()
        return phone_number

    def get_phone_number(self):
        if self.phone_number:
            return get_raw_phone_number(self.phone_number)

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

    def get_full_name(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'
        return _('No name')


# User Profile model
class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='user_profile')
    image = models.ImageField(_('Picture'), upload_to='images/user/profile/', null=True, blank=True)
    date_of_birth = models.DateField(_('Date of birth'), null=True, blank=True)

    height = models.PositiveIntegerField(_('Height'), default=0)
    weight = models.PositiveIntegerField(_('Weight'), default=0)

    is_verified = models.BooleanField(_('Verified'), default=False)

    class Meta:
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')

    def __str__(self):
        return f'{self.user}'

    def get_image_url(self):
        if self.image:
            return self.image.url

        return static('images/default/comment-default.png')

    def get_date_of_birth(self):
        if self.date_of_birth:
            return self.date_of_birth.strftime('%Y-%m-%d')
