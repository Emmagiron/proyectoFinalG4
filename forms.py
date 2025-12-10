from django import forms
from .models import Articulo, Categoria, Comentario 


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = [
            'titulo', 
            'categoria', 
            'autor', 
            'contenido',
            'imagen'
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
            # No se necesita widget para 'imagen' ya que es un FileInput por defecto.
        }
        labels = {
            'titulo': 'Título de la Publicación',
            'categoria': 'Categoría Principal',
            'autor': 'Nombre del Autor',
            'contenido': 'Contenido',
        }


class ComentarioForm(forms.ModelForm):
    """
    Formulario para que los usuarios dejen comentarios en un artículo.
    """
    class Meta:
        model = Comentario
        # Solo necesitamos que el usuario ingrese el autor y el contenido.
        fields = ['autor', 'contenido']
        
        widgets = {
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre o seudónimo',
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe tu comentario...',
            }),
        }
        
        labels = {
            'autor': 'Nombre',
            'contenido': 'Comentario',
        }