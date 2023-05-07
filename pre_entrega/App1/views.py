from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *
from App1.forms import *
from django.views.generic import ListView


def Inicio(request):
    return render(request,'App1/Inicio.html')
#def Perfil(request):
#    return render(request,'App1/Perfil.html')
# No esta siendo usada por ahora. Sera usada mas tarde
def Vendedor_Promocionado(request):
    return render(request,'App1/Vendedor_Promocionado.html')
def Volverse_prime(request):
    return render(request,'App1/Volverse_prime.html')
def Crear_cuenta(request):
    return render(request,'App1/Crear_cuenta.html')


#Formularios para crear usuarios, vendedores con la promocion que es basicamente publicidad y vendedores certificados
def Formulario_crearusuario(request):
      if request.method == "POST":
            miFormulario = UsuariosFormularios(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  usuario = Usuario(contraseñas=informacion['contraseñas'],nombre_d_usuario=informacion['nombre_d_usuario'],email=informacion['email'])
                  usuario.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = UsuariosFormularios()
 

      return render(request, "App1/Formulario_crearusuario.html", {"miFormulario": miFormulario})
def Formulario_Promocion_vendedor(request):
      if request.method == "POST":
            miFormulario = Promo_Vendedor_Formularios(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  usuario = vendedor_promocionado(contraseñas=informacion['contraseñas'],nombre_d_usuario=informacion['nombre_d_usuario'],email=informacion['email'],nombre=informacion["nombre"],
                                                  apellido=informacion["apellido"], DNI=informacion["DNI"], Promo_code=informacion["Promo_code"])
                  usuario.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = Promo_Vendedor_Formularios()
 
      return render(request, "App1/Formulario_Promocion_vendedor.html", {"miFormulario": miFormulario})
def Formulario_Vendedor_certificado(request):
      if request.method == "POST":
            miFormulario = Vendedor_C_Formularios(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  usuario = vendedor_certificado(contraseñas=informacion['contraseñas'],nombre_d_usuario=informacion['nombre_d_usuario'],email=informacion['email'],nombre=informacion["nombre"],
                                                  apellido=informacion["apellido"], DNI=informacion["DNI"])
                  usuario.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = Vendedor_C_Formularios()
 
      return render(request, "App1/Formulario_Vendedor_certificado.html", {"miFormulario": miFormulario})


#Funcion y clase para buscar Usuarios. 
class BookSearchView(ListView):
    model = Usuario
    template_name = 'busquedaUsuario.html'
    context_object_name = 'Usuarios encontrados'

    def get_queryset(self):
        queryset = super().get_queryset()
        nombre_d_usuario = self.request.GET.get('nombre_d_usuario')
        contraseñas = self.request.GET.get('contraseñas')
        email = self.request.GET.get('email')
        if nombre_d_usuario:
            queryset = queryset.filter(nombre_d_usuario__icontains=nombre_d_usuario)
        if contraseñas:
            queryset = queryset.filter(contraseñas__icontains=contraseñas)
        if email:
            queryset = queryset.filter(email__icontains=email)
        return queryset
    
def buscar_usuario(request):
    usuarios = Usuario.objects.none()
    if request.method == 'GET':
        form = BookSearchForm(request.GET)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('nombre_usuario')
            usuarios = Usuario.objects.filter(nombre_d_usuario__icontains=nombre_usuario)
    else:
        form = BookSearchForm()
    return render(request, 'App1/busquedaUsuario.html', {'form': form, 'Usuarios_encontrados': usuarios})
"""
def buscar(request):
    if request.GET['usuario']:
          usuario = request.GET['usuario']
          usuarios= Usuario.objects.filter(usuario__icontains=usuario)

          return render(request,'App1/resultadosBusqueda.html', {"Usuarios":usuarios, "Contraseñas": usuario })
    else:
          respuesta= "No enviaste datos"

    return HttpResponse(respuesta)
"""