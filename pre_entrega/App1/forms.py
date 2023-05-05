from django import forms
 
#class CursoFormulario(forms.Form):
#    id= forms.IntegerField()
#    nombre = forms.CharField()
#    curso = forms.IntegerField()
    
class UsuariosFormularios(forms.Form):
    contraseña= forms.CharField(max_length=30)
    nombre_d_usuario= forms.CharField(max_length=30)
    email= forms.EmailField()
