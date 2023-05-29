from django.db import models
from django.conf import settings

class Pregunta(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField()
    fecha = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='comentario', null=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    contenido = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"comentario de {self.nombre}: {self.contenido}"