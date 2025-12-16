from django.shortcuts import redirect, get_object_or_404
#from django.contrib.auth import login
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.contrib.auth.decorators import login_required
from django.db.models import Q 

from .forms import ArticuloForm, ComentarioForm
from .models import Articulo, Categoria, Comentario 


class HomeView(TemplateView):
    template_name = 'home.html'

class AcercaDeView(TemplateView):
    template_name = 'acerca_de.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['miembros'] = [
            {'nombre': 'Román Huel', 'rol': 'Líder Técnico y Desarrollador Backend', 'contribucion': 'Arquitectura de modelos, lógica de filtrado, implementación de vistas CRUD.'},
            {'nombre': 'Valentina Sapag', 'rol': 'Diseñadora Frontend y Administradora', 'contribucion': 'Maquetación HTML/CSS, adaptación responsive, implementación de Comentarios y Registro.'},
            {'nombre': 'Emmanuel Girón', 'rol': 'Diseñador Frontend y Administrador', 'contribucion': 'Maquetación HTML/CSS, adaptación responsive, implementación de Comentarios y Registro.'},
            {'nombre': 'Maria Celeste Zapata', 'rol': 'Diseñadora Frontend y Administradora', 'contribucion': 'Maquetación HTML/CSS, adaptación responsive, implementación de Comentarios y Registro.'}
        ]
        return context


class ContactoView(TemplateView):
    template_name = 'contacto.html'


class ArticuloListView(ListView):
    model = Articulo 
    template_name = 'articulos/articulo_list.html' 
    context_object_name = 'object_list'
    paginate_by = 5

    def get_queryset(self):
        orden = self.request.GET.get('orden', 'fecha_desc')

        if orden == 'fecha_asc':
            ordering = 'fecha_creacion'
        elif orden == 'fecha_desc':
            ordering = '-fecha_creacion'
        elif orden == 'titulo_asc':
            ordering = 'titulo'
        elif orden == 'titulo_desc':
            ordering = '-titulo'
        else:
            ordering = '-fecha_creacion'

        return Articulo.objects.all().order_by(ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['orden_actual'] = self.request.GET.get('orden', 'desc') 
        return context


class ArticuloPorCategoriaListView(ListView):
    model = Articulo
    template_name = 'articulos/articulo_list.html' 
    context_object_name = 'object_list'
    paginate_by = 5

    def get_queryset(self):
        categoria_pk = self.kwargs['pk']
        categoria = get_object_or_404(Categoria, pk=categoria_pk)
        
        orden = self.request.GET.get('orden', 'desc')

        if orden == 'asc':
            ordering = 'fecha_creacion'
        else:
            ordering = '-fecha_creacion'
        
        return Articulo.objects.filter(categorias=categoria).order_by(ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_pk = self.kwargs['pk']
        context['categorias'] = Categoria.objects.all()
        context['categoria_actual'] = get_object_or_404(Categoria, pk=categoria_pk)
        context['orden_actual'] = self.request.GET.get('orden', 'desc') 
        return context


class ArticuloDetailView(DetailView):
    model = Articulo 
    template_name = 'articulos/articulo_detail.html' 
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        if not hasattr(self, 'object') or self.object is None:
            self.object = self.get_object() 
            
        context = super().get_context_data(**kwargs)
        
        context['comentarios'] = self.object.comentario_set.all().order_by('-fecha')
        
        if 'form' not in context:
            context['form'] = ComentarioForm() 
            
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            comentario = form.save(commit=False)
            comentario.articulo = self.object
            comentario.autor = request.user
            comentario.save()
            
            return redirect(self.object.get_absolute_url() + '#comentarios')
        
        context = self.get_context_data(object=self.object)
        context['form'] = form
        return self.render_to_response(context)


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm 
    template_name = 'articulos/articulo_form.html'
    success_url = reverse_lazy('articulos:lista')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class ArticuloUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulos/articulo_form.html'
    
    def test_func(self):
        obj = self.get_object()
        return (
            obj.autor == self.request.user
            or self.request.user.is_staff
            or self.request.user.groups.filter(name='Moderador').exists()
        )


class ArticuloDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = 'articulos/articulo_confirm_delete.html'
    success_url = reverse_lazy('articulos:lista')
    
    def test_func(self):
        obj = self.get_object()
        return (
            obj.autor == self.request.user
            or self.request.user.is_staff
            or self.request.user.groups.filter(name='Moderador').exists()
        )



class ArticuloPorCategoriaListView(ListView):
    model = Articulo
    template_name = 'articulos/articulo_list.html' 
    context_object_name = 'object_list'
    paginate_by = 5

    def get_queryset(self):
        categoria_pk = self.kwargs['pk']
        categoria = get_object_or_404(Categoria, pk=categoria_pk)
        return Articulo.objects.filter(categorias=categoria).order_by('-fecha_creacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_pk = self.kwargs['pk']
        context['categorias'] = Categoria.objects.all()
        context['categoria_actual'] = get_object_or_404(Categoria, pk=categoria_pk)
        return context


class ArticuloBusquedaListView(ListView):
    model = Articulo
    template_name = 'articulos/articulo_list.html'
    context_object_name = 'object_list'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Articulo.objects.filter(
                Q(titulo__icontains=query) | Q(contenido__icontains=query)
            ).distinct().order_by('-fecha_creacion')
        else:
            object_list = Articulo.objects.none()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busqueda_q'] = self.request.GET.get('q')
        context['categorias'] = Categoria.objects.all()
        return context


class ComentarioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'articulos/comentario_form.html'

    def get_success_url(self):
        return self.object.articulo.get_absolute_url()
        
    def test_func(self):
        obj = self.get_object()
        return (obj.autor == self.request.user if obj.autor else False) or self.request.user.is_staff or self.request.user.groups.filter(name='Moderador').exists()


class ComentarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comentario
    template_name = 'articulos/comentario_confirm_delete.html' 
    
    def get_success_url(self):
        return self.object.articulo.get_absolute_url()

    def test_func(self):
        obj = self.get_object()
        return (obj.autor == self.request.user if obj.autor else False) or self.request.user.is_staff or self.request.user.groups.filter(name='Moderador').exists()