from django.db import models


"""
¿Como le hago para usar subclases? ¿Y cuentan para la cantidad de clases que pide la entrega, o al ser subclases no se las cuenta como una clase hecha?
"""
class Usuario(models.Model):
    nombre_d_usuario= models.CharField(max_length=30,null=False, default='')
    contraseñas= models.CharField(max_length=30,null=False, default='')
    email= models.EmailField(null=False, default='')

#class usuario_prime(Usuario):
#    nombre= models.CharField(max_length=30)
#    apellido= models.CharField(max_length=30)
#    email= models.EmailField()
# Es un futuro tipo de usuario a añadir!
class vendedor_certificado(models.Model):
    contraseñas= models.CharField(max_length=30)
    nombre_d_usuario= models.CharField(max_length=30,null=False, default='')
    nombre= models.CharField(max_length=30,null=False, default='')
    apellido= models.CharField(max_length=30,null=False, default='')
    email= models.EmailField(null=False, default='')
    DNI= models.IntegerField(default=None)
class vendedor_promocionado(models.Model):
    contraseñas= models.CharField(max_length=30)
    nombre_d_usuario= models.CharField(max_length=30,null=False, default='')
    nombre= models.CharField(max_length=30,null=False, default='')
    apellido= models.CharField(max_length=30,null=False, default='')
    email= models.EmailField(null=False, default='')
    DNI= models.IntegerField(default=None)
    Promo_code= models.CharField(max_length=30,null=False, default='')

