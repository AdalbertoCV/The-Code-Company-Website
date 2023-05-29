from django.contrib import admin
from .models import Pregunta, Comentario

class PreguntaAdmin(admin.ModelAdmin):
    fields = ('titulo', 'slug', 'contenido')
    prepopulated_fields = {'slug':('titulo',)}
    
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Comentario)
