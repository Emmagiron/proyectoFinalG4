

from django.shortcuts import render
    

def acerca_de(request):
    """
    Vista que renderiza la plantilla 'Acerca de'.
    Aquí no se necesita lógica de base de datos, solo mostrar el HTML.
    """
    return render(request, 'acerca_de.html', {}) 
