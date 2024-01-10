from django.contrib import admin
from . import models


# Register OperatorCategory model admin
@admin.register(models.OperatorCategory)
class OperatorCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


# Register Operator as Inline
class OperatorWorkSampleInline(admin.StackedInline):
    model = models.OperatorWorkSample
    extra = 0


# Register Operator model admin
@admin.register(models.Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    search_fields = ('name',)

    inlines = (OperatorWorkSampleInline,)


# Register OperatorReserve model admin
@admin.register(models.OperatorReserve)
class OperatorReserveAdmin(admin.ModelAdmin):
    list_display = ('id', 'operator', 'phonenumber')
    list_display_links = ('id', 'operator')
    search_fields = ('phonenumber', 'operator')

