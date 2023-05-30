from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.models import User
from app.models import Producto, Marca , Categoria 
from api.serializers import  productoSerializer , MarcaSerializer, CategoriaSerializer, UserSerializer

@csrf_exempt
@api_view(('POST', 'GET'))
def apiproducto(request):
    if request.method ==  'GET':
        pro = Producto.objects.all()
        serializer = productoSerializer(pro, many=True)
        return Response(serializer.data)
    elif request.method ==  'POST':
        data = JSONParser().parse(request)
        serializer = productoSerializer(data = data)
        if serializer.os_valid():
            serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(('POST', 'GET'))
def apimarca(request):
    if request.method ==  'GET':
        marca = Marca.objects.all()
        serializer = MarcaSerializer(marca, many=True)
        return Response(serializer.data)
    elif request.method ==  'POST':
        data = JSONParser().parse(request)
        serializer = MarcaSerializer(data = data)
        if serializer.os_valid():
            serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(('POST', 'GET'))
def apicategoria(request):
    if request.method ==  'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria , many=True)
        return Response(serializer.data)
    elif request.method ==  'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data = data)
        if serializer.os_valid():
            serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(('POST', 'GET'))
def apiuser(request):
    if request.method ==  'GET':
        user = User.objects.all()
        serializer = UserSerializer(user , many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def apiProductoDetalle(request, buscarId):
    try:
        id = int(buscarId)
        producto = Producto.objects.get(pk=id)
    except:
        return Response(status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = productoSerializer(Producto)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = productoSerializer(Producto, data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method ==  'POST':
        data = JSONParser().parse(request)
        serializer = productoSerializer(data = data)
        if serializer.os_valid():
            serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        producto.delete()
        return Response(status = status.HTTP_200_OK)
