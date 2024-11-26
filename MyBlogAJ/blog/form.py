from django import forms
from .models import Carta

class formularioPublicacion(forms.ModelForm):
    class Meta:
        model = Carta
        fields = ['titulo', 'contenido', 'autor']
