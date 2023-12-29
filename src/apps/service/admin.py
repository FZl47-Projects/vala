from django.contrib import admin
from . import models

admin.site.register(models.Operator)
admin.site.register(models.OperatorCategory)
admin.site.register(models.OperatorWorkSample)