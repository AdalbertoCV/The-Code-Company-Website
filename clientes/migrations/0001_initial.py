# Generated by Django 4.1.4 on 2023-05-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='')),
                ('descripcionTrabajo', models.CharField(max_length=500)),
            ],
        ),
    ]
