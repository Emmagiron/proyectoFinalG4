# Archivo: blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post  # Importa tu modelo Post

# 1. Función para la página principal del blog (Lista de posts)
# Esta vista corresponde a la ruta: path('', views.blog_home, name='blog_home')
def blog_home(request):
    posts = Post.objects.all() # Obtiene todos los posts
    return render(request, 'blog/blog_home.html', {'posts': posts})

# 2. FUNCIÓN PARA EL DETALLE DEL POST (ESTA ES LA QUE FALTABA O ESTABA MAL NOMBRADA)
# Esta vista corresponde a la ruta: path('<int:pk>/', views.post_detalle, name='post_detalle')
def post_detalle(request, pk):
    # Busca el post por ID (pk) o genera un error 404
    post = get_object_or_404(Post, pk=pk) 
    return render(request, 'blog/post_detalle.html', {'post': post})