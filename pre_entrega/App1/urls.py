from django.urls import path
from App1 import views
from .views import BookSearchView

urlpatterns = [
   
    path('Inicio', views.Inicio, name="Inicio"), #este era nuestro primer view
#    path('Perfil', views.Perfil, name="Perfil"),
    path('Vendedor_Promocionado', views.Vendedor_Promocionado, name="Vendedor_Promocionado"),
    path('Volverse_prime', views.Volverse_prime, name="Volverse_prime"),
    path("Crear_cuenta", views.Crear_cuenta, name="Crear_cuenta"),
    path('Formulario_crearusuario', views.Formulario_crearusuario, name="Formulario_crearusuario"),
    path("Formulario_Vendedor_certificado", views.Formulario_Vendedor_certificado, name="Formulario_Vendedor_certificado"),
    path("Formulario_Promocion_vendedor", views.Formulario_Promocion_vendedor, name="Formulario_Promocion_vendedor"),
    path('busquedaUsuario/', views.buscar_usuario, name='busquedaUsuario'),


]