from django import forms
from inventory.models import Case, Device
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CaseForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))

    devices = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Case
        fields = (
            'name', 'quantity', 'devices'
        )


class DeviceForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Device
        fields = (
            'name', 'quantity'
        )
