from django.shortcuts import render
from .models import cliente

def lista_clientes(request):
    clientes = cliente.objects.all()
    contexto = {'clientes': clientes}
    return render(request, 'lista_clientes.html', contexto)