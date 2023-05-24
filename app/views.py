from django.shortcuts import render, redirect
from .forms import  CustomUserForm
from django.contrib.auth import  authenticate, login


def indexView(request):
    return render(request, 'index.html', {})

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
            return redirect(to= 'home')
        data ["form"] = formulario


    return render (request, 'registrar.html' , data )