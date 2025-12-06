from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def acerca_de(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contact.html')

def caracteristicas(request):
    return render(request, 'feature.html')

