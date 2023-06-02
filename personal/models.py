from django.db import models
from personal.validators import image_validator

class Persona(models.Model):
    nombre_completo = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    url_facebook = models.URLField(max_length=200)
    url_instagram = models.URLField(max_length=200)
    habilidades = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='imgs_personal/', validators=[image_validator])
    certificaciones = models.TextField(max_length=500)
    idiomas = models.TextField(max_length=100)
    pasatiempo = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.nombre_completo}"

    
