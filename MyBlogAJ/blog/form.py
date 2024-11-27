from django import forms
from .models import Carta

# Este formulario fue creado por Andres Urango
class formularioPublicacion(forms.ModelForm):
    class Meta:
        model = Carta
        fields = ['titulo', 'contenido', 'autor']
