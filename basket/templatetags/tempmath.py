from django import template

register = template.Library()

@register.filter(name='div')
def convert_total(value1, value2):
    return format(value1/int(value2),".2f")
