# Generated by Django 4.2 on 2023-05-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_delete_entregable_delete_estudiante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor_certificado',
            name='DNI1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vendedor_promocionado',
            name='DNI',
            field=models.IntegerField(),
        ),
    ]
