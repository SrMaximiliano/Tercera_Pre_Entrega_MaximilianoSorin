from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    curso= models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email15= models.EmailField()
    profesion= models.CharField(max_length=30)

"""
¿Como le hago para usar subclases? ¿Y cuentan para la cantidad de clases que pide la entrega, o al ser subclases no se las cuenta como una clase hecha?
"""
class Usuario(models.Model):
    nombre_d_usuario= models.CharField(max_length=30)
    contraseñas= models.CharField(max_length=30)
    email0= models.EmailField(unique=True)
#class usuario_prime(Usuario):
#    nombre= models.CharField(max_length=30)
#    apellido= models.CharField(max_length=30)
#    email= models.EmailField()
class vendedor_certificado(models.Model):
    nombre_d_usuario1= models.CharField(max_length=30)
    nombre1= models.CharField(max_length=30)
    apellido1= models.CharField(max_length=30)
    email1= models.EmailField()
    DNI1= models.IntegerField()
class vendedor_promocionado(models.Model):
    nombre_d_usuario= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email2= models.EmailField()
    DNI= models.IntegerField()
    Promo_code= models.CharField(max_length=15)

