from django.contrib import admin
from django.urls import path, include
from tcc.views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('contacto/', include('contacto.urls')),
    path('clientes/', include('clientes.urls')),
    path('servicios/', include('servicios.urls')),
]

urlpatterns += staticfiles_urlpatterns()
