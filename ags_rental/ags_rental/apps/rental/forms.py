from django import forms
from inventory.models import Case, Device
from rental.models import Person, Rental
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RentalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.queryset = kwargs.pop('queryset', None)
        super().__init__(*args, **kwargs)
        if self.request and self.queryset:
            self.fields['cases'].initial = Case.objects.filter(id__in=self.queryset)
        self.fields['devices'].required = False
        print(self.request, self.queryset)

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))

    cases = forms.ModelMultipleChoiceField(
        queryset=Case.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    return_date = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}
    ))

    class Meta:
        model = Rental
        fields = (
            'person', 'cases', 'devices', 'return_date'
        )
