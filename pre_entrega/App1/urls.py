from django.urls import path
from App1 import views

urlpatterns = [
   
    path('Inicio', views.Inicio, name="Inicio"), #este era nuestro primer view
    path('Perfil', views.Perfil, name="Perfil"),
    path('Vendedor_certificado', views.Vendedor_certificado, name="Vendedor_certificado"),
    path('Volverse_prime', views.Volverse_prime, name="Volverse_prime"),
    path("Iniciar_sesion", views.Iniciar_sesion, name="Iniciar_sesion"),
    path('Formulario_Iniciar_Sesion', views.Formulario_Iniciar_Sesion, name="Formulario_Iniciar_Sesion"),
    path('busquedaUsuario',views.busquedaUsuario,name="busquedaUsuario"),
    path('buscar/',views.buscar),



]