from django import forms
from .models import Cliente

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }
