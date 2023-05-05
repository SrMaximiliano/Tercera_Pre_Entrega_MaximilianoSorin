from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *
from App1.forms import *

def Inicio(request):
    return render(request,'App1/Inicio.html')
def Perfil(request):
    return render(request,'App1/Perfil.html')
def Vendedor_certificado(request):
    return render(request,'App1/Vendedor_certificado.html')
def Volverse_prime(request):
    return render(request,'App1/Volverse_prime.html')
def Iniciar_sesion(request):
    return render(request,'App1/Iniciar_sesion.html')
def Formulario_Iniciar_Sesion(request):
      if request.method == "POST":
            miFormulario = UsuariosFormularios(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  usuario = Usuario(contraseñas=informacion['contraseñas'],nombre_d_usuario=informacion['nombre_d_usuario'])#,email=informacion['email'])
                  usuario.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = UsuariosFormularios()
 
      return render(request, "App1/Formulario_Iniciar_Sesion.html", {"miFormulario": miFormulario})
def busquedaUsuario(request):
     return render(request,'App1/busquedaUsuario.html')
def buscar(request):
    if request.GET['usuario']:
          usuario = request.GET['usuario']
          usuarios= Usuario.objects.filter(usuario__icontains=usuario)

          return render(request,'App1/resultadosBusqueda.html', {"Usuarios":usuarios, "Contraseñas": usuario })
    else:
          respuesta= "No enviaste datos"

    return HttpResponse(respuesta)
