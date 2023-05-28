from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username' , 'password1' , 'password2']

class productoform(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombreProducto', 'precioProducto', 'stockProducto', 'descripcionProducto', 'categoriaProducto', 'marcaProducto', 'imagen']