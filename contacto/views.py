from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Pregunta
from .forms import FormComentario

def inicio(request):
    return render(request, 'homeOfi.html')

def telefonos(request):
    return render(request, 'telefonos.html')

def ubicacion(request):
    return render(request, 'ubicacion_geo.html')

def lista_preguntas(request):
    preguntas = Pregunta.objects.all()
    context = {
        'preguntas': preguntas
    }
    return render(request, 'lista_preguntas.html', context)

def detalle_preguntas(request, pregunta_id):
    preguntas = Pregunta.objects.get(id=pregunta_id) 
    comentario = preguntas.comentario.filter(active=True)
    if request.method == 'POST':
        form = FormComentario(request.POST)
        if form.is_valid():
            nuevo_form = form.save(commit=False)
            nuevo_form.preguntas = preguntas
            nuevo_form.save()
            return HttpResponseRedirect("")
    else:
        form = FormComentario
    context = {
        'preguntas': preguntas,
        'comentario': comentario,
        'form': form
    }   
    return render(request, 'detalle_preguntas.html', context)
