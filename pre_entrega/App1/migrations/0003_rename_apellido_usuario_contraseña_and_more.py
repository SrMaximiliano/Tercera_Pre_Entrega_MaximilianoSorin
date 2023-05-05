# Generated by Django 4.2 on 2023-05-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_usuario_vendedor_certificado_vendedor_promocionado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='apellido',
            new_name='contraseña',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='nombre_d_usuario',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
