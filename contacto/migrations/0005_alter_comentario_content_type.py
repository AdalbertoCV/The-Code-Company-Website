# Generated by Django 4.2.1 on 2023-05-29 00:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('contacto', '0004_comentario_padre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
    ]