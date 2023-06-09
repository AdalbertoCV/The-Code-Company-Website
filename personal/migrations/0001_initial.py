# Generated by Django 4.2.1 on 2023-06-01 20:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('url_facebook', models.URLField()),
                ('url_instagram', models.URLField()),
                ('imagen', models.ImageField(upload_to='img/imgs_personal/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], code='formato_invalido', message='Sólo se permite formato PNG, JPEG, JPG.')])),
                ('habilidades', models.TextField(max_length=500)),
                ('certificaciones', models.TextField(max_length=500)),
                ('idiomas', models.TextField(max_length=100)),
                ('pasatiempo', models.TextField(max_length=500)),
            ],
        ),
    ]
