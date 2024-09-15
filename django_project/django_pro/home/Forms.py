from django import forms
from .models import Registor
class DateInput(forms.DateInput):
    input_type='date'

class RegistorForm(forms.ModelForm):
    class Meta:
        model = Registor
        fields = '__all__'
        widgets={
            'Registor_date':DateInput(),
        }
        