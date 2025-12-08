from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django import forms
from .models import Articulo

# Formulario rápido basado en el modelo (ajústalo si quieres campos específicos)
class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Articulo
		fields = '__all__'

# CREATE (GET - POST)
def crear_articulo(request):
	# Lógica para crear un nuevo evento
	if request.method == 'POST':
		form = ArticuloForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Artículo creado correctamente.")
			return redirect('listar_articulos')
	else:
		form = ArticuloForm()
	return render(request, 'crear_articulo.html', {'form': form})

# READ (GET)
def listar_articulos(request):
	# Lógica para obtener y mostrar la lista de eventos
	articulos = Articulo.objects.all().order_by('-pk')
	return render(request, 'todos_los_articulos.html', {'articulos': articulos})

# UPDATE (GET - POST)
def actualizar_articulo(request, articulo_id):
	# Lógica para actualizar un evento existente
	articulo = get_object_or_404(Articulo, pk=articulo_id)
	if request.method == 'POST':
		form = ArticuloForm(request.POST, request.FILES, instance=articulo)
		if form.is_valid():
			form.save()
			messages.success(request, "Artículo actualizado correctamente.")
			return redirect('listar_articulos')
	else:
		form = ArticuloForm(instance=articulo)
	return render(request, 'actualizar_articulo.html', {'form': form, 'articulo': articulo})

# DELETE (GET - POST)
def eliminar_articulo(request, articulo_id):
	# Lógica para eliminar un evento existente
	articulo = get_object_or_404(Articulo, pk=articulo_id)
	if request.method == 'POST':
		articulo.delete()
		messages.success(request, "Artículo eliminado correctamente.")
		return redirect('listar_articulos')
	return render(request, 'eliminar_articulo.html', {'articulo': articulo})