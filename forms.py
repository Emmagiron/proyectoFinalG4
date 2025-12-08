from django import forms
from .models import Articulo, Categoria

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = [
            'titulo', 
            'categoria', 
            'autor', 
            'contenido'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese el título del artículo'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre del autor'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 8,
                'placeholder': 'Escribe el contenido completo del artículo aquí...'
            }),
        }
        labels = {
            'titulo': 'Título de la Publicación',
            'categoria': 'Categoría Principal',
            'autor': 'Nombre del Autor',
            'contenido': 'Contenido',
        }