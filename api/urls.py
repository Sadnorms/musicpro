from django.urls import path
from api.views import apicategoria,apimarca,apiproducto,apiuser,apiProductoDetalle

urlpatterns = [
    path('producto', apiproducto, name='apiProducto'),
    path('categoria', apicategoria, name='apiProducto'),
    path('marca', apimarca, name='apiProducto'),
    path('user', apiuser, name='apiProducto'),
    path('apiProductoDetalle/<buscarId>/', apiProductoDetalle, name='ProductoDetalle'),
]