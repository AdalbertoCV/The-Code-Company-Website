from django.urls import path
from acerca import views

urlpatterns = [
    path('mision', views.mision, name='mision'),  
    path('vision', views.vision, name='vision'),  
    path('valores', views.valores, name='valores'),  
]
