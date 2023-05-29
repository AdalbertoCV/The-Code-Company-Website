from django.urls import path
from clientes import views

urlpatterns = [
    path('', views.lista_clientes, name='clientes'),    
]
