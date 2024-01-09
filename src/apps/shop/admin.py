from django.contrib import admin
from .models import Product, ProductImage, OrderRequest


# Register ProductImage as inline
class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


# Register Product model admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'quantity', 'selling_price')
    list_display_links = ('id', 'title')
    list_filter = ('is_active',)
    search_fields = ('title',)
    inlines = (ProductImageInline,)


# Register OrderRequest model admin
@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user')
    list_display_links = ('id', 'product')
    search_fields = ('product__title', 'user__phone_number')
    list_filter = ('delivered',)
