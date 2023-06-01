from django.urls import path
from contacto import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista_preguntas', views.lista_preguntas, name='lista_preguntas'),
    path('<int:pregunta_id>', views.detalle_preguntas, name='detalle_preguntas'),
    path('lista_telefonos', views.telefonos, name='lista_telefonos'),
    path('ubicacion', views.ubicacion, name='ubicacion'),  
]
