

from django.shortcuts import render
    

def acerca_de(request):
    miembros = [
        {'nombre': 'Román Huel', 'rol': 'Líder Técnico y Desarrollador Backend', 'contribucion': 'Arquitectura de modelos, lógica de filtrado, implementación de vistas CRUD.'},
        {'nombre': 'Valentina Sapag', 'rol': 'Diseñadora Frontend y Administradora', 'contribucion': 'Maquetación HTML/CSS, adaptación responsive, implementación de Comentarios y Registro.'},
        {'nombre': 'Emmanuel Girón', 'rol': 'Diseñador Frontend y Administrador', 'contribucion': 'Maquetación HTML/CSS, adaptación responsive, implementación de Comentarios y Registro.'},
        {'nombre': 'Maria Celeste Zapata', 'rol': 'Diseñadora Frontend y Administradora', 'contribucion': 'Maquetación HTML/CSS, adaptación responsive, implementación de Comentarios y Registro.'}
    ]

    return render(request, 'acerca_de.html', {'miembros': miembros})
