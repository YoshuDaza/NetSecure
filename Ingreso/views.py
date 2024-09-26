from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError

# Vista de registro
def registrar(request):
    if request.method == 'GET':
        return render(request, 'registro_usuario.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Creación del usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # Iniciar sesión automáticamente después de registrar
                login(request, user)
                return redirect('Perfil')  # Redirige al perfil una vez registrado
            except IntegrityError:
                # Si el nombre de usuario ya existe
                return render(request, 'registro_usuario.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        else:
            # Si las contraseñas no coinciden
            return render(request, 'registro_usuario.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })

# Vista de inicio de sesión
def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        # Autenticar usuario
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # Si el usuario no existe o la contraseña es incorrecta
            return render(request, 'inicio_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Nombre de usuario o contraseña incorrectos'
            })
        else:
            # Iniciar sesión si las credenciales son correctas
            login(request, user)
            return redirect('Perfil')  # Redirige al perfil después de iniciar sesión

# Vista de cierre de sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('/')

# Vistas protegidas por login_required
@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def nuevo_escaneo(request):
    return render(request, 'nuevo_escaneo.html')
