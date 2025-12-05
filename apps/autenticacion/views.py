from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrarUsuarioForm, IngresarUsuarioForm

def registrar_usuario(request):
    # POST
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente.")
            return redirect('apps.autenticacion:ingresar')
    # GET
    else:
        form = RegistrarUsuarioForm()

    return render(request, 'autenticacion/registrar.html', {'form': form})

def ingresar_usuario(request):
    # POST
    if request.method == 'POST':
        form = IngresarUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, "Credenciales inválidas. Inténtalo de nuevo.")
    # GET
    else:
        form = IngresarUsuarioForm()

    return render(request, 'autenticacion/ingresar.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('apps.autenticacion:ingresar')