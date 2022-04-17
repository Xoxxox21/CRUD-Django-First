from django import forms
from django.forms import ModelForm
from login.models import user

class FormTambahUser(ModelForm):
    class Meta:
        model = user
        fields = '__all__'        
        Widget = {
            'username' : forms.TextInput({'class': 'form-control'}),
            'password' : forms.PasswordInput({'class': 'form-control'})
        }