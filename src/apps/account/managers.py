from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from .enums import AccessChoices
from . import models


# Custom User manager
class UserManager(BaseUserManager):
    def create_admin_access(self, user):
        try:
            obj = models.Access.objects.get(title=AccessChoices.ADMIN)
        except models.Access.DoesNotExist:
            obj = models.Access.objects.create(title=AccessChoices.ADMIN)

        return obj

    def create_user(self, password=None, phone_number=None, verify=False):
        """ Creates and saves a User with the given data. """

        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password=None):
        """ Creates and saves a superuser with the given data. """

        if not phone_number:
            raise ValueError(_("Users must have a mobile number!"))

        user = self.create_user(password, phone_number)

        obj = self.create_admin_access(user)  # Create admin access
        user.access.add(obj)  # Set admin access

        user.is_admin = True  # Set as 'admin' user
        user.is_verified = True
        user.save(using=self._db)

        return user
