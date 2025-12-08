# Importaciones de Django
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect, render 
from django.db.models import Q # ⬅️ Necesario para la búsqueda OR

# Importaciones de tu aplicación
from .models import Articulo, Comentario, Categoria 
from .forms import ArticuloForm, ComentarioForm 

# ------------------- VISTAS DE ARTÍCULO (CLASES) -------------------

class ArticuloListView(ListView):
    model = Articulo 
    template_name = 'articulos/articulo_list.html' 
    context_object_name = 'articulos_list'
    paginate_by = 5 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
 
class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'articulos/articulo_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm() 
        return context

class ArticuloCreateView(CreateView):
    model = Articulo
    template_name = 'articulos/articulo_form.html'
    form_class = ArticuloForm
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('articulos:detalle', kwargs={'pk': self.object.pk})

class ArticuloUpdateView(UpdateView):
    model = Articulo
    template_name = 'articulos/articulo_form.html'
    form_class = ArticuloForm
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('articulos:detalle', kwargs={'pk': self.object.pk})

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'articulos/articulo_confirm_delete.html'
    success_url = reverse_lazy('articulos:lista')

# ------------------- VISTA PARA FILTRADO POR CATEGORÍA -------------------

class ArticulosPorCategoriaListView(ListView):
    model = Articulo
    template_name = 'articulos/articulo_list.html'
    context_object_name = 'articulos_list'
    paginate_by = 5 
    
    def get_queryset(self):
        categoria_pk = self.kwargs.get('pk')
        return Articulo.objects.filter(categoria__pk=categoria_pk).order_by('-fecha_creacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_pk = self.kwargs.get('pk')
        context['categoria_actual'] = get_object_or_404(Categoria, pk=categoria_pk)
        context['categorias'] = Categoria.objects.all() 
        return context

# ------------------- VISTA PARA BÚSQUEDA GLOBAL -------------------

class ArticuloSearchView(ListView):
    model = Articulo
    template_name = 'articulos/articulo_list.html' 
    context_object_name = 'articulos_list'
    paginate_by = 5 
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if query:
            # Filtra por título O contenido (insensible a mayúsculas)
            lookups = Q(titulo__icontains=query) | Q(contenido__icontains=query)
            return Articulo.objects.filter(lookups).order_by('-fecha_creacion')
        
        return Articulo.objects.none() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['categorias'] = Categoria.objects.all() 
        return context

# ------------------- VISTA DE COMENTARIO (FUNCIÓN) -------------------

def crear_comentario(request, pk):
    """
    Vista para procesar la creación de comentarios adjuntos a un artículo.
    """
    articulo = get_object_or_404(Articulo, pk=pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.save()
            return redirect('articulos:detalle', pk=articulo.pk)
    
    return redirect('articulos:detalle', pk=articulo.pk)