from django.shortcuts import render, redirect
from .forms import  CustomUserForm
from .forms import productoform
from django.contrib.auth import  authenticate, login
from app.models import Marca, Categoria, Producto

def indexView(request):
    return render(request, 'index.html', {})

#USER ----------------------------------------------------------------------------------------------------
def registro_usuario(request): 
    contexto = {}
    data = {
        'form':CustomUserForm()
    } 
    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST )
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to= 'index')
        data ["form"] = formulario
    return render (request, 'registrar.html' , data )

#MARCA ----------------------------------------------------------------------------------------------------
def marcaLeerView(request, id):
    contexto = {}
    try:
        fila = Marca.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    contexto["productCategories"] = productCategories
    return render(request, 'marca.html', contexto)

def marcaView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombreMarca = request.POST["txtNombre"]
        activoMarca = False
        if 'chkActivo' in request.POST:
            activoMarca = True
        # detectar que botón fue presionado
        if 'btnGrabar' in request.POST:
            if len(nombreMarca) < 5:
                contexto = {'error': 'El nombre del tipo de usuario debe tener como minimo 5 caracteres'}
            else:
                if id < 1: # ORM Object relational Mapping
                    Marca.objects.create(nombreMarca = nombreMarca, activoMarca = activoMarca) 
                else:
                    fila = Marca.objects.get(pk = id)
                    fila.nombreMarca = nombreMarca
                    fila.activoMarca = activoMarca
                    fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        
        elif 'btnListar' in request.POST:
            listado = Marca.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Marca.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    contexto["productCategories"] = productCategories        
    return render(request, 'marca.html', contexto)

#CATEGORIA ----------------------------------------------------------------------------------------------------
def categoriaLeerView(request, id):
    contexto = {}
    try:
        fila = Categoria.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    contexto["productCategories"] = productCategories
    return render(request, 'categoria.html', contexto)

def categoriaView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombreCategoria = request.POST["txtNombre"]
        activoCategoria = False
        if 'chkActivo' in request.POST:
            activoCategoria = True

        # detectar que botón fue presionado

        if 'btnGrabar' in request.POST:
            if len(nombreCategoria) < 5:
                contexto = {'error': 'El nombre de la marca debe tener como minimo 5 caracteres'}
            else:
                if id < 1: # ORM Object relational Mapping
                    Categoria.objects.create(nombreCategoria = nombreCategoria, activoCategoria = activoCategoria) 
                else:
                    fila = Categoria.objects.get(pk = id)
                    fila.nombreCategoria = nombreCategoria
                    fila.activoCategoria = activoCategoria
                    fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        elif 'btnListar' in request.POST:
            listado = Categoria.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Categoria.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}

    productCategories = Categoria.objects.all()
    contexto["productCategories"] = productCategories        
    return render(request, 'categoria.html', contexto)

#PRODUCTO ----------------------------------------------------------------------------------------------------
def crearProductoView(request): 
    data = {
        'form' : productoform()
    }
    if request.method == 'POST':
        formulario = productoform(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
    return render (request, 'crearProducto.html' , data )


def productosView(request): 
    data = {
        'productos' : Producto.objects.all()
    }
    return render (request, 'productos.html', data)

def modificarProductoLeerView(request, id):
    contexto = {}
    try:
        fila = Producto.objects.get(pk = id)
        contexto = {'fila': fila}
    except:
        contexto = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    productBrand = Marca.objects.all()
    contexto["productCategories"] = productCategories
    contexto["productBrand"] = productBrand

    return render(request, 'modificarProducto.html', contexto)

def modificarProductoView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombreProducto = request.POST["txtNombre"]
        precioProducto = request.POST["txtPrecioProducto"]
        stockProducto = request.POST["txtStockProducto"]
        descripcionProducto = request.POST["txtDescripcion"]
        categoriaProducto = request.POST["ctProducto"]
        marcaProducto = request.POST["ctMarca"]
        

        # detectar que botón fue presionado
        if 'btnGrabar' in request.POST:
            if len(nombreProducto) < 5:
                contexto = {'error': 'El nombre del producto debe tener como minimo 5 caracteres'}
            elif len(precioProducto) < 3:
                contexto = {'error': 'El  precio producto debe tener como minimo 3 caracteres'}
            elif len(stockProducto) < 1:
                contexto = {'error': 'El stock producto debe tener como minimo 1 caracteres'}
            elif (categoriaProducto) == '0':
                contexto = {'error': 'Debe seleccionar la marca del producto'}
            elif (marcaProducto) == '0':
                contexto = {'error': 'Debe seleccionar la marca del producto'}

        
            elif id < 1: # ORM Object relational Mapping
                Producto.objects.create(nombreProducto = nombreProducto, precioProducto = precioProducto, stockProducto = stockProducto, descripcionProducto = descripcionProducto, categoriaProducto = categoriaProducto, marcaProducto = marcaProducto)
                contexto = {'mensaje': 'Los datos fueron guardados'}  
            else:
                fila = Producto.objects.get(pk = id)
                fila.nombreProducto = nombreProducto
                fila.precioProducto = precioProducto
                fila.stockProducto = stockProducto
                fila.descripcionProducto = descripcionProducto
                fila.categoriaProducto = categoriaProducto
                fila.marcaProducto = marcaProducto
                fila.save()     
                contexto = {'mensaje': 'Los datos fueron guardados'}

        elif 'btnListar' in request.POST:
            listado = Producto.objects.all()
            contexto = {'listado': listado }
        elif 'btnEliminar' in request.POST:
            try:
                fila = Producto.objects.get(pk = id)
                fila.delete()
                contexto = {'mensaje': 'Los datos fueron eliminados'}
            except:
                contexto = {'error': 'Debe seleccionar item a eliminar'}

    productCategories = Categoria.objects.all()
    productBrand = Marca.objects.all()
    contexto["productCategories"] = productCategories
    contexto["productBrand"] = productBrand

    return render(request, 'modificarProducto.html', contexto)