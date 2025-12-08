from django.shortcuts import render

## ---CRUD---

# CREATE (GET - POST)

# READ (GET)
def listar_articulos(request):
    # Lógica para obtener y mostrar la lista de eventos
    return render(request, 'todos_los_articulos.html')

# UPDATE (GET - POST)

# DELETE (GET - POST)
