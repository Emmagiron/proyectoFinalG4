from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from .models import Articulo
from django.urls import reverse_lazy

class ArticuloListView(ListView):
    model = Articulo 
    template_name = 'articulos/articulo_list.html' 
    context_object_name = 'articulos_list' 

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'articulos/articulo_detail.html'

class ArticuloCreateView(CreateView):
    model = Articulo
    template_name = 'articulos/articulo_form.html'
    fields = ['titulo', 'contenido', 'autor'] 
    
    def get_success_url(self):
        return reverse_lazy('articulos:detalle', kwargs={'pk': self.object.pk})

class ArticuloUpdateView(UpdateView):
    model = Articulo
    template_name = 'articulos/articulo_form.html'
    fields = ['titulo', 'contenido', 'autor']
    
    def get_success_url(self):
        return reverse_lazy('articulos:detalle', kwargs={'pk': self.object.pk})

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'articulos/articulo_confirm_delete.html'
    success_url = reverse_lazy('articulos:lista')