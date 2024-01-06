from django import forms
from . import models


# Add Product form
class AddProductForm(forms.ModelForm):
    image = forms.ImageField(required=True, widget=forms.FileInput)

    class Meta:
        model = models.Product
        exclude = ('discount', 'selling_price', 'is_active', 'quantity')

    def save(self, commit=True):
        product = super(AddProductForm, self).save(commit=False)
        image = self.cleaned_data.get('image')

        if commit:
            product.save()

            if image:
                models.ProductImage.objects.create(product=product, image=image)

        return product


# Add OrderRequest form
class AddOrderRequestForm(forms.ModelForm):
    class Meta:
        model = models.OrderRequest
        fields = ('user', 'product', 'extra_data')
