from django.shortcuts import render
from .models import Persona


def VerPersonal(request):
    personas = Persona.objects.all() 
    context = {
        'personas': personas
    }
    return render(request, 'ver_personal.html', context)