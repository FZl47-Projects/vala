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


# AddSkinRoutine form
class AddSkinRoutineForm(forms.ModelForm):
    class Meta:
        model = models.SkinRoutine
        exclude = ('answer', 'is_active')


# AnswerRoutine form
class AnswerRoutineForm(forms.ModelForm):
    class Meta:
        model = models.SkinRoutine
        fields = ('user', 'answer')
