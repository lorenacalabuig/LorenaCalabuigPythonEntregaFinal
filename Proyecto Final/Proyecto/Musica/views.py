from django.shortcuts import render, redirect
from .forms import ArtistaForm, AlbumForm
from .models import Artista, Album
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def Home(request):
    return render(request, 'index.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login (request, user)
                return render(request, 'index.html', {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, 'index.html', {"mensaje":"ERROR DE DATOS"})
        else:
            return render(request, 'index.html', {"mensaje":"FORMULARIO ERRONEO"})
    form = AuthenticationForm()

    return render(request, 'login.html', {'form':form})


def crearArtista(request):
    if request.method == 'POST':
        artista_form = ArtistaForm(request.POST)
        if artista_form.is_valid():
            artista_form.save()
            return redirect('index.html')
    else:
        artista_form = ArtistaForm()
    return render(request, 'crear_artista.html',{'artista_form':artista_form})


def listarArtista(request):
    artistas = Artista.objects.all()
    return render(request, 'listar_artista.html', {'artistas': artistas})

def editarArtista(request,id):
    artista_form = None
    error = None
    try:
        artista= Artista.objects.get(id = id)
        if request.method == "GET":
            artista_form= ArtistaForm(instance=artista)
        else:
            artista_form = ArtistaForm(request.POST, instance= artista)
            if artista_form.is_valid():
                artista_form.save()
            return redirect('index.html')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'crear_artista.html', {'artista_form': artista_form, 'error': error})

def eliminarArtista(request, id):
    artista = Artista.objects.get(id=id)
    if request.method == 'POST':
        artista.delete()
        return redirect('listar_artista')
    return render(request,'eliminar_artista.html',{'artista': artista})

def crearAlbum(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('index.html')
    else:
        album_form = AlbumForm()
    return render(request, 'crear_album.html',{'album_form':album_form})

def listarAlbum(request):
    albumes = Album.objects.all()
    return render(request, 'listar_album.html', {'albumes': albumes})