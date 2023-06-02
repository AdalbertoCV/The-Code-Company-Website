from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from personal import views


urlpatterns = [
    
    path('', views.VerPersonal, name="ver_personal"),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

