from django.db import models

SATISFACCCION = (
    ('1','ALTA'),
    ('2', 'MEDIA'),
    ('3','BAJA'),
)
class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='static/img')
    descripcionTrabajo = models.CharField(max_length=500)
    satisfaccion= models.CharField(max_length=6,choices=SATISFACCCION, default='1')