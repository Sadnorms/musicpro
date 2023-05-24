from django.urls import path
from . import views
urlpatterns = [path('index', views.indexView, name="index"),
               path('registrar/', views.registro_usuario, name="registrar"),]