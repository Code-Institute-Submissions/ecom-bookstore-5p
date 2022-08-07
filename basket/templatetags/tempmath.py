from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def convert_total(value):
    return format(value / 100, '.2f')

@register.filter
def discount(value, amount):
    return format(value * (1 - Decimal(amount/100)), '.2f')
