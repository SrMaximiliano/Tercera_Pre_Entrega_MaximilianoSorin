# Generated by Django 4.2 on 2023-05-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0009_alter_vendedor_promocionado_promo_code'),
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
        migrations.AlterField(
            model_name='vendedor_promocionado',
            name='Promo_code',
            field=models.CharField(default='', max_length=30),
        ),
    ]
