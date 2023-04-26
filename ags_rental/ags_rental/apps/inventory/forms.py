from django import forms
from inventory.models import Case
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CaseForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))
    class Meta:
        model = Case
        fields = (
            'name', 'quantity', 'contains'
        )
