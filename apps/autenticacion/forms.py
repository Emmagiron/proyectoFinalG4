from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'imagen_perfil']

class IngresarUsuarioForm(forms.Form):
    username = forms.CharField(max_length=150, label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')