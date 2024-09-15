from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class CreateNewUserForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(CreateNewUserForm, self).__init__(*args, **kwargs)
        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-control-lg'
    
    class Meta:
        model = User
        fields = ['username','password1','password2']
    
    


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username','class':'form-control form-control-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password','class':'form-control form-control-lg'}))

    class Meta:
        fields = ('username', 'password')