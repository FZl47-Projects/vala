from django import forms
from . import models


# Add DietProgram form
class AddDietProgramForm(forms.ModelForm):
    class Meta:
        model = models.DietProgram
        fields = ('user',)


# Update DietProgram form
class UpdateDietProgramForm(forms.ModelForm):
    class Meta:
        model = models.DietProgram
        exclude = ('status', 'is_active')


# Add ExerciseProgram form
class AddExerciseProgramForm(forms.ModelForm):
    class Meta:
        model = models.ExerciseProgram
        fields = ('user',)


# Update ExerciseProgram form
class UpdateExerciseProgramForm(forms.ModelForm):
    class Meta:
        model = models.DietProgram
        exclude = ('status', 'is_active')
