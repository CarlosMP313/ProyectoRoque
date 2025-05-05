from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm

class LoginFrom(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario',
                                                               'name': 'nombre','id':'nombre'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña',
                                                                   'name': 'password','id':'password'}))


class RegistroForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario',
                                                               'name': 'nombre','id':'nombre'}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico',
                                                             'name': 'correo','id':'correo'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña',
                                                                   'name': 'password','id':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña',
                                                                   'name': 'password-confirm','id':'password-confirm'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
