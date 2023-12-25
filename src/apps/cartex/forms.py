from django import forms
from . import models


class MeetingAddForm(forms.ModelForm):
    description = forms.CharField(required=False)
    time_start = forms.TimeField(required=False)
    time_end = forms.TimeField(required=False)

    class Meta:
        model = models.Meeting
        exclude = ('number_id',)


class AreaBodyAddForm(forms.ModelForm):
    note = forms.CharField(required=False)

    class Meta:
        model = models.AreaBody
        fields = '__all__'


class FormSetCustom:
    _is_valid = None

    def get_fields(self):
        raise NotImplementedError

    def get_once_fields(self):
        raise NotImplementedError

    def get_form_model(self):
        raise NotImplementedError

    def get_iter_key(self):
        raise NotImplementedError

    def __init__(self, data):
        forms_cleaned = []
        iter_key = self.get_iter_key()
        forms = data.getlist(iter_key, [])
        for i, form in enumerate(forms):
            data_form = {**data}
            fields_name = self.get_fields()
            fields_once_name = self.get_once_fields()
            for field in fields_name:
                data_form[field] = data.getlist(field, [])[i]
            for field in fields_once_name:
                data_form[field] = data.get(field)
            forms_cleaned.append(self.get_form_model()(data_form))
        self.forms_cleaned = forms_cleaned

    def is_valid(self):
        if all([f.is_valid() for f in self.forms_cleaned]):
            self._is_valid = True
            return True
        return False

    def errors(self):
        forms = {}
        for i, f in enumerate(self.forms_cleaned, 1):
            forms[f'form-{i}'] = f.erros
        return forms

    def save(self):
        if not self._is_valid:
            raise ValueError('You must check FormSet by is_valid method before save')
        for form in self.forms_cleaned:
            form.save()
        return self.forms_cleaned


# handle add many AreaBody object
class AreaBodyFormSetAdd(FormSetCustom):

    def get_form_model(self):
        return AreaBodyAddForm

    def get_fields(self):
        return (
            'note', 'area_code', 'area_name', 'intensity'
        )

    def get_once_fields(self):
        return (
            'meeting',
        )

    def get_iter_key(self):
        return 'area_code'


class AreaBodyUpdateForm(forms.ModelForm):
    class Meta:
        model = models.AreaBody
        fields = ('intensity', 'note')
