from django.shortcuts import render

# Create your views here.
def listar_eventos(request):
    # Lógica para obtener y mostrar la lista de eventos
    return render(request, 'todos_los_eventos.html')