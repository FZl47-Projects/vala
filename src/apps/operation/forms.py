from django import forms
from . import models


# AddCounseling form
class AddCounselingForm(forms.ModelForm):
    class Meta:
        model = models.Counseling
        fields = ('user', 'title', 'description', 'file')
