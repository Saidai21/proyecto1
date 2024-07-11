from django import forms
from .models import Cliente
from .models import Producto

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre_prod", "descripcion_prod", "precio", "imagen", "categoria"]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }
