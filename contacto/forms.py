from django.forms import ModelForm 
from .models import Comentario

class FormComentario(ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'email', 'contenido', 'active')

