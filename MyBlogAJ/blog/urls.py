from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicacion, name='publicacionurl'),
    path('detalle/<int:publicacion_id>/', views.detallePublicacion, name='detallePublicacionurl'),
    path('crear/', views.crearPublicacion, name='crearPublicacionurl'),

]
