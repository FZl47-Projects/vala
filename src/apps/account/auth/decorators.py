from functools import wraps
from django.conf import settings
from django.core.exceptions import PermissionDenied
from apps.account.models import User


def admin_required(roles=User.ADMIN_ROLES):
    def wrapper(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            user = request.user
            if user is None or user.is_anonymous:
                raise PermissionDenied
            role = user.role
            if not (role in roles):
                raise PermissionDenied
            return func(request, *args, **kwargs)

        return inner

    return wrapper


def admin_required_cbv(roles=User.ADMIN_ROLES):
    def wrapper(func):
        @wraps(func)
        def inner(self,request, *args, **kwargs):
            user = request.user
            if user is None or user.is_anonymous:
                raise PermissionDenied
            role = user.role
            if not (role in roles):
                raise PermissionDenied
            return func(self,request, *args, **kwargs)
        return inner
    return wrapper


def user_role_required_cbv(roles=User.ALL_USER_ROLES):
    def wrapper(func):
        @wraps(func)
        def inner(self,request, *args, **kwargs):
            user = request.user
            if user is None or user.is_anonymous:
                raise PermissionDenied
            role = user.role
            if not (role in roles):
                raise PermissionDenied
            return func(self,request, *args, **kwargs)
        return inner
    return wrapper
