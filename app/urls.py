from django.urls import path

from . import views
urlpatterns = [path('index', views.indexView, name="index"),
               path('registrar/', views.registro_usuario, name="registrar"),
               path('marca', views.marcaView, name="marca"),
               path('marca/<int:id>/', views.marcaLeerView, name="marca"),
               path('categoria', views.categoriaView, name="categoria"),
               path('categoria/<int:id>/', views.categoriaLeerView, name="categoria"),
                path('crearProducto/', views.crearProductoView,  name='crearProducto'),
                path('tienda/', views.tiendaView,  name='tienda' ) ,
                path('modificarProducto', views.modificarProductoView, name="modificarProducto"),
                path('modificarProducto/<int:id>/', views.modificarProductoLeerView, name="modificarProducto"),
                ]


