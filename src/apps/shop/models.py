from django.utils.translation import gettext as _
from django.db import models

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
