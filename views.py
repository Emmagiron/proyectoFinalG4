from django.shortcuts import render

# --- CRUD de Artículos ---

# READ: lista todos los artículos
def articulos_todos_los(request):
    return render(request, 'articulos_todos_los.html')

# CREATE: crear un artículo
def articulos_crear(request):
    return render(request, 'articulos_crear.html')

# READ: detalle de un artículo
def articulos_detalle(request, id):
    return render(request, 'articulos_detalle.html', {'id': id})

# UPDATE: modificar un artículo
def articulos_modificar(request, id):
    return render(request, 'articulos_modificar.html', {'id': id})
