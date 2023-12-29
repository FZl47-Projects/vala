from django.forms import ModelForm
from . import models


class OperatorCategoryAdd(ModelForm):
    class Meta:
        model = models.OperatorCategory
        fields = '__all__'


class OperatorAdd(ModelForm):
    class Meta:
        model = models.Operator
        fields = '__all__'
