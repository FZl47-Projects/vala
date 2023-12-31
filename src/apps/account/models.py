from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext as _
from django.templatetags.static import static
from django.shortcuts import reverse
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from .enums import UserAccessEnum, ProfileLevelsEnum
from apps.core.models import BaseModel
from .utils import get_raw_phone_number
from .managers import UserManager
from secrets import token_hex


# User Access model
class Access(BaseModel):
    ACCESS = UserAccessEnum
    title = models.CharField(_('Access title'), max_length=64, choices=ACCESS.choices, unique=True)

    class Meta:
        verbose_name = _('Access')
        verbose_name_plural = _('Accesses')

    def __str__(self):
        return self.title

    def get_title_label(self):
        return self.get_title_display()


# Custom User model
class User(AbstractBaseUser):
    ACCESSES = UserAccessEnum

    # Fields
    phone_number = PhoneNumberField(_('Phone number'), max_length=32, unique=True)
    email = models.EmailField(_("Email address"), max_length=255, null=True, blank=True)
    first_name = models.CharField(_('First name'), max_length=128, null=True, blank=True)
    last_name = models.CharField(_('Last name'), max_length=128, null=True, blank=True)
    is_active = models.BooleanField(_("Active"), default=True)
    is_verified = models.BooleanField(_('Verify'), default=False)
    is_admin = models.BooleanField(_("Admin"), default=False)
    access = models.ManyToManyField(Access, verbose_name=_("Accesses"), blank=True)

    token = models.CharField(_("Secret token"), max_length=64, null=True, blank=True, editable=False)

    created_at = models.DateTimeField(_('Creation time'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update time'), auto_now=True)

    objects = UserManager()  # Set UserManager as model object manager

    USERNAME_FIELD = "phone_number"

    REQUIRED_FIELDS = []

    OP_ROLES = [ACCESSES.DIET_OP, ACCESSES.WORKOUT_OP, ACCESSES.ADMIN]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        phone_number = self.get_phone_number()
        return phone_number

    def get_phone_number(self):
        if self.phone_number:
            return get_raw_phone_number(self.phone_number)

    def has_perm(self, perm=None, obj=None):
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

    @property
    def has_admin_access(self):
        if self.access.filter(title=self.ACCESSES.ADMIN).exists():
            return True
        return False

    def has_specific_access(self, access=None):
        if self.access.filter(title=access).exists():
            return True
        return False

    def has_operator_access(self):
        if self.access.filter(title__in=self.OP_ROLES).exists():
            return True
        return False

    def get_full_name(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'
        return _('No name')

    def generate_token(self, byte: int = 12):
        self.token = token_hex(byte)
        self.save()

        return self.token

    def clear_token(self, request):
        if 'register_token' in request.session:
            del request.session['register_token']

        self.token = None
        self.save()


# User Profile model
class UserProfile(BaseModel):
    LEVELS = ProfileLevelsEnum

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='user_profile')
    level = models.CharField(_('Profile level'), max_length=32, choices=LEVELS.choices, default=LEVELS.BASIC)

    # Admin questions
    question1 = models.CharField(_('First question'), max_length=64, default=_('No answer'))
    question2 = models.CharField(_('Second question'), max_length=64, default=_('No answer'))

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

    def get_absolute_url(self):
        return reverse('account:profile_details', args=[self.user.pk])

    def get_image_url(self):
        if self.image:
            return self.image.url

        return static('images/default/user-default.png')

    def get_date_of_birth(self):
        if self.date_of_birth:
            return self.date_of_birth.strftime('%Y-%m-%d')

    def get_level_label(self):
        return self.get_level_display()
