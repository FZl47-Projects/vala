from django import forms
from . import models


# AnswerTest form
class AnswerTestForm(forms.ModelForm):
    class Meta:
        model = models.Test
        fields = ('user', 'answer')


# AddCounseling form
class AddCounselingForm(forms.ModelForm):
    class Meta:
        model = models.Counseling
        fields = ('user', 'title', 'description', 'file')
