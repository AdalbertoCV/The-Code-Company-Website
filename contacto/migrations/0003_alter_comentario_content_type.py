# Generated by Django 4.2.1 on 2023-05-28 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('contacto', '0002_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
