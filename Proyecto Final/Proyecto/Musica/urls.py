from django.urls import path
from .views import crearArtista, listarArtista, editarArtista, eliminarArtista, crearAlbum, listarAlbum, login_request

urlpatterns = [
    path('crear_artista/', crearArtista, name='crear_artista'),
    path('listar_artista/', listarArtista, name= 'listar_artista'),
    path('editar_artista/<int:id>', editarArtista, name= 'editar_artista' ),
    path('eliminar_artista/<int:id>', eliminarArtista, name = 'eliminar_artista'),
    path('crear_album', crearAlbum, name = 'crear_album'),
    path('listar_album', listarAlbum, name= 'listar_album'),
    path('login', login_request, name = 'Login'),
]