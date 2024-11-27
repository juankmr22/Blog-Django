from django.urls import path
from . import views

urlpatterns = [
    # esta url fue creada por juan amaya
    path('', views.publicacion, name='publicacionurl'),
    # esta url fue creada por Andres Urango
    path('detalle/<int:publicacion_id>/', views.detallePublicacion, name='detallePublicacionurl'),
    # esta url fue creada por Andres Urango
    path('crear/', views.crearPublicacion, name='crearPublicacionurl'),

]
