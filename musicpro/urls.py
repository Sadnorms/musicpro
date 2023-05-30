"""
URL configuration for musicpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from app import views
from carro.views import agregar_producto, restar_producto, restar_producto_n,eliminar_producto,limpiar_carrito
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexView, name="index"),
    path('registrar/', views.registro_usuario, name="registrar"),
    path('api/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('app/', include('app.urls')),
    path('add/<int:producto_id>/', agregar_producto, name="Add"),
    path('remove/<int:producto_id>/', restar_producto, name="Sub"),
    path('remove/<int:producto_id>/<int:n>/', restar_producto_n, name="SubN"),
    path('delete/<int:producto_id>/', eliminar_producto, name="Del"),
    path('clear/', limpiar_carrito, name="CLS")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)