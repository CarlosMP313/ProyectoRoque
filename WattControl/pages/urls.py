from pages.views import index
from pages.views import contacto
from pages.views import nosotros
from pages.views import productos
from pages.views import soporte
from pages.views import base
from django.urls import path,include
from. import views
    
urlpatterns = [
    path('', index, name="inicio"),
    path('base/', base),
    path('Contacto/', contacto, name="contacto"),
    path('Nosotros/', nosotros, name="nosotros"),
    path('Soporte/', soporte, name="soporte"),
    path('Productos/', productos, name="productos"),
    path('enviar-correos/', views.enviar_correosB, name='enviar_correosB'),
    path('enviar-correosContacto/', views.enviar_correoDia, name='enviar_correosC'),
   ]