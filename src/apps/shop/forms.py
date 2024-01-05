from django import forms
from . import models


# Add Product form
class AddProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        exclude = ('discount', 'selling_price', 'is_active')


# Add ProductImage form
class AddProductImageForm(forms.ModelForm):
    class Meta:
        model = models.ProductImage
        fields = ('product', 'image')
