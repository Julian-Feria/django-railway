# Generated by Django 5.0.7 on 2024-11-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_account', models.CharField(max_length=70, verbose_name='Nombre del correo')),
                ('email_account', models.EmailField(max_length=254, verbose_name='Correo de envio')),
                ('password_account', models.CharField(max_length=16, verbose_name='Contraseña de aplicacion')),
                ('is_active', models.BooleanField(default=False, verbose_name='¿Cuenta activa?')),
            ],
            options={
                'verbose_name': 'Credenciales',
                'verbose_name_plural': 'Credenciales',
            },
        ),
    ]
