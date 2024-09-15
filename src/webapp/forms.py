from django import forms
from .models import Record
import re
from django.core.exceptions import ValidationError



class MobileNumberInput(forms.widgets.TextInput):

    def __init__(self, attrs=None):

        super().__init__(attrs)
        self.attrs['placeholder'] = '+9705********'

#--(a.almajayda) : form to add new records 
class AddNewRecordForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AddNewRecordForm, self).__init__(*args, **kwargs)
        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control '


    def clean_mobile(self):

        mobile = self.cleaned_data['mobile']

        if not re.match(r'^(\+970|\+972)[0-9]+$', mobile):

            raise ValidationError('Invalid mobile number. It must start with +970 or +972.')

        return mobile

    class Meta:
        model = Record
        fields = ('first_name', 'last_name', 'birth_date', 'category', 'weight', 'tall', 'mobile', 'address',)
        widgets = {
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'mobile': MobileNumberInput,
            }



class UpdateRecordForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(UpdateRecordForm, self).__init__(*args, **kwargs)
        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control '

    def clean_mobile(self):

        mobile = self.cleaned_data['mobile']

        if not re.match(r'^(\+970|\+972)[0-9]+$', mobile):

            raise ValidationError('Invalid mobile number. It must start with +970 or +972.')

        return mobile


    class Meta:
        model = Record
        fields = ('first_name', 'last_name', 'birth_date', 'category', 'weight', 'tall', 'mobile', 'address',)
        widgets = {
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'mobile': MobileNumberInput,
            }