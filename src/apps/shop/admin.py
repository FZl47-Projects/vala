from django.contrib import admin
from . import models


# Register Product model admin
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'quantity', 'selling_price', 'is_active')
    list_display_links = ('id', 'title')


# Register ProductImage model admin
@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')
    list_display_links = ('id', 'product')
