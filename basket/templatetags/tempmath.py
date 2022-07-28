from django import template

register = template.Library()

@register.filter
def convert_total(value):
    return format(value / 100, ".2f")
