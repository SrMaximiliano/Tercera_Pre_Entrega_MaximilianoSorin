from django import forms
 
#class CursoFormulario(forms.Form):
#    id= forms.IntegerField()
#    nombre = forms.CharField()
#    curso = forms.IntegerField()

class UsuariosFormularios(forms.Form):
    nombre_d_usuario= forms.CharField(max_length=30)
    email= forms.EmailField()
    contraseñas= forms.CharField(max_length=30)

class Vendedor_C_Formularios(forms.Form):
    contraseñas= forms.CharField(max_length=30)
    nombre_d_usuario= forms.CharField(max_length=30)
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    DNI= forms.IntegerField()

class Promo_Vendedor_Formularios(forms.Form):
    contraseñas= forms.CharField(max_length=30)
    nombre_d_usuario= forms.CharField(max_length=30)
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    DNI= forms.IntegerField()
    Promo_code= forms.IntegerField()

class BookSearchForm(forms.Form):
    nombre_usuario = forms.CharField(label='Nombre de usuario', required=False)
