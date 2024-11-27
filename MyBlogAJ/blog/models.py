from django.db import models

# Create your models here.
from django.db import models

# Este modelo fue creado por Andres Urango
class Carta(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100, default='Anonimo')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
