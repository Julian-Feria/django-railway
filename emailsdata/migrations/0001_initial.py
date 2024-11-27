# Generated by Django 5.0.7 on 2024-11-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Primer nombre')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('group', models.CharField(default='Group', max_length=50, verbose_name='Grupo')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Email',
            },
        ),
    ]
