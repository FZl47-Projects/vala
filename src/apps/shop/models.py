from django.utils.translation import gettext as _
from django.db import models

from apps.account.models import User
from apps.core.models import BaseModel


# Products model
class Product(BaseModel):
    title = models.CharField(_('Product title'), max_length=255, default=_('No title'))
    description = models.TextField(_('Description'), default=_('No description'))

    selling_price = models.PositiveIntegerField(_('Selling price'), default=0)
    price = models.PositiveIntegerField(_('Price'), default=0)
    quantity = models.PositiveIntegerField(_('Remaining quantity'), default=0)
    discount = models.PositiveIntegerField(_('Price discount'), default=0, help_text=_('Percentage'))

    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.selling_price = self.price - (self.price * self.discount)
        super().save(*args, **kwargs)


# ProductImages model
class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name=_('Product'))
    image = models.ImageField(_('Image'), upload_to='images/products/')
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Product image')
        verbose_name_plural = _('Product images')

    def __str__(self):
        return f'{self.product} - {self.id}'

    def get_image_url(self):
        if self.image:
            return self.image.url


# OrderRequests model
class OrderRequest(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='order_requests', null=True, blank=True, verbose_name=_('User'))
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='orders_requests', null=True, blank=True, verbose_name=_('Product'))
    extra_data = models.TextField(_('Extra data'), null=True, blank=True)
    delivered = models.BooleanField(_('Id delivered'), default=False)

    class Meta:
        verbose_name = _('Order request')
        verbose_name_plural = _('Order requests')
        ordering = ('-id',)

    def __str__(self):
        return f'{self.user} - {self.product}'

    def get_date_created(self):
        return self.created_at.strftime('%Y-%m-%d')
