from django import template

register = template.Library()

@register.filter(name='tiene_grupo')
def tiene_grupo(user, grupo_nombre):
    return user.groups.filter(name=grupo_nombre).exists()

'''
def designar_grupo(user, grupo_nombre):
    if user.is_authenticated:
        return user.groups.filter(name=grupo_nombre).exists()
    return False
'''