"""
URL configuration for NetSecure project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Servicios import views as servicios_views
from Información import views as sobre_nosotros_views
from Blog import views as blog_views
from Ingreso import views as ingresar_views
from Inicio import views as Inicio_views
from Vulnerabilidades import views as Vulnerabilidades_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio_views.inicio, name='Inicio'),
    path('servicios/', servicios_views.servicios, name='Servicios'),
    path('sobre-nosotros/', sobre_nosotros_views.sobre_nosotros, name='Sobre Nosotros'),
    path('blog/', blog_views.blog, name='blog'),
    
    # Rutas relacionadas con la autenticación
    path('registrar/', ingresar_views.registrar, name='Registrar'),
    path('iniciar_sesion/', ingresar_views.iniciar_sesion, name='Iniciar Sesion'),
    path('cerrar_sesion/', ingresar_views.cerrar_sesion, name='Cerrar Sesion'),

    # Rutas protegidas (sólo accesibles si el usuario está autenticado)
    path('perfil/', ingresar_views.perfil, name='Perfil'),
    path('nuevo_escaneo/', ingresar_views.nuevo_escaneo, name='Nuevo Escaneo'),
    path('sql_injection/', Vulnerabilidades_views.sql_injection, name='Vulnerabilidad SQLI'),
]