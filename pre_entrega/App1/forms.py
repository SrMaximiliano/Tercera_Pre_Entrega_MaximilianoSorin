from django import forms
 
#class CursoFormulario(forms.Form):
#    id= forms.IntegerField()
#    nombre = forms.CharField()
#    curso = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)    

class UsuariosFormularios(forms.Form):
    nombre_d_usuario= forms.CharField(max_length=30)
    email1= forms.EmailField()
    contraseñas= forms.CharField(max_length=30)

class Vendedor_C_Formularios(forms.Form):
    nombre_d_usuario= forms.CharField(max_length=30)
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email2= forms.EmailField()
    DNI= forms.IntegerField()

class Promo_Vendedor_Formularios(forms.Form):
    nombre_d_usuario= forms.CharField(max_length=30)
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email3= forms.EmailField()
    DNI= forms.IntegerField()
    Promo_code= forms.CharField(min_length=15, max_length=15)