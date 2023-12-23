from functools import wraps
from django.core.exceptions import PermissionDenied
from apps.account.models import User


def admin_required_cbv(func):
    def wrapper(self, request, *args, **kwargs):
        user = request.user
        if user is None or user.is_anonymous:
            raise PermissionDenied
        role = user.role
        if not (role in User.ADMIN_ROLES):
            raise PermissionDenied
        return func(self, request, *args, **kwargs)

    return wrapper


def super_admin_required_cbv(func):
    def wrapper(self, request, *args, **kwargs):
        user = request.user
        if user is None or user.is_anonymous:
            raise PermissionDenied
        role = user.role
        if not (role in User.SUPER_USER_ROLES):
            raise PermissionDenied
        return func(self, request, *args, **kwargs)

    return wrapper


def user_role_required_cbv(roles=User.ALL_USER_ROLES):
    def wrapper(func):
        @wraps(func)
        def inner(self, request, *args, **kwargs):
            user = request.user
            if user is None or user.is_anonymous:
                raise PermissionDenied
            role = user.role
            if not (role in roles):
                raise PermissionDenied
            return func(self, request, *args, **kwargs)
        return inner

    return wrapper
