from django.shortcuts import render

def inicio(request):
    return render(request, 'articulo_list.html')