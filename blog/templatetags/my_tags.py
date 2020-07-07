from django import template

register = template.Library()

@register.filter(name='getAt') 
def getItemAt(index, list):
    return list[index]