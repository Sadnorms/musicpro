from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from carro.Carrito import Carrito
from app.models import Producto

def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    productos = Producto.objects.all()
    return render(request, "productos.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def restar_producto_n(request, producto_id, n):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    for x in range(n):
        carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")