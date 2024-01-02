from django import template

register = template.Library()


# Register UserAccessCheck
@register.filter
def has_access(user, value):
    return user.has_specific_access(value)
