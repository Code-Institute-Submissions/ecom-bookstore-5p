from django import template

register = template.Library()

@register.filter(name='div')
def div(value1, value2):
    return value1/int(value2)