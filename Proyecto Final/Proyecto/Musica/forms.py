from django import forms
from .models import Artista, Album

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'apellido']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'fecha_publicacion']