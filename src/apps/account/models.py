from django.db import models
from django.urls import reverse
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import BadRequest
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from apps.core.utils import random_str


class CustomBaseUserManager(BaseUserManager):

    def create_user(self, phonenumber, password, **extra_fields):
        """
        Create and save a normal_user with the given phonenumber and password.
        """
        if not phonenumber:
            raise ValueError("The phonenumber must be set")
        user = self.model(phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_operator_user(self, phonenumber, password, email=None, **extra_fields):
        return self.create_user(phonenumber=phonenumber, password=password, role='operator_user',
                                **extra_fields)

    def create_superuser(self, phonenumber, password, email=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields['is_phonenumber_confirmed'] = True

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(phonenumber=phonenumber, password=password, role='super_user',
                                **extra_fields)


class NormalUserManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(role='normal_user')


class OperatorUserManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(role='operator_user')


class SuperUserManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(role='super_user')


class User(AbstractUser):
    ROLE_USER_OPTIONS = (
        ('normal_user', 'کاربر عادی'),
        ('operator_user', 'ادمین اپراتور'),
        ('super_user', 'ادمین وِیژه'),
    )
    OPERATOR_USER_ROLES = ('operator_user',)
    SUPER_USER_ROLES = ('super_user',)
    ADMIN_ROLES = (*SUPER_USER_ROLES, *OPERATOR_USER_ROLES)
    ALL_USER_ROLES = (*ADMIN_ROLES, 'normal_user')

    first_name = models.CharField("first name", max_length=150, blank=True, default="بدون نام")
    username = None
    email = None
    phonenumber = PhoneNumberField(region='IR', unique=True)
    is_phonenumber_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # type users|roles
    role = models.CharField(max_length=20, choices=ROLE_USER_OPTIONS, default='normal_user')

    USERNAME_FIELD = "phonenumber"
    REQUIRED_FIELDS = []

    objects = CustomBaseUserManager()
    normal_user_objects = NormalUserManager()
    operator_user_objects = OperatorUserManager()
    super_user_objects = SuperUserManager()

    class Meta:
        ordering = '-id',

    @property
    def is_admin(self):
        return True if self.role in self.ADMIN_ROLES else False

    @property
    def is_operator_admin(self):
        return True if self.role in self.OPERATOR_USER_ROLES else False

    @property
    def is_super_admin(self):
        return True if self.role in self.SUPER_USER_ROLES else False

    def __str__(self):
        return f'{self.role} - {self.phonenumber}'

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    def get_role_label(self):
        return self.get_role_display()

    def get_raw_phonenumber(self):
        p = str(self.phonenumber).replace('+98', '')
        return p

    def get_full_name(self):
        fl = f'{self.first_name} {self.last_name}'.strip() or 'بدون نام'
        return fl

    def get_email(self):
        return self.email or '-'

    def get_picture_profile_url(self):
        default_pic = '/static/template/images/default-user.jpg'
        profile = self.get_profile()
        if not profile:
            return default_pic
        if profile.picture:
            return profile.picture.url
        return default_pic

    def get_last_login(self):
        if self.last_login:
            return self.last_login.strftime('%Y-%m-%d %H:%M:%S')
        return '-'

    def get_dashboard_absolute_url(self):
        return reverse('account:user__detail', args=(self.id,))

    def get_absolute_url(self):
        return self.get_dashboard_absolute_url()

    def get_notifications(self):
        notifications = self.notificationuser_set.filter(is_showing=True)
        return notifications

    def get_unread_notifications(self):
        return self.get_notifications().filter(is_seen=False)

    def get_notifications_absolute_url(self):
        return f"{reverse('notification:notification_user__list')}?search={self.get_raw_phonenumber()}"

    def get_meetings_absolute_url(self):
        return f"{reverse('cartex:meeting__list')}?search={self.get_raw_phonenumber()}"

    def get_profile(self):
        try:
            return self.profile
        except AttributeError:
            return None

    def get_meetings(self):
        if self.role == 'normal_user':
            return self.meeting_set.all()
        return self.meetings_set_operator.all()

    def get_meetings_with_operator(self, operator):
        return self.get_meetings().filter(operator=operator)

    def get_count_meetings_with_operator(self, operator):
        return self.get_meetings_with_operator(operator).count()

    # operator methods
    def get_customers(self):
        return User.objects.filter(meeting__operator=self)

    def get_meetings_with_user(self, user):
        return self.get_meetings().filter(user=user)


def upload_picture_profile(instance, path):
    frmt = str(path).split('.')[-1]
    if frmt not in settings.IMAGES_FORMAT:
        raise BadRequest('picture format is not correct')
    return f'images/profile/pictures/{random_str(10)}.{frmt}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    height = models.SmallIntegerField()
    picture = models.ImageField(upload_to=upload_picture_profile, null=True)
    note = models.TextField(null=True)

    def __str__(self):
        return f'{self.user} - profile'
