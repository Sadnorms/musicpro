import marshal
from rest_framework import serializers
from app.models import Producto, Marca, Categoria
from django.contrib.auth.models import User


class productoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Producto
        fields = ['nombreProducto' , 'precioProducto', 'stockProducto','descripcionProducto','categoriaProducto','marcaProducto', 'imagen']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombreCategoria' ]

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nombreMarca' ]


class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['username' , 'first_name', 'last_name','email','is_staff','is_superuser', 'date_joined', 'password']