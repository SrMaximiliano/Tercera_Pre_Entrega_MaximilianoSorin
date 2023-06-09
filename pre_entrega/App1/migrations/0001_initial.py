# Generated by Django 4.2 on 2023-05-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('curso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email15', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_d_usuario', models.CharField(default='', max_length=30)),
                ('contraseñas', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='vendedor_certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contraseñas', models.CharField(max_length=30)),
                ('nombre_d_usuario', models.CharField(default='', max_length=30)),
                ('nombre', models.CharField(default='', max_length=30)),
                ('apellido', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('DNI', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='vendedor_promocionado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contraseñas', models.CharField(max_length=30)),
                ('nombre_d_usuario', models.CharField(default='', max_length=30)),
                ('nombre', models.CharField(default='', max_length=30)),
                ('apellido', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('DNI', models.IntegerField(default=None)),
                ('Promo_code', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
