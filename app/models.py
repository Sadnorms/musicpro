from django.db import models

class Marca(models.Model):
    nombreMarca = models.TextField(max_length=100)
    activoMarca = models.BooleanField()

    def __str__(self):
        return self.nombreMarca

class Categoria(models.Model):
    nombreCategoria = models.TextField(max_length=100)
    activoCategoria = models.BooleanField()
    
    def __str__(self):
        return self.nombreCategoria
    
class Producto(models.Model):
    nombreProducto = models.CharField(max_length=90)
    precioProducto = models.IntegerField()
    stockProducto = models.IntegerField()
    descripcionProducto = models.TextField(max_length=600)
    categoriaProducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marcaProducto = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.nombreProducto